import os
import boto3

aws_lambda = boto3.client(
    'lambda',
    region_name='us-west-2',
    AWS_ACCESS_KEY_ID=os.environ.get('AWS_ACCESS_KEY_ID'),
    AWS_SECRET_ACCESS_KEY=os.environ.get('AWS_SECRET_ACCESS_KEY')
)


s3 = boto3.resource(
    's3',
    region_name='us-west-2'
)

dependency_bucket = s3.Bucket("pi-requirements")