import requests
from graphql import GraphQLError


def request_coin_data():
    """
    Makes an GET request to retrieve the current prices of bitcoin
    :return: The current bitcoin rate in USD
    """

    response = requests.get(
        'https://api.coindesk.com/v1/bpi/currentprice.json')

    if response.status_code == 404:
        raise GraphQLError('Exchange rate data is unavailable')

    rate_float = response.json()['bpi']['USD']['rate_float']
    return rate_float
