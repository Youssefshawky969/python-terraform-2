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
```
- Clone the repository:
  ```
  git clone https://github.com/Youssefshawky969/python-terraform-2.git
  cd python-terraform-2/
  ```

## Project Structure:
```
python-terraform-2/
├── main.py                     # CLI entry point
├── utils/
│   ├── aws_fetch.py            # AWS Boto3 logic
│   └── tf_generator.py         # Terraform file generation
├── vpcs.tf                     # Generated .tf files
├── docs/                       # MkDocs documentation
├── mkdocs.yml                  # Docs site configuration
└── README.md

```

##  How to use?

1. Run this tool

```bash
python main.py
```
2. Enter your desired AWS region ```(e.g. us-east-1)``` 

3. This tool will:
      - List your VPCs and EC2s
      - Generate ``` .tf ``` file under ``` terraform_output/```


## Example Output:

![image](https://github.com/user-attachments/assets/3664f067-b961-4f60-9092-43db93aa424c)




## To view the full developer documenation:

- Run

```
python mkdocs serve
```
then visit:
```
http://127.0.0.1:8000
```
It will appears like this:

![image](https://github.com/user-attachments/assets/510d4412-fe89-4bdf-a7f7-5be6b0dfc0ff)


## Example Output  Terraform:
```
resource "aws_vpc" "vpc_1" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "MyVPC"
  }
}
```

## For Full Documentation:
[Click here to view](https://youssefshawky969.github.io/python-terraform-2/)






