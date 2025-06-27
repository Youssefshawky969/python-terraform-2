from typing import List, Dict
import boto3

def list_vpcs(region: str) -> List[Dict]:
    """
    List all VPCs in the specified AWS region.

    Args:
        region (str): AWS region (e.g., 'us-east-1').

    Returns:
        List[Dict[str, Any]]: A list of VPC objects from Boto3.
    """
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_vpcs()
    return response.get("Vpcs", [])

def list_ec2_instances(region: str) -> List[Dict]:
    """
    List all EC2 instances in the specified AWS region.

    Args:
        region (str): AWS region (e.g., 'us-east-1').

    Returns:
        List[Dict[str, Any]]: A list of EC2 instance details.
    """
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        instances.extend(reservation['Instances'])
    return instances