from azure.mgmt.storage.models import StorageAccount

def scan(rules: list, storage_accounts: list[StorageAccount]):
    for account in storage_accounts:
        for check in rules:
            result = check.function(account)
            print(f"{account.name} - {'Passed' if result else 'Failed'} - {check.name} - {check.description}")