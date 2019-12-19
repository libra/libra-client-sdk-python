from pylibra import TransactionUtils

ADDRESS = bytes.fromhex("fe3e61c509e00e49c018f140c302da2e66be04937a41db1d3ee116cac9646d0f")
RECEIVER_ADDRESS = bytes.fromhex("00" * 32)
PRIVATE_KEY = bytes.fromhex("11" * 32)

SIGNED_TXN_BYTES_HEX = (
    "a07ffc5e1799c00f3ac9fa7bbf1db75a25aaf4d0ac1e104f3f16a5445cd9c571ff"
    "0000000000000002000000b80000004c49425241564d0a010007014a0000000400"
    "0000034e000000060000000d54000000060000000e5a0000000600000005600000"
    "002900000004890000002000000008a90000000f00000000000001000200010300"
    "020002040200030204020300063c53454c463e0c4c696272614163636f756e7404"
    "6d61696e0f7061795f66726f6d5f73656e64657200000000000000000000000000"
    "00000000000000000000000000000000000000000100020004000c000c01130101"
    "020200000001000000000000000000000000000000000000000000000000000000"
    "000000000000000000000000b168de3a00000000e0220200000000000000000000"
    "00000015cd5b070000000020000000d04ab232742bb4ab3a1368bd4615e4e6d022"
    "4ab71a016baf8520a332c97787374000000075d64bdccccf1dc3000220307d07d7"
    "feafc5b01db4ffe2c9fb3870e59cf3bde44d3902a48e7e873b06f095674f9ac3f4"
    "96b749393f942d84e759a7434c0b3506"
)


def test_sign_transcation():
    tx = TransactionUtils.createSignedP2PTransaction(
        PRIVATE_KEY,
        RECEIVER_ADDRESS,
        # sequence
        255,
        # micro libra
        987_654_321,
        expiration_time=123_456_789,
    )

    assert SIGNED_TXN_BYTES_HEX == tx.hex
