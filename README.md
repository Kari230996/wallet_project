# 💸 Wallet Project

A web application for managing virtual wallets: creating, depositing, withdrawing funds, and checking balances. Implemented in Django with a REST API and a UI interface.

## 🚀 Features

* ✅ Create a new wallet
* 💰 Deposit or withdraw funds
* 📊 View current balance by UUID
* 🌐 API documentation (Swagger, ReDoc)
* 🧪 Test coverage using `pytest`
* 🐳 Docker and docker-compose support
* 🎨 UI built with Django templates and Bootstrap 5

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Kari230996/wallet_project.git
cd wallet_project
```

### 2. Run with Docker

1. Before starting, rename `.env.example` to `.env`
2. Open `.env` and replace `SECRET_KEY` with your own:

```bash
SECRET_KEY=django-insecure-replace-with-unique-key
```

3. Generate a new key (Windows example):

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

4. Start the project:

```bash
docker-compose up --build
```

### 3. Apply migrations inside the container

```bash
docker-compose exec web python manage.py migrate
```

### 4. Create a superuser

```bash
docker-compose exec web python manage.py createsuperuser
```

---

## 📘 API Documentation

* Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
* ReDoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

⚠️ All API endpoints are prefixed with `/api/v1/`.
Example request: `POST http://localhost:8000/api/v1/wallets/`

---

## 🧪 Testing

```bash
docker-compose exec web pytest
```

| Test                                                | What it checks                                |
| --------------------------------------------------- | --------------------------------------------- |
| `test_wallet_create`                                | Wallet creation, UUID format, initial balance |
| `test_wallet_balance_success`                       | Get balance of existing wallet                |
| `test_wallet_balance_not_found`                     | Response for non-existent UUID                |
| `test_wallet_operation_deposit`                     | Successful deposit                            |
| `test_wallet_operation_withdraw_success`            | Successful withdrawal                         |
| `test_wallet_operation_withdraw_insufficient_funds` | Error when withdrawing more than available    |

---

## 🖥️ UI Interface

Main UI page: [http://localhost:8000/wallets-ui/](http://localhost:8000/wallets-ui/)

---

## 📁 Project Structure

```
wallet_project/
├── wallets/            # Core API app
├── wallet_ui/          # UI app with templates
├── config/             # Django settings
├── templates/          # HTML templates
├── tests/              # Pytest tests
├── docker-compose.yml
...
```

---

## 🛠️ Technologies Used

* Python 3.11
* Django 5.x
* Django REST Framework
* PostgreSQL
* Bootstrap 5
* Docker, docker-compose
* Pytest + pytest-django
* drf-yasg (Swagger)

---

## 📩 Contact

**Developer:** [karina.apaeva96@gmail.com](mailto:karina.apaeva96@gmail.com)
