import datetime

def lambda_handler(event, context):
    now = datetime.datetime.now().isoformat()
    return {
        'statusCode': 200,
        'body': f'Now is: {now}'
    }
