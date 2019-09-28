import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from calculate_price.models import Coin


# Create a GraphQL type for the actor model
class CoinType(DjangoObjectType):
    class Meta:
        model = Coin


class Query(ObjectType):
    coins = graphene.List(CoinType)

    def resolve_coins(self, info, **kwargs):
        return Coin.objects.all()
