# AzAudit

A Python CLI tool that scans Azure resources against configurable YAML-based compliance rules and generates audit reports.

## What It Does

AzAudit connects to your Azure subscription, retrieves resource configurations, and evaluates them against a set of compliance rules you define in YAML. Results are printed to the console and exported as a CSV report. Currently supports storage account checks with more resource types planned.

## Prerequisites

- Python 3.10+
- An Azure account with at least one subscription
- Azure CLI installed and authenticated (`az login`)
- Terraform (optional, for provisioning test resources)

## Setup

Clone the repo and create a virtual environment:

```bash
git clone https://github.com/your-username/AzAudit.git
cd AzAudit
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Run a compliance scan by providing your Azure subscription ID:

```bash
python cli.py --subscription-id <your-subscription-id>
```

To specify a custom report filename:

```bash
python cli.py --subscription-id <your-subscription-id> --filename my_report.csv
```

If no filename is provided, results are saved to `report.csv` by default.

## Adding Compliance Rules

Rules are defined in `Rules/storage.yaml`. To add a new check, add an entry to the file:

```yaml
  - name: Your Check Name
    description: What this check verifies
    property: azure_property_name
    expected: expected_value
```

No Python code changes required. AzAudit reads the YAML at runtime and builds checks dynamically.

## Running Tests

```bash
pytest
```

Tests verify that the compliance check logic works correctly using mock objects — no Azure connection needed.

## Test Infrastructure

The project includes a Terraform configuration (`terraform/main.tf`) that provisions test storage accounts in Azure — one compliant and one non-compliant — so you can verify AzAudit detects both passing and failing checks.

```bash
terraform init
terraform apply
```

To tear everything down when you're done:

```bash
terraform destroy
```

Requires Terraform installed and Azure CLI authenticated.

## Docker

Docker is useful if you don't want to manage a Python environment locally, or if you're running AzAudit in a CI pipeline or on a server.

Build the image:

```bash
docker build -t azaudit .
```

Run with a service principal (no interactive `az login` needed):

```bash
docker run \
  -e AZURE_CLIENT_ID=<your-client-id> \
  -e AZURE_CLIENT_SECRET=<your-client-secret> \
  -e AZURE_TENANT_ID=<your-tenant-id> \
  -v ./reports:/usr/src/app/reports \
  azaudit --subscription-id <your-subscription-id>
```

The `-v` flag mounts a local `reports/` directory so the CSV output is saved to your machine.

## CI/CD

The project includes a GitHub Actions workflow that runs on every push. It runs the test suite first, and only builds the Docker image if all tests pass.