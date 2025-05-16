import requests
import json
from django.shortcuts import render


def home(request):
    return render(request, "wallet_ui/home.html")


def create_wallet(request):
    if request.method == "POST":
        response = requests.post("http://localhost:8000/api/v1/wallets/")
        if response.status_code == 201:
            data = response.json()
            return render(request, "wallet_ui/wallet_created.html",
                          {"wallet": data})
        return render(request, "wallet_ui/create_wallet.html",
                      {"error": "Ошибка при создании кошелька"})

    return render(request, "wallet_ui/create_wallet.html")


def check_balance(request):
    uuid = request.GET.get("uuid")
    balance_data = None
    balance_error = None

    if uuid:
        url = f"http://localhost:8000/api/v1/wallets/{uuid}/"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                balance_data = response.json()["data"]
            else:
                balance_error = response.json().get(
                    "description",
                    "Ошибка получения баланса."
                )
        except Exception:
            balance_error = "Ошибка соединения с API."

    return render(request, "wallet_ui/home.html", {
        "balance_data": balance_data,
        "balance_error": balance_error
    })


def wallet_operation(request):
    context = {}

    if request.method == "POST":
        uuid = request.POST.get("uuid")
        operation_type = request.POST.get("operation_type")
        amount = request.POST.get("amount")

        try:
            amount = float(amount)
        except (ValueError, TypeError):
            context["operation_error"] = "Сумма должна быть числом"
            return render(request, "wallet_ui/home.html", context)

        url = f"http://localhost:8000/api/v1/wallets/{uuid}/operation/"
        payload = {
            "operation_type": operation_type,
            "amount": amount
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json()
        except json.JSONDecodeError:
            context["operation_error"] = "Сервер вернул невалидный JSON"
            return render(request, "wallet_ui/home.html", context)
        except requests.RequestException:
            context["operation_error"] = "Ошибка соединения с сервером"
            return render(request, "wallet_ui/home.html", context)

        if response.status_code == 200:
            context["operation_success"] = True
            context["operation_data"] = data["data"]
        else:
            context["operation_error"] = data.get(
                "description", "Произошла ошибка")

    return render(request, "wallet_ui/home.html", context)
