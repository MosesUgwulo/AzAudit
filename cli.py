from rules import checks
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from scanner import scan
import typer

app = typer.Typer()

@app.command()
def check_compliance(subscription_id: str):
    client = StorageManagementClient(credential=DefaultAzureCredential(), subscription_id=subscription_id)
    scan(checks, client.storage_accounts.list())
    

if __name__ == "__main__":
    app()