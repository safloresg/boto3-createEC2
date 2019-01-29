# Boto3-createEC2

Tool for creating simple EC2 instances in AWS Amazon by using CloudFormation.   

The instance created includes [cowsay](https://www.npmjs.com/package/cowsay).

## Prerequisites

* [Boto 3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation)
* Verify that you have the ~/.aws/config file.
* [Python 3.x](https://www.python.org/downloads/)

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

## Usage example


```
python3 create-ec2.py -p my-pem
INFO       2019-01-29 01:38:48,899 main
50  : succeed. response: {"ResponseMetadata": {"HTTPStatusCode": 200, "RetryAttempts": 0, "RequestId": "ea5dd5c6-2398-11e9-b585-837dd6a4b3c8", "HTTPHeaders": {"content-type": "text/xml", "x-amzn-requestid": "ea5dd5c6-2398-11e9-b585-837dd6a4b3c8", "content-length": "378", "date": "Tue, 29 Jan 2019 07:38:47 GMT"}}, "StackId": "arn:aws:cloudformation:us-east-1:218566243244:stack/my-stack/9c38faf0-2395-11e9-a2f2-12545315cab6"}

```
