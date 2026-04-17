"""
Compliance rules for Azure storage account checks

To add a new check:
    1. Write a function that takes a StorageAccount and returns a bool
    2. Create a StorageAccountCompliance instance
    3. Add it to the checks list
"""

from azure.mgmt.storage.models import StorageAccount
from dataclasses import dataclass
from typing import Callable

@dataclass
class StorageAccountCompliance:
    name: str
    description: str
    function: Callable[[StorageAccount], bool]

# Compliance checks
def check_https(account: StorageAccount):
    return account.enable_https_traffic_only

def check_tls(account: StorageAccount):
    return account.minimum_tls_version == "TLS1_2"

https_check_rule = StorageAccountCompliance(
    "Check HTTPS",
    "Checking to see if HTTPS is enabled on the storage account",
    check_https
)

tls_check_rule = StorageAccountCompliance(
    "Check TLS Version",
    "Checks the TLS version and making sure it matches TLS1_2",
    check_tls
)


checks = [https_check_rule, tls_check_rule]
