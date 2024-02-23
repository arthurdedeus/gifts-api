from rest_framework import serializers

from gifts.models import Gift


class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ("id", "name", "description", "price", "amount", "image")
