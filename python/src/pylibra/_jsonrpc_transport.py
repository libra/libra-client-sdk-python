# pyre-strict

import dataclasses
import requests
import typing

from . import NETWORK_DEFAULT, ENDPOINT_CONFIG
from ._types import SignedTransaction, Event, PaymentEvent, AccountResource
from ._transport import BaseLibraNetwork, ClientError, SubmitTransactionError


@dataclasses.dataclass
class ServerError:
    code: int
    data: dict
    message: str


@dataclasses.dataclass
class GetAccountStateResp:
    sequence_number: int
    authentication_key: str
    delegated_key_rotation_capability: bool
    delegated_withdrawal_capability: bool
    balance: int
    sent_events_key: str
    received_events_key: str


@dataclasses.dataclass
class GetMetadataResp:
    version: int
    timestamp: int


@dataclasses.dataclass
class SubmitResp:
    pass


@dataclasses.dataclass
class JSONUserTransaction:
    type: str
    sender: str
    signature_scheme: str
    signature: str
    public_key: str
    sequence_number: int
    max_gas_amount: int
    gas_unit_price: int
    expiration_time: int
    gas_used: int
    script_hash: str
    script: object


@dataclasses.dataclass
class JSONTransaction:
    version: int
    events: object
    transaction: typing.Union[JSONUserTransaction]


class JSONSignedTransaction(SignedTransaction):
    _result: dict
    _transaction: dict

    def __init__(self, result: dict):
        self._result = result
        self._transaction = result["transaction"]

    def __repr__(self):
        return repr(self._result)

    @property
    def sender(self) -> bytes:
        return bytes.fromhex(self._transaction["sender"])

    @property
    def sequence(self) -> int:
        return self._transaction["sequence_number"]

    @property
    def max_gas_amount(self) -> int:
        return self._transaction["max_gas_amount"]

    @property
    def gas_unit_price(self) -> int:
        return self._transaction["gas_unit_price"]

    @property
    def expiration_time(self) -> int:
        return self._transaction["expiration_time"]

    @property
    def is_p2p(self) -> bool:
        return self._transaction["script"]["type"] == "peer_to_peer_transaction"

    @property
    def is_mint(self) -> bool:
        return self._transaction["script"]["type"] == "mint_transaction"

    @property
    def receiver(self) -> bytes:
        return self._transaction["script"]["receiver"]

    @property
    def amount(self) -> int:
        return self._transaction["script"]["amount"]

    @property
    def public_key(self) -> bytes:
        return self._transaction["public_key"]

    @property
    def signature(self) -> bytes:
        return self._transaction["signature"]

    @property
    def version(self) -> int:
        return self._result["version"]

    @property
    def gas(self) -> int:
        return self._result["gas_used"]


class JSONAccountResource(AccountResource):
    _address: bytes
    _state: GetAccountStateResp

    def __init__(self, address_hex: str, state: GetAccountStateResp):
        self._address = bytes.fromhex(address_hex)
        self._state = state

    @property
    def address(self) -> bytes:
        return self._address

    @property
    def balance(self) -> int:
        return self._state.balance

    @property
    def sequence(self) -> int:
        return self._state.sequence_number

    @property
    def authentication_key(self) -> bytes:
        return bytes.fromhex(self._state.authentication_key)

    @property
    def delegated_key_rotation_capability(self) -> bool:
        return self._state.delegated_key_rotation_capability

    @property
    def delegated_withdrawal_capability(self) -> bool:
        return self._state.delegated_withdrawal_capability

    @property
    def sent_events_key(self) -> bytes:
        return bytes.fromhex(self._state.sent_events_key)

    @property
    def received_events_key(self) -> bytes:
        return bytes.fromhex(self._state.received_events_key)


class JSONPaymentEvent(PaymentEvent):
    _ev_dict: dict

    def __init__(self, ev_dict: dict):
        self._ev_dict = ev_dict

    @property
    def is_sent(self) -> bool:
        return self._ev_dict["data"]["type"] == "sentpayment"

    @property
    def is_received(self) -> bool:
        return self._ev_dict["data"]["type"] == "receivedpayment"

    @property
    def sender_address(self) -> bytes:
        if self.is_sent:
            return bytes.fromhex(self._ev_dict["key"][8:])
        else:
            return bytes.fromhex(self._ev_dict["data"]["sender"])

    @property
    def receiver_address(self) -> bytes:
        if self.is_sent:
            return bytes.fromhex(self._ev_dict["data"]["receiver"])
        else:
            return bytes.fromhex(self._ev_dict["key"][8:])

    @property
    def amount(self) -> int:
        return self._ev_dict["data"]["amount"]

    @property
    def metadata(self) -> bytes:
        return bytes.fromhex(self._ev_dict["data"]["metadata"])

    @property
    def module(self) -> str:
        return "LibraAccount"

    @property
    def name(self) -> str:
        return "SentPayment" if self.is_sent else "ReceivedPayment"


class JSONUnknownEvent(Event):
    @property
    def module(self) -> str:
        return "Unknown"

    @property
    def name(self) -> str:
        return "Unknown"


def as_result_or_error(cls: typing.ClassVar):
    def _as_result_or_error(x: dict):
        if "result" in x:
            if x["result"] is not None:
                return cls(**(x["result"]))
            else:
                return None
        else:
            return ServerError(**(x["error"]))

    return _as_result_or_error


T = typing.TypeVar("T")


def make_json_rpc_request(
    url: str, session: requests.Session, method: str, params: typing.List[typing.Any], result_class: typing.Optional[T]
) -> typing.Union[ServerError, T, dict]:
    req = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params,
    }

    try:
        resp = session.post(url, json=req, timeout=1)
        resp.raise_for_status()
    except requests.RequestException as e:
        raise ClientError("API Error: " + str(e))

    result_object = resp.json()

    assert result_object["jsonrpc"] == "2.0"
    assert result_object["id"] == 1
    if result_class is None:
        if "error" in result_object:
            raise ClientError("Server returned error:" + str(result_object))
        return result_object["result"]

    result_or_error = as_result_or_error(result_class)(result_object)

    if isinstance(result_or_error, ServerError):
        print(str(result_or_error))

    return result_or_error


class LibraNetwork(BaseLibraNetwork):
    def __init__(self, network: str = NETWORK_DEFAULT):
        self._url = ENDPOINT_CONFIG[network]["json-rpc"]
        self._session = requests.sessions.Session()

    def currentTimestampUsecs(self) -> int:
        result = make_json_rpc_request(self._url, self._session, "get_metadata", [], GetMetadataResp)
        print(result)
        return result.timestamp

    def getAccount(self, address_hex: str) -> typing.Optional[AccountResource]:
        resp = make_json_rpc_request(self._url, self._session, "get_account_state", [address_hex], GetAccountStateResp)
        if resp is None:
            return None
        elif isinstance(resp, GetAccountStateResp):
            return JSONAccountResource(address_hex, resp)
        else:
            raise ClientError(str(resp))

    def sendTransaction(self, signed_transaction_bytes: bytes) -> None:
        resp = make_json_rpc_request(self._url, self._session, "submit", [signed_transaction_bytes.hex()], SubmitResp)
        if resp is None:
            return None
        elif isinstance(resp, SubmitResp):
            return None
        else:
            raise SubmitTransactionError(resp.code, resp.message, resp.data)

    def transactions_by_range(
        self, start_version: int, limit: int, include_events: bool = False
    ) -> typing.List[typing.Tuple[SignedTransaction, typing.List[typing.Union[Event, PaymentEvent]]]]:
        resp_dict = make_json_rpc_request(
            self._url, self._session, "get_transactions", [start_version, limit, include_events], None
        )

        results = []
        for tx_dict in resp_dict:
            tx = None
            events = []

            if include_events:
                for e_dict in tx_dict["events"]:
                    if e_dict["data"]["type"] == "sentpayment" or e_dict["data"]["type"] == "receivedpayment":
                        events.append(JSONPaymentEvent(e_dict))
                    else:
                        events.append(JSONUnknownEvent())

            if tx_dict["transaction"]["type"] == "user":
                tx = JSONSignedTransaction(tx_dict)

            results.append((tx, events))

        return results

    def transaction_by_acc_seq(
        self, addr_hex: str, seq: int, include_events: bool = False
    ) -> typing.Tuple[typing.Optional[SignedTransaction], typing.List[typing.Union[Event, PaymentEvent]]]:
        resp_dict = make_json_rpc_request(
            self._url, self._session, "get_account_transaction", [addr_hex, seq, include_events], None
        )

        events = []

        if resp_dict is None:
            return None, events

        if include_events and len(resp_dict["events"]):
            for e_dict in resp_dict["events"]:
                if e_dict["data"]["type"] == "sentpayment" or e_dict["data"]["type"] == "receivedpayment":
                    events.append(JSONPaymentEvent(e_dict))
                else:
                    events.append(JSONUnknownEvent())

        if resp_dict["transaction"]["type"] != "user":
            raise ClientError("Unexpected response: " + str(resp_dict))

        res = JSONSignedTransaction(resp_dict)

        return res, events

    def get_events(self, key_hex: str, start: int, limit: int) -> typing.List[typing.Union[Event, PaymentEvent]]:
        resp_list = make_json_rpc_request(self._url, self._session, "get_events", [key_hex, start, limit], None)

        events = []

        for e_dict in resp_list:
            if e_dict["data"]["type"] == "sentpayment" or e_dict["data"]["type"] == "receivedpayment":
                events.append(JSONPaymentEvent(e_dict))
            else:
                events.append(JSONUnknownEvent())

        return events