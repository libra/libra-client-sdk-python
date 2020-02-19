# pyre-strict

import typing

class EventHandle:
    @property
    def count(self) -> int: ...
    @property
    def key(self) -> bytes: ...

class AccountResource:
    @staticmethod
    def create(addr_bytes: bytes, lcs_bytes: bytes) -> AccountResource: ...
    @property
    def address(self) -> bytes: ...
    @property
    def balance(self) -> int: ...
    @property
    def sequence(self) -> int: ...
    @property
    def authentication_key(self) -> bytes: ...
    @property
    def delegated_key_rotation_capability(self) -> bool: ...
    @property
    def delegated_withdrawal_capability(self) -> bool: ...
    @property
    def sent_events(self) -> EventHandle: ...
    @property
    def received_events(self) -> EventHandle: ...

class TransactionUtils:
    @staticmethod
    def createSignedP2PTransaction(
        sender_private_key: bytes,
        receiver: bytes,
        sender_sequence: int,
        num_coins_microlibra: int,
        *ignore: typing.Any,
        expiration_time: int,
        max_gas_amount: int = 140000,
        gas_unit_price: int = 0
    ) -> BytesWrapper: ...
    @staticmethod
    def parse(version: int, lcs_bytes: bytes, gas: int) -> SignedTransaction: ...

class BytesWrapper:
    @property
    def byte(self) -> bytes: ...
    @property
    def hex(self) -> str: ...

class AccountKey:
    def __init__(self, private_key_bytes: bytes) -> None: ...
    @property
    def address(self) -> bytes: ...
    @property
    def public_key(self) -> bytes: ...
    @property
    def private_key(self) -> bytes: ...

class Transaction:
    @property
    def sender(self) -> bytes: ...
    @property
    def sequence(self) -> int: ...
    @property
    def sender(self) -> bytes: ...
    @property
    def sequence(self) -> int: ...
    @property
    def max_gas_amount(self) -> int: ...
    @property
    def gas_unit_price(self) -> int: ...
    @property
    def expiration_time(self) -> int: ...
    @property
    def is_p2p(self) -> bool: ...
    @property
    def is_mint(self) -> bool: ...
    @property
    def receiver(self) -> bytes: ...
    @property
    def amount(self) -> int: ...

class SignedTransaction(Transaction):
    @property
    def public_key(self) -> bytes: ...
    @property
    def signature(self) -> bytes: ...
    @property
    def version(self) -> int: ...
    @property
    def gas(self) -> int: ...

class Event:
    @property
    def module(self) -> str: ...
    @property
    def name(self) -> str: ...

class PaymentEvent(Event):
    @property
    def is_sent(self) -> bool: ...
    @property
    def is_received(self) -> bool: ...
    @property
    def sender_address(self) -> bytes: ...
    @property
    def receiver_address(self) -> bytes: ...
    @property
    def amount(self) -> int: ...
    @property
    def metadata(self) -> bytes: ...

class EventFactory:
    @staticmethod
    def parse(
        key: bytes, sequence_number: int, event_data: bytes, type_tag: bytes
    ) -> typing.Union[Event, PaymentEvent]: ...
