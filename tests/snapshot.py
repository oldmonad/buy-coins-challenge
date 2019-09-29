calculate_price_fixture = '''
    query {{
    calculatePrice(
    choiceType: {choice_type}, margin: {margin}, exchangeRate: {exchange_rate}
    )
    {{
     calculatedPrice
}}
}}
'''
