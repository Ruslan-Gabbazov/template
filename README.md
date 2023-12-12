# FastAPI + SQLAlchemy MVC template 


## Создание окружения    
Установка poetry и необходимых пакетов:
``` Bash
pip install poetry

cd .\src\
poetry install
```

Установить postgreSQL и pdAdmin, создать БД с параметрами из ```src/core/config.py```   

Применение миграций:
``` Bash
poetry run alembic upgrade head
```

Локальный запуск сервиса:
``` Bash
poetry run py main.py
```
