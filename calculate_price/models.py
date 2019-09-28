from django.db import models


class Coin(models.Model):
    code = models.CharField(max_length=100)
    rate_per_btc = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.code

    def get_rate(self):
        return f"The current rate of {self.country}'s BTC to {self.code} is {self.rate_per_btc}"

    def __repr__(self):
        return self.code + ' is added.'

    class Meta:
        ordering = ('code',)
