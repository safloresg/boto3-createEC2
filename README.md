# Boto3-createEC2

Tool for creating simple EC2 instances in AWS Amazon by using CloudFormation.   

The instance created includes cowsay (https://www.npmjs.com/package/cowsay).

## Usage - Create EC2


```
python create-ec2.py -h
usage: create-ec2.py [-h] [-r REGION] [-i INSTANCE_TYPE] -p PEM_NAME

optional arguments:
  -h, --help            show this help message and exit
  -r REGION, --region REGION
                        AWS Region in which the ec2 instance is being created
                        (default: us-east-1)
  -i INSTANCE_TYPE, --instance-type INSTANCE_TYPE
                        Instance type.(default: t2.micro)
  -p PEM_NAME, --pem-name PEM_NAME
                        The key pair to be used for the instance.

```


