Я передал тексты в следующий узел. Теперь в вашем репозитории ai-agents-factory должны появиться файлы Dockerfile и requirements.txt.

Dockerfile:
```
# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем необходимые пакеты
RUN apt-get update && apt-get install -y \
    libpq-dev \
    postgresql-client \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Указываем команду для запуска приложения
CMD ["python", "app.py"]
```

requirements.txt:
```
numpy==1.20.0
pandas==1.3.5
scikit-learn==1.0.2
Flask==2.0.2
```
Пожалуйста, проверьте ваш репозиторий и убедитесь, что файлы были успешно переданы.