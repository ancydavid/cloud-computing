import boto3
ec2 = boto3.resource('ec2')

outfile = open('ancy0.pem','w')

key_pair = ec2.create_key_pair(KeyName='ancy0')
KeyPairOut = str(key_pair.key_material)
print(KeyPairOut)
outfile.write(KeyPairOut)