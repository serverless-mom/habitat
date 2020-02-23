from __future__ import print_function
from datetime import datetime
import os
import boto3
import json
import urllib



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
            message = "get back on Habit@ in the next two hours! your "+ str(user['streakLength'])+" day streak is in danger!"
            sns.publish(
                TopicArn='arn:aws:sns:us-east-1:524823921797:habitat-email',
                Subject='Your Streak is in danger!',
                Message=message
            )

    response = {
        'statusCode': 200,
        'body': 'number of users nagged: '+str(nagCount)
    }

    return response



