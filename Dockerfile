Извините, но как текстовый помощник, я не имею прямого доступа к внешним системам, включая GitHub, и не могу напрямую выполнять действия по обновлению репозитория. Однако, я могу помочь вам сгенерировать необходимые файлы, такие как Dockerfile и requirements.txt, для вашего проекта с FastAPI.

Для начала, вот пример того, как может выглядеть файл `requirements.txt` для проекта с FastAPI:

```
fastapi
uvicorn
```

И вот пример файла Dockerfile для проекта с FastAPI:

```dockerfile
# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл requirements.txt
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения
COPY . .

# Запускаем приложение
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Вам нужно будет заменить `main:app` на фактический путь к вашему FastAPI-приложению.

Чтобы обновить ваш репозиторий на GitHub, вам нужно будет создать эти файлы в вашем локальном репозитории, выполнить `git add .`, затем `git commit -m "Обновление Dockerfile и requirements.txt"`, и, наконец, `git push origin ваша_ветка`.