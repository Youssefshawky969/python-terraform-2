# AWS Boto3 to Terraform CLI Tool

A simple Python CLI tool that uses **Boto3** to fetch AWS VPC and EC2 instance details and automatically generates equivalent **Terraform** `.tf` configuration files.

---

##  Features

-  Fetches VPCs and EC2 instances using AWS Boto3
-  Generates Terraform config with provider and resource blocks
-  Outputs clean, ready-to-apply `.tf` files
-  Modular Python structure with type hints and docstrings
-  MkDocs-powered developer documentation

---

##  Requirements

- Python 3.8+
- AWS credentials configured (via `~/.aws/credentials` or env vars)
- Install dependencies:

```bash
pip install boto3 mkdocs mkdocs-material mkdocstrings[python]

##  How to use?

1. Run this tool

```bash
python main.py

2. Enter your desired AWS region ```(e.g. us-east-1)``` 

3. This tool will:
     .   List your VPCs and EC2s
     .   Generate ``` .tf ``` file under ``` terraform_output/


Example Output:



## Project Structure:
```bash
aws_boto3_to_terraform/
├── main.py                      # CLI entry point
├── utils/
│   ├── aws_fetch.py            # AWS Boto3 logic
│   └── tf_generator.py         # Terraform file generation
├── terraform_output/            # Generated .tf files
├── docs/                        # MkDocs documentation
├── mkdocs.yml                   # Docs site configuration
└── README.md



## To view the full developer documenation:

```bash 

python mkdocs serve


then visit: http://127.0.0.1:8000

Example Output  Terraform:




