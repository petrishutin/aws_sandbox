import json

from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda


_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass

    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        if event['rawPath'] == '/hello' and event['httpMethod'] == 'GET':
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Hello from Lambda"})
            }
        else:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": f"Bad request syntax or unsupported method. Request path: {event['rawPath']}. HTTP method: {event['httpMethod']}"})
            }


HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
