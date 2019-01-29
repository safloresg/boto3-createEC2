import boto3
import argparse
import yaml
import logging
import botocore
import json

from utils import get_yaml,get_log_level


LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(funcName) '
                            '-35s %(lineno) -5d: %(message)s')

LOGGER = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-r','--region', type=str, required=False,help='AWS Region in which the ec2 instance is being created (default: us-east-1)',default='us-east-1')
    parser.add_argument('-i','--instance-type', type=str, required=False,help='Instance type.(default: t2.micro)',default='t2.micro')
    parser.add_argument('-p','--pem-name', type=str, required=True,help='The key pair to be used for the instance.')
    parser.add_argument('-l','--log-level', type=str, required=False,help='DEBUG, INFO, WARNING, CRITICAL',default='INFO')    

    args = parser.parse_args()

    client = boto3.client('cloudformation',region_name=args.region)

    fileData = get_yaml('templates/ec2Template.yml')

    logging.basicConfig(level=get_log_level(args.log_level), format=LOG_FORMAT)

    try:
        response = client.create_stack(
            StackName='my-stack',
            TemplateBody= yaml.dump(fileData),
            Parameters=[
                {
                    'ParameterKey': 'KeyName',
                    'ParameterValue': args.pem_name
                },
                {
                    'ParameterKey': 'InstanceType',
                    'ParameterValue': args.instance_type
                }
            ],
            TimeoutInMinutes=3,
            OnFailure='ROLLBACK')

        if 'ResponseMetadata' in response and response['ResponseMetadata']['HTTPStatusCode'] < 300:
            logging.info("succeed. response: {0}".format(json.dumps(response)))
        else:
            logging.critical("There was an Unexpected error. response: {0}".format(json.dumps(response)))
            
    except botocore.exceptions.ClientError as e:
        logging.critical("Boto error caught: {0}".format(e))
        
                                
if __name__ == '__main__':
        main()
