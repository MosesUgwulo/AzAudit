"""
Compliance rules for Azure storage account checks

To add a new check:
    1. Add an entry to Rules/storage.yaml
"""

from azure.mgmt.storage.models import StorageAccount
from dataclasses import dataclass
from typing import Callable
import yaml

@dataclass
class StorageAccountCompliance:
    name: str
    description: str
    function: Callable[[StorageAccount], bool]

checks = []

def make_check(property_name: str, expected_value):
    def check(account: StorageAccount):
        return getattr(account, property_name) == expected_value
    return check


try:
    with open('rules/storage.yaml') as stream:
        obj = yaml.safe_load(stream=stream)
        for rule in obj['rules']:
            check = StorageAccountCompliance(
                rule['name'],
                rule['description'],
                make_check(rule['property'], rule['expected'])
            )
            checks.append(check)
            
except FileNotFoundError as err:
    print(err)
except yaml.YAMLError as exc:
    print(exc)