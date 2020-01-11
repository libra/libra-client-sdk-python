// Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::data::{LibraAccountKey, LibraStatus};
use libra_crypto::ed25519::*;
use libra_types::account_address::{AccountAddress, ADDRESS_LENGTH};
use std::{convert::TryFrom, slice};

#[no_mangle]
pub unsafe extern "C" fn libra_LibraAccount_from(
    private_key_bytes: *const u8,
    out: *mut LibraAccountKey,
) -> LibraStatus {
    let private_key_buf: &[u8] =
        slice::from_raw_parts(private_key_bytes, ED25519_PRIVATE_KEY_LENGTH);

    let private_key = match Ed25519PrivateKey::try_from(private_key_buf) {
        Ok(result) => result,
        Err(_e) => {
            return LibraStatus::InvalidArgument;
        }
    };
    let public_key: Ed25519PublicKey = (&private_key).into();
    let address = AccountAddress::from_public_key(&public_key);

    let mut address_bytes = [0u8; ADDRESS_LENGTH];
    address_bytes.copy_from_slice(address.as_ref());

    *out = LibraAccountKey {
        address: address_bytes,
        private_key: private_key.to_bytes(),
        public_key: public_key.to_bytes(),
    };

    LibraStatus::OK
}

pub extern "C" fn LibraAccount_from(
    private_key_buf: &[u8],
) -> Result<LibraAccountKey, LibraStatus> {
    let private_key = match Ed25519PrivateKey::try_from(private_key_buf) {
        Ok(result) => result,
        Err(_e) => {
            return Err(LibraStatus::InvalidArgument);
        }
    };
    let public_key: Ed25519PublicKey = (&private_key).into();
    let address = AccountAddress::from_public_key(&public_key);

    let mut address_bytes = [0u8; ADDRESS_LENGTH];
    address_bytes.copy_from_slice(address.as_ref());

    Ok(LibraAccountKey {
        address: address_bytes,
        private_key: private_key.to_bytes(),
        public_key: public_key.to_bytes(),
    })
}

/// Generate a private key, then get LibraAccount
#[test]
fn test_libra_account_from() {
    use libra_crypto::test_utils::TEST_SEED;
    use rand::{rngs::StdRng, SeedableRng};

    // generate key pair
    let mut rng = StdRng::from_seed(TEST_SEED);
    let key_pair = compat::generate_keypair(&mut rng);
    let private_key = key_pair.0;

    let mut libra_account = LibraAccountKey::default();
    let result =
        unsafe { libra_LibraAccount_from(private_key.to_bytes().as_ptr(), &mut libra_account) };
    assert_eq!(result, LibraStatus::OK);

    let public_key = key_pair.1;
    let address = AccountAddress::from_public_key(&public_key);

    assert_eq!(libra_account.public_key, public_key.to_bytes());
    assert_eq!(libra_account.private_key, private_key.to_bytes());
    assert_eq!(AccountAddress::new(libra_account.address), address);
}
