import json


def handler(event, context):
    usuario = event['pathParameters']['usuario'];
    
    body = {
        "message": "O usuario enviado foi: " + str(usuario)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
