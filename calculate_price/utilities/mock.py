mock_response = {
    'time': {
        'updated': 'Sep 28, 2019 18:01:00 UTC',
        'updatedISO': '2019-09-28T18:01:00+00:00',
        'updateduk': 'Sep 28, 2019 at 19:01 BST'
    },
    'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price \
        Index (USD). Non-USD currency data converted using hourly conversion \
            rate from openexchangerates.org',
    'chartName': 'Bitcoin',
    'bpi': {
        'USD': {
            'code': 'USD',
            'symbol': '&#36;',
            'rate': '8,155.7050',
            'description': 'United States Dollar',
            'rate_float': 8155.705
        },
        'GBP': {
            'code': 'GBP',
            'symbol': '&pound;',
            'rate': '6,636.0525',
            'description': 'British Pound Sterling',
            'rate_float': 6636.0525
        },
        'EUR': {
            'code': 'EUR',
            'symbol': '&euro;',
            'rate': '7,453.9474',
            'description': 'Euro',
            'rate_float': 7453.9474
        }
    }
}


request_sell_mock = {
    'margin_input': 2,
    'exchange_rate': 360,
    'action_type': 'sell'
}
