from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from gifts.models import Gift
from gifts.serializers import GiftSerializer


class GiftViewSet(ModelViewSet):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
