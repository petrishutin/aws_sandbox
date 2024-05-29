from tests.test_hello import HelloLambdaTestCase


class TestSuccess(HelloLambdaTestCase):

    def test_success(self):
        result = {
            "statusCode": 200,
            "message": "Hello from Lambda"
        }
        self.assertEqual(self.HANDLER.handle_request(dict(), dict()), result)
