import pytest
from rest_framework.test import APIClient
from uuid import UUID


@pytest.mark.django_db
class TestWalletAPI:
    def setup_method(self):
        self.client = APIClient()

    def test_wallet_create(self):
        response = self.client.post("/api/v1/wallets/")
        assert response.status_code == 201
        data = response.json()
        assert "uuid" in data
        assert "balance" in data
        assert data["balance"] == "0.00"
        UUID(data["uuid"])

    def test_wallet_balance_success(self):
        create_response = self.client.post("/api/v1/wallets/")
        wallet_uuid = create_response.json()["uuid"]

        response = self.client.get(f"/api/v1/wallets/{wallet_uuid}/")
        assert response.status_code == 200
        body = response.json()
        assert body["description"] == "Данные кошелька успешно получены."
        assert body["data"]["uuid"] == wallet_uuid
        assert body["data"]["balance"] == "0.00"

    def test_wallet_balance_not_found(self):
        response = self.client.get(
            "/api/v1/wallets/00000000-0000-0000-0000-000000000000/")
        assert response.status_code == 404
        assert response.json()[
            "description"] == "Кошелёк с таким UUID не найден."

    def test_wallet_operation_deposit(self):
        create_response = self.client.post("/api/v1/wallets/")
        wallet_uuid = create_response.json()["uuid"]

        response = self.client.post(
            f"/api/v1/wallets/{wallet_uuid}/operation/",
            {"operation_type": "DEPOSIT", "amount": "100.00"},
            format="json"
        )
        assert response.status_code == 200
        assert response.json()["data"]["balance"] == "100.00"

    def test_wallet_operation_withdraw_success(self):
        create_response = self.client.post("/api/v1/wallets/")
        wallet_uuid = create_response.json()["uuid"]

        self.client.post(
            f"/api/v1/wallets/{wallet_uuid}/operation/",
            {"operation_type": "DEPOSIT", "amount": "100.00"},
            format="json"
        )

        response = self.client.post(
            f"/api/v1/wallets/{wallet_uuid}/operation/",
            {"operation_type": "WITHDRAW", "amount": "40.00"},
            format="json"
        )
        assert response.status_code == 200
        assert response.json()["data"]["balance"] == "60.00"

    def test_wallet_operation_withdraw_insufficient_funds(self):
        create_response = self.client.post("/api/v1/wallets/")
        wallet_uuid = create_response.json()["uuid"]

        response = self.client.post(
            f"/api/v1/wallets/{wallet_uuid}/operation/",
            {"operation_type": "WITHDRAW", "amount": "999.99"},
            format="json"
        )
        assert response.status_code == 400
        assert response.json()["description"] == "Недостаточно средств"
        assert response.json()["error"] == "Insufficient funds"
