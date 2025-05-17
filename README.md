# 💸 Wallet Project

Веб-приложение для управления виртуальными кошельками: создание, пополнение, снятие средств и просмотр баланса. Реализовано на Django с REST API и UI-интерфейсом.

## 🚀 Возможности

- ✅ Создание нового кошелька
- 💰 Пополнение или снятие средств
- 📊 Просмотр текущего баланса по UUID
- 🌐 API-документация (Swagger, ReDoc)
- 🧪 Покрытие тестами с использованием `pytest`
- 🐳 Поддержка Docker и docker-compose
- 🎨 UI на Django-шаблонах с Bootstrap 5

## 🔧 Установка

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/Kari230996/wallet_project.git
cd wallet_project
```

### 2. Запуск через Docker
1. Перед запуском переименуйте вручную файл `.env.example` на `.env`
2. Затем откройте `.env` и замените SECRET_KEY на любой другой:
```bash
SECRET_KEY=django-insecure-замените-на-уникальный-ключ
```
3. Сгенерировать новый ключ можно командой на Windows:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

```
4. Запускайте проект командой:
```bash
docker-compose up --build
```

### 3. Применение миграции внутри контейнера
```bash
docker-compose exec web python manage.py migrate
```

### 4. Создание суперпользователя
```bash
docker-compose exec web python manage.py createsuperuser
```

## 📘 Документация API

- Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- ReDoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

⚠️ Все эндпоинты API начинаются с префикса `/api/v1/`.  
Пример запроса: `POST http://localhost:8000/api/v1/wallets/`

## 🧪 Тестирование

```bash
docker-compose exec web pytest
```
| Тест                                                | Что проверяет                                  |
| --------------------------------------------------- | ---------------------------------------------- |
| `test_wallet_create`                                | Создание кошелька, формат UUID и баланс = 0.00 |
| `test_wallet_balance_success`                       | Получение баланса существующего кошелька       |
| `test_wallet_balance_not_found`                     | Ответ при несуществующем UUID                  |
| `test_wallet_operation_deposit`                     | Успешное пополнение                            |
| `test_wallet_operation_withdraw_success`            | Успешное снятие средств                        |
| `test_wallet_operation_withdraw_insufficient_funds` | Ошибка при попытке снять больше, чем есть      |



## 🖥️ Интерфейс

Главная страница UI: [http://localhost:8000/wallets-ui/](http://localhost:8000/wallets-ui/)

## 📁 Структура проекта

```
wallet_project/
├── wallets/            # Основное API-приложение
├── wallet_ui/          # UI-приложение с шаблонами
├── config/             # Настройки Django
├── templates/          # HTML-шаблоны
├── tests/              # Pytest тесты
├── docker-compose.yml
...
```

## 🛠️ Используемые технологии

- Python 3.11
- Django 5.x
- Django REST Framework
- PostgreSQL
- Bootstrap 5
- Docker, docker-compose
- Pytest + pytest-django
- drf-yasg (Swagger)

## 📩 Контакты

**Разработчик:** karina.apaeva96@gmail.com









