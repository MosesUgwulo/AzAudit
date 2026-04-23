from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from typing import Annotated
from rules import checks
from scanner import scan
from report import generate_report
import typer

app = typer.Typer()

@app.command()
def check_compliance(
    subscription_id: Annotated[str, typer.Option(help="Your subscription ID on your Azure account")],
    filename: Annotated[str, typer.Option(help="File name for the report")] = "report.csv"
    ):
    client = StorageManagementClient(credential=DefaultAzureCredential(), subscription_id=subscription_id)
    list_of_results = scan(checks, client.storage_accounts.list())
    generate_report(list_of_results, filename)
    print(list_of_results)

if __name__ == "__main__":
    app()