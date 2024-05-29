from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('Hello-handler')


class Hello(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass

    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        return {
            "statusCode": 200,
            "message": "Hello from Lambda"
        }


HANDLER = Hello()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
