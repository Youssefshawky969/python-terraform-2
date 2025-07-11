"""
tf_generator.py

Generates Terraform configuration (.tf) files based on AWS resource data.
"""

import os
from typing import List, Dict, Any

def generate_vpc_tf(vpcs: List[Dict[str, Any]], filename: str = "vpcs.tf", region: str = "us-east-1") -> None:
    """
    Generate Terraform configuration for the provided VPCs.

    Args:
        vpcs (List[Dict[str, Any]]): A list of VPC objects returned from Boto3.
        filename (str): The file path to write the Terraform config to.
        region (str): The AWS region for the provider block in Terraform.

    Returns:
        None
    """
    terraform_content = f'''provider "aws" {{
  region = "{region}"
}}\n\n'''

    for idx, vpc in enumerate(vpcs):
        cidr_block = vpc.get("CidrBlock", "0.0.0.0/0")
        tags = vpc.get("Tags", [])
        name_tag = next((tag["Value"] for tag in tags if tag["Key"] == "Name"), f"VPC_{idx + 1}")

        terraform_content += f'''
resource "aws_vpc" "vpc_{idx + 1}" {{
  cidr_block = "{cidr_block}"
  tags = {{
    Name = "{name_tag}"
  }}
}}
'''

    # Ensure output directory exists
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as tf_file:
        tf_file.write(terraform_content)

    print(f"Terraform file generated at: {filename}")
