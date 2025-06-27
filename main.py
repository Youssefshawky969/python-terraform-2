from utils.aws_fetch import list_vpcs, list_ec2_instances
from utils.tf_generator import generate_vpc_tf

def main():
    """
    Main entry point to the CLI tool.
    Prompts user for AWS region, lists VPCs/EC2s,
    and generates a Terraform file from fetched data.
    """
    region = input("Enter AWS region (e.g. us-east-1): ").strip()
    
    # List VPCs
    vpcs = list_vpcs(region)
    print(f"Found {len(vpcs)} VPCs.")

    # List EC2s (optional)
    ec2s = list_ec2_instances(region)
    print(f"Found {len(ec2s)} EC2 instances.")

    # Generate Terraform file
    generate_vpc_tf(vpcs)
    print("Terraform file 'vpcs.tf' has been generated.")

if __name__ == "__main__":
    main()
