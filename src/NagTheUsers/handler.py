import os
import boto3
import json
from datetime import datetime


dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')


def lambda_handler(event, context):
    table_name = 'tasks'
    table = dynamodb.Table(table_name)

    the_big_wad = table.scan()

    string_format = "%m/%d/%Y, %H:%M:%S"
    now = datetime.now()
    nagCount = 0

    for user in the_big_wad['Items']:
        last_done = datetime.strptime(user['lastDone'], string_format)
        delta = now - last_done
        print(delta.days)
        if delta.days > 1:
            nagCount += 1
            message = "get back on Habit@ you jerk! your streak is in danger!"
            response = sns.publish(
                TargetArn='arn:aws:sns:us-east-1:524823921797:habitat-email:f1ecb6be-a8b1-4c17-a8db-02ae6aa2f07e',
                Message=json.dumps({'default': json.dumps(message)}),
                MessageStructure='json'
            )

    response = {
        'statusCode': 200,
        'body': 'number of users nagged: '+str(nagCount)
    }

    return response
