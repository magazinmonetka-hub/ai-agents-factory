Добавим необходимые эндпоинты и обновим файлы, используя библиотеку FastAPI.

**context_cleaning.py**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

class RequestData(BaseModel):
    data: dict

def clean_context(data: dict) -> dict:
    # Здесь должна быть ваша логика очистки контекста
    # Для примера просто удалим лишние ключи
    cleaned_data = {key: value for key, value in data.items() if key != 'unnecessary_key'}
    return cleaned_data

@app.post("/execute")
async def execute(request_data: RequestData):
    try:
        cleaned_data = clean_context(request_data.data)
        return {"result": cleaned_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

**json_validation.py**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
import json

app = FastAPI()

class RequestData(BaseModel):
    data: dict

def validate_json(data: dict) -> bool:
    try:
        # Здесь должна быть ваша логика валидации JSON
        # Для примера просто проверим, что JSON не пустой
        if not data:
            return False
        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/validate")
async def validate(request_data: RequestData):
    try:
        is_valid = validate_json(request_data.data)
        return {"is_valid": is_valid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

**main.py**
```python
from fastapi import FastAPI
from context_cleaning import app as cleaning_app
from json_validation import app as validation_app

app = FastAPI()

@app.get("/status")
async def get_status():
    return {"status": "OK"}

app.mount("/cleaning", cleaning_app)
app.mount("/validation", validation_app)
```

**Dockerfile**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**requirements.txt**
```
fastapi
uvicorn
pydantic
```

Теперь вы можете запустить приложение в Docker, используя команду:
```bash
docker build -t my-fastapi-app .
docker run -p 8000:8000 my-fastapi-app
```
И доступ к эндпоинтам:
- `http://localhost:8000/cleaning/execute` - для очистки контекста
- `http://localhost:8000/validation/validate` - для валидации JSON
- `http://localhost:8000/status` - для проверки работоспособности приложения