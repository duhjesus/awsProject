import json
import datetime


def handler(event, context):
    print("TEST TEST")
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps("test test\n\n\n\n"+data),
            'headers': {'Content-Type': 'application/json'}}
