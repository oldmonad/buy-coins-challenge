import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from calculate_price.models import Coin
from .utilities.calculate_margin import calculate_margin


# Create a GraphQL type for the actor model
class CoinType(DjangoObjectType):
    class Meta:
        model = Coin


class RequestEnum(graphene.Enum):
    """
        Validate Enum field
    """
    BUY = 'buy'
    SELL = 'sell'


class CalculatePrice(graphene.ObjectType):
    """
        Calculate price objectType that declares
        the Calculate price field
    """
    choice_type = graphene.String()
    margin = graphene.Float()
    exchange_rate = graphene.Float()
    calculated_price = graphene.Float()


class Query(ObjectType):
    coins = graphene.List(CoinType)
    calculate_price = graphene.Field(
        CalculatePrice,
        choice_type=graphene.Argument(RequestEnum, required=True),
        margin=graphene.Float(),
        exchange_rate=graphene.Float()
    )

    def resolve_coins(self, info, **kwargs):
        """
        This methos retrievs all the coins from the database
        """
        return Coin.objects.all()

    def resolve_calculate_price(self, *args, **kwargs):
        """
        This method returns the exchange rate of bitcoin in NGN
        based on user inputs
        :param args: null
        :param kwargs: choice_type, margin, computed_margin
        :return: calculated_price
        """
        choice_type = kwargs.get('choice_type')
        margin = kwargs.get('margin')
        exchange_rate = kwargs.get('exchange_rate')

        if choice_type == 'sell':
            calculated_price = calculate_margin(margin, exchange_rate, 'sell')
        else:
            calculated_price = calculate_margin(margin, exchange_rate, 'buy')

        return CalculatePrice(
            calculated_price=calculated_price
        )
