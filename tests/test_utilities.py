from requests.models import Response
import unittest
from unittest import mock
from calculate_price.utilities.request import request_coin_data
from calculate_price.utilities.mock import mock_response
# from calculate_price.utilities.calculate_margin import calculate_margin


def req_res():
    return mock_response


class TestUtilities(unittest.TestCase):

    def test_request_coin_data(self):
        """
        Test for the helper method that extracts the latest
        coin price from the third party API
        """
        with mock.patch('calculate_price.utilities.request.requests.get') as mocked_data:
            api_call = Response()
            api_call.json = req_res
            mocked_data.return_value = api_call
            mocked_response = request_coin_data()
            self.assertEqual(mocked_response, mock_response['bpi']['USD']['rate_float'])

    # def test_calculate_margin(self):
    #     with mock.patch('calculate_price.utilities.request.requests.get') as \
    #          mocked_data:
    #         api_call = Response()
    #         api_call.json = req_res
    #         mocked_data.return_value = api_call
    #         margin = request_sell_mock['margin_input']
    #         exchange_rate = request_sell_mock['exchange_rate']
    #         action_type = request_sell_mock['action_type']
    #         mock_calculation = calculate_margin(margin, exchange_rate, action_type)
