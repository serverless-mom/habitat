import os
import boto3
dynamodb = boto3.resource('dynamodb')
def handler(event, context):
  table_name = os.environ['TABLE_NAME'] # get the table name from the automatically populated environment variables
  table = dynamodb.Table(table_name)

  result = {
    'id': '8476', # we only have one user for development
    'lastDone': '02/21/2020, 10:38:00', # a random time from yesterday
    'streakLength': '32' # random number for development
  }

  # add one to streakLength
  # create new params object that has the new streak length and a date time of right now
  # do this:
    table.update_item(Item = params) # do not overwrite existing entries


#do that:
  response = {
    'statusCode': 200,
    'body': 'this should be a new streak length'
  }

  #done!
  
  return response

