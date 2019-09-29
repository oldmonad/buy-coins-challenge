from .request import request_coin_data
from graphql import GraphQLError


def validate_input(input_number):

    if isinstance(input_number, int) or isinstance(input_number, float):
        return True
    return GraphQLError('Make sure the margin field contains a number')


def calculate_margin(margin_input, exchange_rate, action_type):
    """
        This method calculates the exchange rate of bitcoin in NGN
        based on arguments passed
        :param: margin_input, exchange_rate, action_type
        :return: calculated_price
    """
    current_coin_price = request_coin_data()
    margin_percentage = validate_input(margin_input)/100
    margin_value = current_coin_price * margin_percentage

    if action_type == 'sell':
        computed_price = current_coin_price - margin_value
        return computed_price * exchange_rate

    if action_type == 'buy':
        computed_price = current_coin_price + margin_value
        return computed_price * exchange_rate
