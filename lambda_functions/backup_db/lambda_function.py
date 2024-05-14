import boto3
import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    dynamodb = boto3.client('dynamodb')
    backup_name = f"backup-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
    response = dynamodb.create_backup(
        TableName='YourDynamoDBTable',
        BackupName=backup_name
    )
    backup_arn = response['BackupDetails']['BackupArn']
    s3.put_object(Bucket='my-s3-bucket', Key=f'backups/{backup_name}.json', Body=backup_arn)
    return {
        'statusCode': 200,
        'body': f'Backup {backup_name} created and stored in S3'
    }
