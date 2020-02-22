import os
import boto3

dynamodb = boto3.resource('dynamodb')

def handler(event, context):
  table_name = os.environ['TABLE_NAME'] # get the table name from the automatically populated environment variables
  table = dynamodb.Table(table_name)

  # How to convert datetime object to string for database. Can specify any format. 
  # string_format = "%m/%d/%Y, %H:%M:%S"
  # date = now.strftime(string_format)
  # date_string = '12/24/2018, 04:59:31'

  # How to convert string back to datetime object for manipulation. Must use the same format. 
  # strptime(date_string, string_format)

  params = {
    'id': '8476', # we only have one user for development
    'lastDone': '02/21/2020, 10:38:00', # a random time from yesterday "%m/%d/%Y, %H:%M:%S"
    'streakLength': '32' # random number for development
  }

  # Write a new item to the Items table
  item_id = params.get('id')
  print(f'Adding item {item_id} to table {table_name}')
  table.put_item(Item = params, ConditionExpression='attribute_not_exists(id)') # do not overwrite existing entries
  print('Item added to table, done')

  # Return a 200 response if no errors
  response = {
    'statusCode': 200,
    'body': 'Success!'
  }

  return response