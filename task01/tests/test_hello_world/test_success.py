from task01.tests.test_hello_world import HelloWorldLambdaTestCase


class TestSuccess(HelloWorldLambdaTestCase):

    def test_success(self):
        result = {
            "statusCode": 200,
            "message": "Hello from Lambda"
        }
        self.assertEqual(self.HANDLER.handle_request(dict(), dict()), result)

