import os
import boto3

from datetime import datetime


dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):
    table_name = 'tasks'
    table = dynamodb.Table(table_name)

    user_id = '8476'

    the_big_wad = table.scan()
    get_user = the_big_wad['Items'][0]
    print(get_user)

    # get_user = table.get_item({'id': user_id})

    string_format = "%m/%d/%Y, %H:%M:%S"
    now = datetime.now()
    last_done = now.strftime(string_format)

    streak = get_user['streakLength']
    streak += 1

    key = {'id': user_id}
    
    table.update_item(Key=key,
                        UpdateExpression="SET lastDone = :updated",                   
                        ExpressionAttributeValues={':updated': last_done}
                        ) 
    table.update_item(Key=key,
                        UpdateExpression="SET streakLength = :updated",                   
                        ExpressionAttributeValues={':updated': streak}
                        ) 
    response = {
        'statusCode': 200,
        'body': streak
    }
    return response

