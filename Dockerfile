# Используем официальный Python-образ
FROM python:3.11

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем все файлы проекта
COPY . .

# Команда по умолчанию
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
