from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    auth_token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "auth_token"]

    @transaction.atomic
    def create(self, validated_data):
        try:
            user = User.objects.get(username=validated_data.get("email"))
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=validated_data.get("email"),
                email=validated_data.get("email"),
                first_name=validated_data.get("first_name"),
                last_name=validated_data.get("last_name"),
            )
        if not hasattr(user, "auth_token"):
            Token.objects.get_or_create(user=user)
        return user
