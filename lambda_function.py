import json
import boto3
s3=boto3.client('s3')
dynamodb=boto3.resource('dynamodb')


def lambda_handler(event, context):
    bucket_name=event["Records"][0]["s3"]["bucket"]["name"]
    object_name=event["Records"][0]["s3"]["object"]["key"]
    
    json_object = s3.get_object(Bucket=bucket_name,Key=object_name)
    json_file=json_object['Body'].read()
    jsondic= json.loads(json_file)
    
    table = dynamodb.Table('employees')
    table.put_item(Item=jsondic)
