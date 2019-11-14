/* automatically generated by rust-bindgen */

#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct CEventHandle {
    pub count: u64,
    pub key: [u8; 32usize],
}
#[test]
fn bindgen_test_layout_CEventHandle() {
    assert_eq!(
        ::std::mem::size_of::<CEventHandle>(),
        40usize,
        concat!("Size of: ", stringify!(CEventHandle))
    );
    assert_eq!(
        ::std::mem::align_of::<CEventHandle>(),
        8usize,
        concat!("Alignment of ", stringify!(CEventHandle))
    );
    assert_eq!(
        unsafe { &(*(::std::ptr::null::<CEventHandle>())).count as *const _ as usize },
        0usize,
        concat!(
            "Offset of field: ",
            stringify!(CEventHandle),
            "::",
            stringify!(count)
        )
    );
    assert_eq!(
        unsafe { &(*(::std::ptr::null::<CEventHandle>())).key as *const _ as usize },
        8usize,
        concat!(
            "Offset of field: ",
            stringify!(CEventHandle),
            "::",
            stringify!(key)
        )
    );
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct CDevAccountResource {
    pub balance: u64,
    pub sequence: u64,
    pub authentication_key: *mut u8,
    pub delegated_key_rotation_capability: bool,
    pub delegated_withdrawal_capability: bool,
    pub sent_events: CEventHandle,
    pub received_events: CEventHandle,
}
#[test]
fn bindgen_test_layout_CDevAccountResource() {
    assert_eq!(
        ::std::mem::size_of::<CDevAccountResource>(),
        112usize,
        concat!("Size of: ", stringify!(CDevAccountResource))
    );
    assert_eq!(
        ::std::mem::align_of::<CDevAccountResource>(),
        8usize,
        concat!("Alignment of ", stringify!(CDevAccountResource))
    );
    assert_eq!(
        unsafe { &(*(::std::ptr::null::<CDevAccountResource>())).balance as *const _ as usize },
        0usize,
        concat!(
            "Offset of field: ",
            stringify!(CDevAccountResource),
            "::",
            stringify!(balance)
        )
    );
    assert_eq!(
        unsafe { &(*(::std::ptr::null::<CDevAccountResource>())).sequence as *const _ as usize },
        8usize,
        concat!(
            "Offset of field: ",
            stringify!(CDevAccountResource),
            "::",
            stringify!(sequence)
        )
    );
    assert_eq!(
        unsafe {
            &(*(::std::ptr::null::<CDevAccountResource>())).authentication_key as *const _ as usize
        },
        16usize,
        concat!(
            "Offset of field: ",
            stringify!(CDevAccountResource),
            "::",
            stringify!(authentication_key)
        )
    );
    assert_eq!(
        unsafe {
            &(*(::std::ptr::null::<CDevAccountResource>())).delegated_key_rotation_capability
                as *const _ as usize
        },
        24usize,
        concat!(
            "Offset of field: ",
            stringify!(CDevAccountResource),
            "::",
            stringify!(delegated_key_rotation_capability)
        )
    );
    assert_eq!(
        unsafe {
            &(*(::std::ptr::null::<CDevAccountResource>())).delegated_withdrawal_capability
                as *const _ as usize
        },
        25usize,
        concat!(
            "Offset of field: ",
            stringify!(CDevAccountResource),
            "::",
            stringify!(delegated_withdrawal_capability)
        )
    );
    assert_eq!(
        unsafe { &(*(::std::ptr::null::<CDevAccountResource>())).sent_events as *const _ as usize },
        32usize,
        concat!(
            "Offset of field: ",
            stringify!(CDevAccountResource),
            "::",
            stringify!(sent_events)
        )
    );
    assert_eq!(
        unsafe {
            &(*(::std::ptr::null::<CDevAccountResource>())).received_events as *const _ as usize
        },
        72usize,
        concat!(
            "Offset of field: ",
            stringify!(CDevAccountResource),
            "::",
            stringify!(received_events)
        )
    );
}