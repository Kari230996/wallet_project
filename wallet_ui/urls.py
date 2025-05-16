from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="wallet_home"),
    path("create/", views.create_wallet, name="create_wallet"),
    path("check/", views.check_balance, name="check_balance"),
    path("operation/", views.wallet_operation, name="wallet_operation"),

]
