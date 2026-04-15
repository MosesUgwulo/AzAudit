from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from dotenv import find_dotenv, load_dotenv
import os

dovenv_path = find_dotenv()
load_dotenv(dovenv_path)

SUBSCRIPTION_ID = os.getenv("SUBSCRIPTION_ID")

client = StorageManagementClient(credential=DefaultAzureCredential(), subscription_id=SUBSCRIPTION_ID)

for account in client.storage_accounts.list():
    print(account.name)