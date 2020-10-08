from rest_framework import serializers

from ..models import AuthenticationKey, DatadogAlert


class AuthenticationKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthenticationKey
        # fields = ["name", "key", "key_type"]
        fields = "__all__"


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatadogAlert
        fields = "__all__"

