import boto3
import argparse
import yaml
import logging


LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(funcName) '
                            '-35s %(lineno) -5d: %(message)s')

LOGGER = logging.getLogger(__name__)

def get_yaml(path):
    with open(path, 'r') as stream:
        try:
            fileData = yaml.load(stream)
            return fileData
        except yaml.YAMLError as exc:
            print(exc)
            return None


def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-r','--region', type=str, required=False,help='AWS Region in which the ec2 instance is being created',default='us-east-1')
    parser.add_argument('-i','--instance-type', type=str, required=False,help='Instance type of the ec2 instance.',default='t2.micro')
    parser.add_argument('-p','--pem-name', type=str, required=True,help='the key name to be used')

    args = parser.parse_args()

    client = boto3.client('cloudformation',region_name=args.region)

    fileData = get_yaml('templates/ec2Template.yml')
    
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
        TimeoutInMinutes=15,
        OnFailure='ROLLBACK')
    
if __name__ == '__main__':
        main()
