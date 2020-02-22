import os
import boto3

from datetime import datetime


dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    table_name = 'tasks'
    table = dynamodb.Table(table_name)

    the_big_wad = table.scan()
    get_user = the_big_wad['Items'][0]

    # get_user = table.get_item({'id': user_id})

    string_format = "%m/%d/%Y, %H:%M:%S"
    now = datetime.now()

    for user in the_big_wad['Items']:
        last_done = datetime.strptime(user['lastDone'], string_format)
        delta = now - last_done
        print(delta.days)
        if delta.days > 1:
            key = {'id': user['id']}
            table.update_item(Key=key,
                              UpdateExpression="SET streakLength = :updated",
                              ExpressionAttributeValues={':updated': 0}
                              )

    response = {
        'statusCode': 200,
        'body': '[memento voice]: I did it'
    }

    return response
