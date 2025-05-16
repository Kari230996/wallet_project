from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from uuid import UUID

from .models import Wallet
from .serializers import OperationSerializer, WalletCreateSerializer


class WalletCreateView(APIView):
    @swagger_auto_schema(
        tags=["Кошельки"],
        operation_summary="Создать новый кошелёк",
        responses={
            201: openapi.Response(
                description="Кошелёк успешно создан",
                examples={
                    "application/json": {
                        "uuid": "ea9993d0-6a92-4e03-bd5e-b160cb8a3d88",
                        "balance": "0.00"
                    }
                }
            )
        }
    )
    def post(self, request):
        wallet = Wallet.objects.create()
        serializer = WalletCreateSerializer(wallet)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WalletBalanceView(APIView):
    @swagger_auto_schema(
        tags=["Кошельки"],
        operation_summary="Получение баланса кошелька",
        operation_description="Получить баланс кошелька по UUID",
        responses={
            200: openapi.Response(
                description="Успешный ответ. Баланс кошелька.",
                examples={
                    "application/json": {
                        "description": "Данные кошелька успешно получены",
                        "data": {
                            "uuid": "8d82b593-9715-436e-8db5-47878302893b",
                            "balance": "1500.00"
                        }
                    }
                }
            ),
            404: openapi.Response(
                description="Кошелёк не найден.",
                examples={
                    "application/json": {
                        "description": "Кошелёк с таким UUID не найден",
                        "data": None
                    }
                }
            ),
            400: openapi.Response(
                description="Некорректный UUID.",
                examples={
                    "application/json": {
                        "description": "Некорректный UUID",
                        "data": None
                    }
                }
            ),
        },

    )
    def get(self, request, wallet_uuid):
        try:
            UUID(wallet_uuid, version=4)
        except ValueError:
            return Response({
                "description": "Некорректный UUID.",
                "data": None
            }, status=status.HTTP_400_BAD_REQUEST)

        wallet = Wallet.objects.filter(uuid=wallet_uuid).first()
        if not wallet:
            return Response({
                "description": "Кошелёк с таким UUID не найден.",
                "data": None
            }, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "description": "Данные кошелька успешно получены.",
            "data": {
                "uuid": str(wallet.uuid),
                "balance": str(wallet.balance)
            }
        }, status=status.HTTP_200_OK)


class WalletOperationView(APIView):
    @swagger_auto_schema(
        tags=["Кошельки"],
        operation_summary=(
            "Выполнить операцию с кошельком "
            "(пополнение или снятие)"
        ),
        operation_description=(
            "Передайте UUID кошелька и данные операции. "
            "Возможные типы: DEPOSIT, WITHDRAW."
        ),
        request_body=OperationSerializer,
        responses={
            200: openapi.Response(
                description="Операция успешно выполнена",
                examples={
                    "application/json": {
                        "description": "Операция прошла успешно",
                        "data": {
                            "uuid": "ea9993d0-6a92-4e03-bd5e-b160cb8a3d88",
                            "balance": "150.00"
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="Ошибка: недостаточно средств",
                examples={
                    "application/json": {
                        "description": "Недостаточно средств",
                        "error": "Insufficient funds"
                    }
                }
            )
        }
    )
    def post(self, request, wallet_uuid):
        try:
            UUID(wallet_uuid, version=4)
        except ValueError:
            return Response({
                "description": "Некорректный UUID кошелька"
            }, status=400)

        serializer = OperationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        wallet = get_object_or_404(Wallet, uuid=wallet_uuid)

        with transaction.atomic():
            wallet.refresh_from_db()

            if data["operation_type"] == "DEPOSIT":
                wallet.balance += data["amount"]
            elif data["operation_type"] == "WITHDRAW":
                if wallet.balance < data["amount"]:
                    return Response({
                        "description": "Недостаточно средств",
                        "error": "Insufficient funds"
                    }, status=400)
                wallet.balance -= data["amount"]

            wallet.save()

        return Response({
            "description": "Операция прошла успешно",
            "data": {
                "uuid": str(wallet.uuid),
                "balance": str(wallet.balance)
            }
        }, status=200)
