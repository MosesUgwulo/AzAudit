from rules import make_check

class TestStorageAccount:
    enable_https_traffic_only: bool = True
    minimum_tls_version: str = "TLS1_2"

storage_account = TestStorageAccount()

def test_make_check_enable_https_traffic_only_pass():
    https_check = make_check("enable_https_traffic_only", True)
    assert https_check(storage_account)

def test_make_check_enable_https_traffic_only_fail():
    https_check = make_check("enable_https_traffic_only", False)
    assert not https_check(storage_account)

def test_minimum_tls_version_pass():
    tls_check = make_check("minimum_tls_version", "TLS1_2")
    assert tls_check(storage_account)

def test_minimum_tls_version_fail():
    tls_check = make_check("minimum_tls_version", "TLS1_0")
    assert not tls_check(storage_account)