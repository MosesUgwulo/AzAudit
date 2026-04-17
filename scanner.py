from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from dotenv import find_dotenv, load_dotenv
from rules import checks
import os


if __name__ == "__main__":
    dovenv_path = find_dotenv()
    load_dotenv(dovenv_path)

    SUBSCRIPTION_ID = os.getenv("SUBSCRIPTION_ID")

    client = StorageManagementClient(credential=DefaultAzureCredential(), subscription_id=SUBSCRIPTION_ID)

    for account in client.storage_accounts.list():
        for check in checks:
            result = check.function(account)
            print(f"{account.name} - {'Passed' if result else 'Failed'} - {check.name} - {check.description}")