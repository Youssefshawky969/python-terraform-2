# Usage Guide

## Running the Tool

```
python main.py
```

You’ll be prompted to enter an AWS region (e.g. `us-east-1`).
The tool will generate a Terraform `.tf ` file in the `terraform_output/` folder.

### Example of the Output:
```
resource "aws_vpc" "vpc_1" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "MyVPC"
  }
}
```
