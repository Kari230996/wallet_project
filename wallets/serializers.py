from rest_framework import serializers

from .models import Wallet


class WalletCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("uuid", "balance")
        read_only_fields = ["uuid", "balance"]


class OperationSerializer(serializers.Serializer):
    operation_type = serializers.ChoiceField(choices=["DEPOSIT", "WITHDRAW"])
    amount = serializers.DecimalField(
        max_digits=12, decimal_places=2, min_value=0.01)
