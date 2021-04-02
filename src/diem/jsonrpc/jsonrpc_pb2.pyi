"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class Amount(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    amount: builtin___int = ...
    currency: typing___Text = ...
    def __init__(
        self,
        *,
        amount: typing___Optional[builtin___int] = None,
        currency: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["amount", b"amount", "currency", b"currency"]
    ) -> None: ...

type___Amount = Amount

class Account(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    address: typing___Text = ...
    sequence_number: builtin___int = ...
    authentication_key: typing___Text = ...
    sent_events_key: typing___Text = ...
    received_events_key: typing___Text = ...
    delegated_key_rotation_capability: builtin___bool = ...
    delegated_withdrawal_capability: builtin___bool = ...
    is_frozen: builtin___bool = ...
    @property
    def balances(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___Amount]: ...
    @property
    def role(self) -> type___AccountRole: ...
    def __init__(
        self,
        *,
        address: typing___Optional[typing___Text] = None,
        balances: typing___Optional[typing___Iterable[type___Amount]] = None,
        sequence_number: typing___Optional[builtin___int] = None,
        authentication_key: typing___Optional[typing___Text] = None,
        sent_events_key: typing___Optional[typing___Text] = None,
        received_events_key: typing___Optional[typing___Text] = None,
        delegated_key_rotation_capability: typing___Optional[builtin___bool] = None,
        delegated_withdrawal_capability: typing___Optional[builtin___bool] = None,
        is_frozen: typing___Optional[builtin___bool] = None,
        role: typing___Optional[type___AccountRole] = None,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal["role", b"role"]) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "address",
            b"address",
            "authentication_key",
            b"authentication_key",
            "balances",
            b"balances",
            "delegated_key_rotation_capability",
            b"delegated_key_rotation_capability",
            "delegated_withdrawal_capability",
            b"delegated_withdrawal_capability",
            "is_frozen",
            b"is_frozen",
            "received_events_key",
            b"received_events_key",
            "role",
            b"role",
            "sent_events_key",
            b"sent_events_key",
            "sequence_number",
            b"sequence_number",
        ],
    ) -> None: ...

type___Account = Account

class AccountRole(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type: typing___Text = ...
    parent_vasp_address: typing___Text = ...
    human_name: typing___Text = ...
    base_url: typing___Text = ...
    expiration_time: builtin___int = ...
    compliance_key: typing___Text = ...
    compliance_key_rotation_events_key: typing___Text = ...
    base_url_rotation_events_key: typing___Text = ...
    num_children: builtin___int = ...
    received_mint_events_key: typing___Text = ...
    @property
    def preburn_balances(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___Amount]: ...
    def __init__(
        self,
        *,
        type: typing___Optional[typing___Text] = None,
        parent_vasp_address: typing___Optional[typing___Text] = None,
        human_name: typing___Optional[typing___Text] = None,
        base_url: typing___Optional[typing___Text] = None,
        expiration_time: typing___Optional[builtin___int] = None,
        compliance_key: typing___Optional[typing___Text] = None,
        compliance_key_rotation_events_key: typing___Optional[typing___Text] = None,
        base_url_rotation_events_key: typing___Optional[typing___Text] = None,
        num_children: typing___Optional[builtin___int] = None,
        received_mint_events_key: typing___Optional[typing___Text] = None,
        preburn_balances: typing___Optional[typing___Iterable[type___Amount]] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "base_url",
            b"base_url",
            "base_url_rotation_events_key",
            b"base_url_rotation_events_key",
            "compliance_key",
            b"compliance_key",
            "compliance_key_rotation_events_key",
            b"compliance_key_rotation_events_key",
            "expiration_time",
            b"expiration_time",
            "human_name",
            b"human_name",
            "num_children",
            b"num_children",
            "parent_vasp_address",
            b"parent_vasp_address",
            "preburn_balances",
            b"preburn_balances",
            "received_mint_events_key",
            b"received_mint_events_key",
            "type",
            b"type",
        ],
    ) -> None: ...

type___AccountRole = AccountRole

class Event(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    key: typing___Text = ...
    sequence_number: builtin___int = ...
    transaction_version: builtin___int = ...
    @property
    def data(self) -> type___EventData: ...
    def __init__(
        self,
        *,
        key: typing___Optional[typing___Text] = None,
        sequence_number: typing___Optional[builtin___int] = None,
        transaction_version: typing___Optional[builtin___int] = None,
        data: typing___Optional[type___EventData] = None,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal["data", b"data"]) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "data",
            b"data",
            "key",
            b"key",
            "sequence_number",
            b"sequence_number",
            "transaction_version",
            b"transaction_version",
        ],
    ) -> None: ...

type___Event = Event

class EventData(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type: typing___Text = ...
    preburn_address: typing___Text = ...
    currency_code: typing___Text = ...
    new_to_xdx_exchange_rate: builtin___float = ...
    sender: typing___Text = ...
    receiver: typing___Text = ...
    metadata: typing___Text = ...
    epoch: builtin___int = ...
    round: builtin___int = ...
    proposer: typing___Text = ...
    proposed_time: builtin___int = ...
    destination_address: typing___Text = ...
    new_compliance_public_key: typing___Text = ...
    new_base_url: typing___Text = ...
    time_rotated_seconds: builtin___int = ...
    created_address: typing___Text = ...
    role_id: builtin___int = ...
    committed_timestamp_secs: builtin___int = ...
    @property
    def amount(self) -> type___Amount: ...
    def __init__(
        self,
        *,
        type: typing___Optional[typing___Text] = None,
        amount: typing___Optional[type___Amount] = None,
        preburn_address: typing___Optional[typing___Text] = None,
        currency_code: typing___Optional[typing___Text] = None,
        new_to_xdx_exchange_rate: typing___Optional[builtin___float] = None,
        sender: typing___Optional[typing___Text] = None,
        receiver: typing___Optional[typing___Text] = None,
        metadata: typing___Optional[typing___Text] = None,
        epoch: typing___Optional[builtin___int] = None,
        round: typing___Optional[builtin___int] = None,
        proposer: typing___Optional[typing___Text] = None,
        proposed_time: typing___Optional[builtin___int] = None,
        destination_address: typing___Optional[typing___Text] = None,
        new_compliance_public_key: typing___Optional[typing___Text] = None,
        new_base_url: typing___Optional[typing___Text] = None,
        time_rotated_seconds: typing___Optional[builtin___int] = None,
        created_address: typing___Optional[typing___Text] = None,
        role_id: typing___Optional[builtin___int] = None,
        committed_timestamp_secs: typing___Optional[builtin___int] = None,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal["amount", b"amount"]) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "amount",
            b"amount",
            "committed_timestamp_secs",
            b"committed_timestamp_secs",
            "created_address",
            b"created_address",
            "currency_code",
            b"currency_code",
            "destination_address",
            b"destination_address",
            "epoch",
            b"epoch",
            "metadata",
            b"metadata",
            "new_base_url",
            b"new_base_url",
            "new_compliance_public_key",
            b"new_compliance_public_key",
            "new_to_xdx_exchange_rate",
            b"new_to_xdx_exchange_rate",
            "preburn_address",
            b"preburn_address",
            "proposed_time",
            b"proposed_time",
            "proposer",
            b"proposer",
            "receiver",
            b"receiver",
            "role_id",
            b"role_id",
            "round",
            b"round",
            "sender",
            b"sender",
            "time_rotated_seconds",
            b"time_rotated_seconds",
            "type",
            b"type",
        ],
    ) -> None: ...

type___EventData = EventData

class Metadata(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    version: builtin___int = ...
    timestamp: builtin___int = ...
    chain_id: builtin___int = ...
    script_hash_allow_list: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
        typing___Text
    ] = ...
    module_publishing_allowed: builtin___bool = ...
    diem_version: builtin___int = ...
    accumulator_root_hash: typing___Text = ...
    dual_attestation_limit: builtin___int = ...
    def __init__(
        self,
        *,
        version: typing___Optional[builtin___int] = None,
        timestamp: typing___Optional[builtin___int] = None,
        chain_id: typing___Optional[builtin___int] = None,
        script_hash_allow_list: typing___Optional[typing___Iterable[typing___Text]] = None,
        module_publishing_allowed: typing___Optional[builtin___bool] = None,
        diem_version: typing___Optional[builtin___int] = None,
        accumulator_root_hash: typing___Optional[typing___Text] = None,
        dual_attestation_limit: typing___Optional[builtin___int] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "accumulator_root_hash",
            b"accumulator_root_hash",
            "chain_id",
            b"chain_id",
            "diem_version",
            b"diem_version",
            "dual_attestation_limit",
            b"dual_attestation_limit",
            "module_publishing_allowed",
            b"module_publishing_allowed",
            "script_hash_allow_list",
            b"script_hash_allow_list",
            "timestamp",
            b"timestamp",
            "version",
            b"version",
        ],
    ) -> None: ...

type___Metadata = Metadata

class Transaction(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    version: builtin___int = ...
    hash: typing___Text = ...
    bytes: typing___Text = ...
    gas_used: builtin___int = ...
    @property
    def transaction(self) -> type___TransactionData: ...
    @property
    def events(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___Event]: ...
    @property
    def vm_status(self) -> type___VMStatus: ...
    def __init__(
        self,
        *,
        version: typing___Optional[builtin___int] = None,
        transaction: typing___Optional[type___TransactionData] = None,
        hash: typing___Optional[typing___Text] = None,
        bytes: typing___Optional[typing___Text] = None,
        events: typing___Optional[typing___Iterable[type___Event]] = None,
        vm_status: typing___Optional[type___VMStatus] = None,
        gas_used: typing___Optional[builtin___int] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["transaction", b"transaction", "vm_status", b"vm_status"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "bytes",
            b"bytes",
            "events",
            b"events",
            "gas_used",
            b"gas_used",
            "hash",
            b"hash",
            "transaction",
            b"transaction",
            "version",
            b"version",
            "vm_status",
            b"vm_status",
        ],
    ) -> None: ...

type___Transaction = Transaction

class MoveAbortExplaination(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    category: typing___Text = ...
    category_description: typing___Text = ...
    reason: typing___Text = ...
    reason_description: typing___Text = ...
    def __init__(
        self,
        *,
        category: typing___Optional[typing___Text] = None,
        category_description: typing___Optional[typing___Text] = None,
        reason: typing___Optional[typing___Text] = None,
        reason_description: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "category",
            b"category",
            "category_description",
            b"category_description",
            "reason",
            b"reason",
            "reason_description",
            b"reason_description",
        ],
    ) -> None: ...

type___MoveAbortExplaination = MoveAbortExplaination

class VMStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type: typing___Text = ...
    location: typing___Text = ...
    abort_code: builtin___int = ...
    function_index: builtin___int = ...
    code_offset: builtin___int = ...
    @property
    def explanation(self) -> type___MoveAbortExplaination: ...
    def __init__(
        self,
        *,
        type: typing___Optional[typing___Text] = None,
        location: typing___Optional[typing___Text] = None,
        abort_code: typing___Optional[builtin___int] = None,
        function_index: typing___Optional[builtin___int] = None,
        code_offset: typing___Optional[builtin___int] = None,
        explanation: typing___Optional[type___MoveAbortExplaination] = None,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal["explanation", b"explanation"]) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "abort_code",
            b"abort_code",
            "code_offset",
            b"code_offset",
            "explanation",
            b"explanation",
            "function_index",
            b"function_index",
            "location",
            b"location",
            "type",
            b"type",
        ],
    ) -> None: ...

type___VMStatus = VMStatus

class TransactionData(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type: typing___Text = ...
    timestamp_usecs: builtin___int = ...
    sender: typing___Text = ...
    signature_scheme: typing___Text = ...
    signature: typing___Text = ...
    public_key: typing___Text = ...
    sequence_number: builtin___int = ...
    chain_id: builtin___int = ...
    max_gas_amount: builtin___int = ...
    gas_unit_price: builtin___int = ...
    gas_currency: typing___Text = ...
    expiration_timestamp_secs: builtin___int = ...
    script_hash: typing___Text = ...
    script_bytes: typing___Text = ...
    @property
    def script(self) -> type___Script: ...
    def __init__(
        self,
        *,
        type: typing___Optional[typing___Text] = None,
        timestamp_usecs: typing___Optional[builtin___int] = None,
        sender: typing___Optional[typing___Text] = None,
        signature_scheme: typing___Optional[typing___Text] = None,
        signature: typing___Optional[typing___Text] = None,
        public_key: typing___Optional[typing___Text] = None,
        sequence_number: typing___Optional[builtin___int] = None,
        chain_id: typing___Optional[builtin___int] = None,
        max_gas_amount: typing___Optional[builtin___int] = None,
        gas_unit_price: typing___Optional[builtin___int] = None,
        gas_currency: typing___Optional[typing___Text] = None,
        expiration_timestamp_secs: typing___Optional[builtin___int] = None,
        script_hash: typing___Optional[typing___Text] = None,
        script_bytes: typing___Optional[typing___Text] = None,
        script: typing___Optional[type___Script] = None,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal["script", b"script"]) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "chain_id",
            b"chain_id",
            "expiration_timestamp_secs",
            b"expiration_timestamp_secs",
            "gas_currency",
            b"gas_currency",
            "gas_unit_price",
            b"gas_unit_price",
            "max_gas_amount",
            b"max_gas_amount",
            "public_key",
            b"public_key",
            "script",
            b"script",
            "script_bytes",
            b"script_bytes",
            "script_hash",
            b"script_hash",
            "sender",
            b"sender",
            "sequence_number",
            b"sequence_number",
            "signature",
            b"signature",
            "signature_scheme",
            b"signature_scheme",
            "timestamp_usecs",
            b"timestamp_usecs",
            "type",
            b"type",
        ],
    ) -> None: ...

type___TransactionData = TransactionData

class Script(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type: typing___Text = ...
    code: typing___Text = ...
    arguments: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    type_arguments: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    receiver: typing___Text = ...
    amount: builtin___int = ...
    currency: typing___Text = ...
    metadata: typing___Text = ...
    metadata_signature: typing___Text = ...
    def __init__(
        self,
        *,
        type: typing___Optional[typing___Text] = None,
        code: typing___Optional[typing___Text] = None,
        arguments: typing___Optional[typing___Iterable[typing___Text]] = None,
        type_arguments: typing___Optional[typing___Iterable[typing___Text]] = None,
        receiver: typing___Optional[typing___Text] = None,
        amount: typing___Optional[builtin___int] = None,
        currency: typing___Optional[typing___Text] = None,
        metadata: typing___Optional[typing___Text] = None,
        metadata_signature: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "amount",
            b"amount",
            "arguments",
            b"arguments",
            "code",
            b"code",
            "currency",
            b"currency",
            "metadata",
            b"metadata",
            "metadata_signature",
            b"metadata_signature",
            "receiver",
            b"receiver",
            "type",
            b"type",
            "type_arguments",
            b"type_arguments",
        ],
    ) -> None: ...

type___Script = Script

class CurrencyInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code: typing___Text = ...
    scaling_factor: builtin___int = ...
    fractional_part: builtin___int = ...
    to_xdx_exchange_rate: builtin___float = ...
    mint_events_key: typing___Text = ...
    burn_events_key: typing___Text = ...
    preburn_events_key: typing___Text = ...
    cancel_burn_events_key: typing___Text = ...
    exchange_rate_update_events_key: typing___Text = ...
    def __init__(
        self,
        *,
        code: typing___Optional[typing___Text] = None,
        scaling_factor: typing___Optional[builtin___int] = None,
        fractional_part: typing___Optional[builtin___int] = None,
        to_xdx_exchange_rate: typing___Optional[builtin___float] = None,
        mint_events_key: typing___Optional[typing___Text] = None,
        burn_events_key: typing___Optional[typing___Text] = None,
        preburn_events_key: typing___Optional[typing___Text] = None,
        cancel_burn_events_key: typing___Optional[typing___Text] = None,
        exchange_rate_update_events_key: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "burn_events_key",
            b"burn_events_key",
            "cancel_burn_events_key",
            b"cancel_burn_events_key",
            "code",
            b"code",
            "exchange_rate_update_events_key",
            b"exchange_rate_update_events_key",
            "fractional_part",
            b"fractional_part",
            "mint_events_key",
            b"mint_events_key",
            "preburn_events_key",
            b"preburn_events_key",
            "scaling_factor",
            b"scaling_factor",
            "to_xdx_exchange_rate",
            b"to_xdx_exchange_rate",
        ],
    ) -> None: ...

type___CurrencyInfo = CurrencyInfo

class StateProof(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ledger_info_with_signatures: typing___Text = ...
    epoch_change_proof: typing___Text = ...
    ledger_consistency_proof: typing___Text = ...
    def __init__(
        self,
        *,
        ledger_info_with_signatures: typing___Optional[typing___Text] = None,
        epoch_change_proof: typing___Optional[typing___Text] = None,
        ledger_consistency_proof: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "epoch_change_proof",
            b"epoch_change_proof",
            "ledger_consistency_proof",
            b"ledger_consistency_proof",
            "ledger_info_with_signatures",
            b"ledger_info_with_signatures",
        ],
    ) -> None: ...

type___StateProof = StateProof

class AccountStateWithProof(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    version: builtin___int = ...
    blob: typing___Text = ...
    @property
    def proof(self) -> type___AccountStateProof: ...
    def __init__(
        self,
        *,
        version: typing___Optional[builtin___int] = None,
        blob: typing___Optional[typing___Text] = None,
        proof: typing___Optional[type___AccountStateProof] = None,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal["proof", b"proof"]) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["blob", b"blob", "proof", b"proof", "version", b"version"]
    ) -> None: ...

type___AccountStateWithProof = AccountStateWithProof

class AccountStateProof(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ledger_info_to_transaction_info_proof: typing___Text = ...
    transaction_info: typing___Text = ...
    transaction_info_to_account_proof: typing___Text = ...
    def __init__(
        self,
        *,
        ledger_info_to_transaction_info_proof: typing___Optional[typing___Text] = None,
        transaction_info: typing___Optional[typing___Text] = None,
        transaction_info_to_account_proof: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "ledger_info_to_transaction_info_proof",
            b"ledger_info_to_transaction_info_proof",
            "transaction_info",
            b"transaction_info",
            "transaction_info_to_account_proof",
            b"transaction_info_to_account_proof",
        ],
    ) -> None: ...

type___AccountStateProof = AccountStateProof
