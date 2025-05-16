Применение миграции внутри контейнера

```bash
docker-compose exec web python manage.py migrate
```
Для создания суперпользователя для входа в /admin/:
```bash
docker-compose exec web python manage.py createsuperuser
```

