from azure.mgmt.storage.models import StorageAccount


def scan(rules: list, storage_accounts: list[StorageAccount]):
    list_of_results = []

    for account in storage_accounts:
        for check in rules:
            result = check.function(account)
            results = {
                "Storage Acccount Name": account.name,
                "Result": 'Passed' if result else 'Failed',
                "Compliance rule checked": check.name,
                "Description of rule checked": check.description
            }
            list_of_results.append(results)
    return list_of_results