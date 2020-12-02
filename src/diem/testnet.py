# Copyright (c) The Diem Core Contributors
# SPDX-License-Identifier: Apache-2.0

"""Provides utilities for working with Diem Testnet.

```python

from diem import testnet, LocalAccount

# create client connects to testnet
client = testnet.create_client()

# create faucet for minting coins for your testing account
faucet = testnet.Faucet(client)

# create a local account and mint some coins for it
account: LocalAccount = faucet.gen_account()

```

"""

import requests
import typing

from . import diem_types, jsonrpc, utils, local_account, serde_types, auth_key, chain_ids, lcs


JSON_RPC_URL: str = "https://testnet.diem.com/v1"
FAUCET_URL: str = "https://testnet.diem.com/mint"
CHAIN_ID: diem_types.ChainId = chain_ids.TESTNET

DESIGNATED_DEALER_ADDRESS: diem_types.AccountAddress = utils.account_address("000000000000000000000000000000dd")
TEST_CURRENCY_CODE: str = "Coin1"


def create_client() -> jsonrpc.Client:
    """create a jsonrpc.Client connects to Testnet public full node cluster"""

    return jsonrpc.Client(JSON_RPC_URL)


class Faucet:
    """Faucet service is a proxy server to mint coins for your test account on Testnet

    See https://github.com/libra/libra/blob/master/json-rpc/docs/service_testnet_faucet.md for more details
    """

    def __init__(
        self,
        client: jsonrpc.Client,
        url: typing.Union[str, None] = None,
        retry: typing.Union[jsonrpc.Retry, None] = None,
    ) -> None:
        self._client: jsonrpc.Client = client
        self._url: str = url or FAUCET_URL
        self._retry: jsonrpc.Retry = retry or jsonrpc.Retry(5, 0.2, Exception)
        self._session: requests.Session = requests.Session()

    def gen_account(self, currency_code: str = TEST_CURRENCY_CODE) -> local_account.LocalAccount:
        account = local_account.LocalAccount.generate()
        self.mint(account.auth_key.hex(), 5_000_000_000, currency_code)
        return account

    def mint(self, authkey: str, amount: int, currency_code: str) -> None:
        self._retry.execute(lambda: self._mint_without_retry(authkey, amount, currency_code))

    def _mint_without_retry(self, authkey: str, amount: int, currency_code: str) -> None:
        response = self._session.post(
            FAUCET_URL,
            params={
                "amount": amount,
                "auth_key": authkey,
                "currency_code": currency_code,
                "return_txns": "true",
            },
        )
        response.raise_for_status()

        de = lcs.LcsDeserializer(bytes.fromhex(response.text))
        length = de.deserialize_len()

        for i in range(length):
            txn = de.deserialize_any(diem_types.SignedTransaction)
            self._client.wait_for_transaction(txn)
