#Проект YaMDb
##Описание:
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles).
##Установка:
Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone 
```
Запустить docker-compose:
```
docker-compose up -d
```
Выполнить миграции:
```
docker-compose exec web python manage.py migrate
```
Проект доступен по адресу :
```
http://localhost/
```
шаблон .env
```
DB_ENGINE=
DB_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=
DB_HOST=
DB_PORT=
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=
```
##Примеры запросов к API:
Endpoint:
```
api/v1/posts/{id}/
```
GET запрос:
```
api/v1/posts/1/
```
Ответ:
```
[
    {
      "id": 1,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
]
```
Endpoint:
```
api/v1/posts/{post_id}/comments/
```
POST запрос:
```
{
"text": "string"
}
```
Ответ:
```
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
```

### Технологии
Python 3.7
Django 2.2.19
Docker
nginx:1.21.3 

### Авторы
Святослав


![This is an image](https://github.com/Sviatoslavvvik/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

В сети:
51.250.101.206