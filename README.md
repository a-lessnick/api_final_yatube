# API для Yatube.
## Описание
Финальная версия API для проекта Yatube, позволяет зарегистрированным пользователям
вести блог, создавая в нем посты.
Зарегистрированные пользователи могут комментировать посты.
Реализован функционал подписки на блоги.

### Технологии:
<ul>
    <li>Python</li>
    <li>Django</li>
    <li>DRF</li>
    <li>JWT</li>
</ul>

## Установка и запуск проекта.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/a-lessnick/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd yatube_api
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов к API.

### Получение списка всех постов. Доступно без авторизации.
   `GET http://127.0.0.1:8000/api/v1/posts/`
* Пример ответа:
   ```json
    {
       "count": 1,
       "next": null,
       "previous": null,
       "results": [
           {
               "id": 1,
               "author": "newuser1",
               "text": "Текст поста.",
               "pub_date": "2024-08-12T23:55:01.961065Z",
               "image": null,
               "group": null
           }
       ]
    }
   ```
### Добавление поста. Авторизация по токену.
   `POST http://127.0.0.1:8000/api/v1/posts/`
   ```json
    {
      "text": "string",
      "image": "string",
      "group": 0
    }
   ```
* Пример ответа:
   ```json
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2024-08-14T23:55:11Z",
      "image": "string",
      "group": 0
    }
   ```

## Статичная документация API.

```
http://127.0.0.1:8000/redoc/
```

## Автор.

Андрей Старостин.




