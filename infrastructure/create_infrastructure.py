import boto3

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

# Create VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc.create_tags(Tags=[{"Key": "Name", "Value": "my-vpc"}])
vpc.wait_until_available()

# Create Subnets
subnet = vpc.create_subnet(CidrBlock='10.0.1.0/24')
subnet.create_tags(Tags=[{"Key": "Name", "Value": "my-subnet"}])

# Create Security Groups
security_group = ec2.create_security_group(
    GroupName='my-security-group', 
    Description='Security group for my app', 
    VpcId=vpc.id
)
security_group.authorize_ingress(
    CidrIp='0.0.0.0/0',
    IpProtocol='tcp',
    FromPort=80,
    ToPort=80
)

# Create Launch Configuration
launch_config = client.create_launch_configuration(
    LaunchConfigurationName='my-launch-config',
    ImageId='ami-0c55b159cbfafe1f0',
    InstanceType='t2.micro',
    SecurityGroups=[security_group.id],
    UserData='''
    #!/bin/bash
    docker run -d -p 80:80 my-backend-image
    '''
)

# Create Auto Scaling Group
asg = client.create_auto_scaling_group(
    AutoScalingGroupName='my-asg',
    LaunchConfigurationName='my-launch-config',
    MinSize=1,
    MaxSize=3,
    DesiredCapacity=2,
    VPCZoneIdentifier=subnet.id
)
