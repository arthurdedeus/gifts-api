from urllib.parse import urljoin

from django.db import transaction
from rest_framework import serializers

from gifts.models.checkout import Checkout
from gifts.models.gift import Gift
from settings import settings


class GiftSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Gift
        fields = ("id", "name", "description", "price", "amount", "image")

    @staticmethod
    def get_image(obj):
        bucket_url = urljoin(
            settings.MINIO_PUBLIC_ENDPOINT,
            settings.MINIO_MEDIA_BUCKET_NAME,
        )
        return bucket_url + "/" + obj.image.name


class CheckoutItemInputSerializer(serializers.Serializer):
    gift_id = serializers.IntegerField(write_only=True, required=True)
    quantity = serializers.IntegerField(write_only=True, required=True)


class CheckoutSerializer(serializers.ModelSerializer):
    message = serializers.CharField(write_only=True, required=False)
    items = CheckoutItemInputSerializer(many=True, write_only=True)
    qr_code = serializers.SerializerMethodField(read_only=True)
    br_code = serializers.CharField(read_only=True)

    class Meta:
        model = Checkout
        fields = ("message", "items", "qr_code", "br_code")

    @staticmethod
    def get_qr_code(obj):
        bucket_url = urljoin(
            settings.MINIO_PUBLIC_ENDPOINT,
            settings.MINIO_MEDIA_BUCKET_NAME,
        )
        return bucket_url + "/" + obj.qr_code.name

    @transaction.atomic
    def create(self, validated_data):
        user = self.context["request"].user
        message = validated_data.get("message")

        checkout = Checkout.objects.create(user=user, message=message)
        self._create_checkout_items(checkout)
        checkout.generate_qr_code()

        return checkout

    def _create_checkout_items(self, checkout):
        items = self.validated_data["items"]
        for item in items:
            gift = Gift.objects.get(id=item["gift_id"])
            total = gift.price * item["quantity"]
            checkout.checkout_items.create(
                gift=gift, quantity=item["quantity"], total=total
            )
