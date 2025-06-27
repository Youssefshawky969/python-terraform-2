# AWS Boto3 to Terraform CLI Tool

This CLI tool uses Boto3 to fetch AWS resources (VPCs, EC2) and generates Terraform `.tf` configuration files.

## Features

- AWS region selection
- VPC and EC2 discovery
- Terraform config generation
- Modular Python structure
- Auto-generated documentation using MkDocs

## How to Use

```bash
python main.py
```
::: utils.aws_fetch

::: utils.tf_generator