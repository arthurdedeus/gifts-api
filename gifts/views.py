from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from gifts.models.checkout import Checkout
from gifts.models.gift import Gift
from gifts.serializers import CheckoutSerializer, GiftSerializer


class GiftViewSet(ModelViewSet):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CheckoutViewSet(ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
