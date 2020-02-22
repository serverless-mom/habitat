import os
import boto3

from datetime import datetime


dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    table_name = 'tasks'
    table = dynamodb.Table(table_name)

    the_big_wad = table.scan()

    string_format = "%m/%d/%Y, %H:%M:%S"
    now = datetime.now()
    resetCount = 0

    for user in the_big_wad['Items']:
        last_done = datetime.strptime(user['lastDone'], string_format)
        delta = now - last_done
        print(delta.days)
        if delta.days > 1:
            resetCount += 1
            key = {'id': user['id']}
            table.update_item(Key=key,
                              UpdateExpression="SET streakLength = :updated",
                              ExpressionAttributeValues={':updated': 0}
                              )

    response = {
        'statusCode': 200,
        'body': 'users reset: '+str(resetCount)
    }

    return response
