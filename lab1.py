import boto3
from botocore.endpoint import Endpoint
ec2 = boto3.client('ec2')
response = ec2.describe_regions()


print('---------------------------------------------------')
print ('ENDPOINT','\t''\t''\t''\t', 'REGION-NAME')
print('---------------------------------------------------')


for p_id, p_info in response.items():
    for i in p_info: 
       print(i['Endpoint'], '\t''\t',i[ 'RegionName'])
    break








