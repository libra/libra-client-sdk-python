# Copyright (c) The Libra Core Contributors
# SPDX-License-Identifier: Apache-2.0

from . import (
    libra_types,
    utils,
)

from .auth_key import AuthKey
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey


class LocalAccount:
    """LocalAccount is like a wallet account

    This is handy class for creating tests for your application, but may not ideal for production code.
    """

    @staticmethod
    def generate() -> "LocalAccount":
        """Generate a random private key and initialize local account"""

        private_key = Ed25519PrivateKey.generate()
        return LocalAccount(private_key)

    private_key: Ed25519PrivateKey

    def __init__(self, private_key: Ed25519PrivateKey) -> None:
        self.private_key = private_key

    @property
    def auth_key(self) -> AuthKey:
        return AuthKey.from_public_key(self.public_key)

    @property
    def account_address(self) -> libra_types.AccountAddress:
        return self.auth_key.account_address()

    @property
    def public_key_bytes(self) -> bytes:
        return utils.public_key_bytes(self.public_key)

    @property
    def public_key(self) -> Ed25519PublicKey:
        return self.private_key.public_key()

    def sign(self, txn: libra_types.RawTransaction) -> libra_types.SignedTransaction:
        """Create signed transaction for given raw transaction"""

        signature = self.private_key.sign(utils.raw_transaction_signing_msg(txn))
        return utils.create_signed_transaction(txn, self.public_key_bytes, signature)
