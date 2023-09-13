## Как развернуть проект:

* Установите Docker и Docker-Compose.
* Клонируйте репозиторий командой:
`git clone git@github.com:sntchweb/albums_and_songs.git`
* Создайте в директории /backend/albums_and_songs/ файл `.env` с переменными окружения.
```
ALLOWED_HOSTS='localhost localhost:8000 127.0.0.1 127.0.0.1:8000 backend backend:8000'
DEBUG='True'
SECRET_KEY='django-insecure-l77w_dq*$#)5w*&4@6s3()#+09l^x(_$8&o-hq=g_@$zzh1pq8'
POSTGRES_DB=django
POSTGRES_USER=django
POSTGRES_PASSWORD=django
DB_NAME=django
DB_HOST=postgres_db
DB_PORT=5432
```
* Откройте терминал и запустите сборку docker-контейнеров командой:  
`docker-compose up --build`.  
* Примените миграции:  
`docker compose -f docker-compose.yml exec backend python manage.py migrate`  
* Соберите и скопируйте статику:  
`docker compose -f docker-compose.yml exec backend python manage.py collectstatic`  
`docker compose -f docker-compose.yml exec backend cp -r /app/collected_static/. /static/static/`

API будет доступно по адресу: `http://127.0.0.1/api/`  
Swagger будет доступен по адресу: `http://127.0.0.1/swagger/`

## Стек:
Python 3.9, Django 4.1, PostgreSQL
