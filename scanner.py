from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccount
from dotenv import find_dotenv, load_dotenv
import os

# Compliance checks
def check_https(account: StorageAccount):
    return account.enable_https_traffic_only

def check_tls(account: StorageAccount):
    return account.minimum_tls_version == "TLS1_2"


checks = [check_https, check_tls]


if __name__ == "__main__":
    dovenv_path = find_dotenv()
    load_dotenv(dovenv_path)

    SUBSCRIPTION_ID = os.getenv("SUBSCRIPTION_ID")

    client = StorageManagementClient(credential=DefaultAzureCredential(), subscription_id=SUBSCRIPTION_ID)

    for account in client.storage_accounts.list():
        for check in checks:
            result = check(account)
            print(f"{account.name} - {'Passed' if result else 'Failed'} - {check.__name__}")