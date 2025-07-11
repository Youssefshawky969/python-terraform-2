# AWS Boto3 to Terraform CLI Tool

Welcome to the documentation site for the AWS Boto3 to Terraform CLI.

#### This tool lets you:
  -  Discover AWS VPCs and EC2 instances
  -  Generate Terraform `.tf` files from live AWS environments
  -  Easily reverse-engineer infrastructure into code

## Features

- AWS region selection
- VPC and EC2 discovery
- Terraform config generation
- Modular Python structure
- Auto-generated documentation using MkDocs

 ### Quick Link

- [Getting Started](getting-started.md)
- [Usage Guide](usage.md)
- [API Reference](api/aws_fetch.md)

## Quick Start

`
python main.py
`

Enter your AWS `region`, and the tool will generate `terraform_output/vpcs.tf`.


