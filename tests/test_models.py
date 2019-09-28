from django.test import TestCase
from calculate_price.models import Coin


class CoinTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Coin.objects.create(
            code='BDP', country='Great Britain', rate_per_btc=4)
        Coin.objects.create(
            code='USD', country='United States', rate_per_btc=5)

    def test_coin_model(self):
        gb_coin = Coin.objects.get(code='BDP')
        us_coin = Coin.objects.get(code='USD')

        self.assertEqual(
            gb_coin.get_rate(), "The current rate of Great Britain's BTC to BDP is 4")
        self.assertEqual(
            us_coin.get_rate(), "The current rate of United States's BTC to USD is 5")
