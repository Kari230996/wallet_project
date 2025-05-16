from django.urls import path

from .views import (
    WalletCreateView,
    WalletBalanceView,
    WalletOperationView,
)

urlpatterns = [
    path("api/v1/wallets/", WalletCreateView.as_view()),
    path("api/v1/wallets/<str:wallet_uuid>/", WalletBalanceView.as_view()),
    path("api/v1/wallets/<str:wallet_uuid>/operation/",
         WalletOperationView.as_view()),
]
