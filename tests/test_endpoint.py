import json
from django.test import TestCase, Client
from tests.snapshot import calculate_price_fixture


class CalculatePriceTest(TestCase):
    """
    Integration test for graphql endpoint
    """

    @classmethod
    def query(cls, query: str = None):
        # Method to run all queries and mutations for tests.
        cls.client = Client()
        body = dict()
        body['query'] = query
        response = cls.client.post(
            '/graphql/', json.dumps(body), content_type='application/json')
        json_response = json.loads(response.content.decode())
        return json_response

    def test_request_to_buy(self):
        """ testing user request to buy"""
        data = {
            'choice_type': 'BUY',
            'margin': 6,
            'exchange_rate': 360
        }
        response = self.query(
            calculate_price_fixture.format(**data))

        self.assertIn('data', response)
        self.assertIn('calculatedPrice', response['data']['calculatePrice'])
        self.assertIsNotNone(response['data']['calculatePrice']['calculatedPrice'])

    def test_request_to_sell(self):
        """ testing user request to sell"""
        data = {
            'choice_type': 'SELL',
            'margin': 7,
            'exchange_rate': 365
        }
        response = self.query(
            calculate_price_fixture.format(**data))
        self.assertIn('data', response)
        self.assertIn('calculatedPrice', response['data']['calculatePrice'])
        self.assertIsNotNone(response['data']['calculatePrice']['calculatedPrice'])
