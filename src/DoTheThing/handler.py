import os
import boto3

from datetime import datetime


dynamodb = boto3.resource('dynamodb')
def handler(event, context):
    table_name = os.environ['TABLE_NAME'] # get the table name from the automatically populated environment variables
    table = dynamodb.Table(table_name)

    user_id = '8476'
    get_user = table.get_item(Key={'id': user_id})

    string_format = "%m/%d/%Y, %H:%M:%S"
    now = datetime.now()
    last_done = now.strftime(string_format)

    streak = get_user['streakLength']
    streak += 1
    
    # result = {
    # 'id': '8476', # we only have one user for development
    # 'lastDone': '02/21/2020, 10:38:00', # a random time from yesterday
    # 'streakLength': '32' # random number for development
    # }

    params = {
        'id': '8476',
        'lastDone': last_done, 
        'streakLength': streak
    }
    
    # add one to streakLength
    # create new params object that has the new streak length and a date time of right now
    # do this:
    table.update_item(Item = params) 

    #do that:
    response = {
        'statusCode': 200,
        'body': streak
    }

    #done!
    
    return response

