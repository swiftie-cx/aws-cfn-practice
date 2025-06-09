def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': f'You said: {event.get("body", "")}'
    }
