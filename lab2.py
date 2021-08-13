import os
import boto3
def create_instance():
    ec2_client = boto3.client("ec2", region_name="ap-southeast-2")
    instances = ec2_client.run_instances(
        ImageId="ami-d38a4ab1",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="ancy0"
    )
    instance_id=instances["Instances"][0]["InstanceId"]
    print(instances["Instances"][0]["InstanceId"])
    return instance_id

def get_public_ip(instance_id):
    ec2_client = boto3.client("ec2", region_name="ap-southeast-2")
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get("PublicIpAddress"))


instance_id=create_instance()
get_public_ip(instance_id)