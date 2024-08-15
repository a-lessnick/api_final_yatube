# api_final
Финальная версия API для проекта Yatube.

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

### Получить список всех публикаций.
ENDPOINT:

```
http://127.0.0.1:8000/api/v1/posts/
```

Method: 

```
GET
```

Необязательные параметры.
(При указании параметров limit и offset выдача будет постраничной.)

```
limit - integer, количество публикаций на страницу.
offset - integer, номер страницы после которой начинать выдачу.
```

### Добавить публикацию.
ENDPOINT:

```
http://127.0.0.1:8000/api/v1/posts/
```

Method: 

```
POST
```

Body:

```
text - string, обязательное, текст публикации.
image - string or null <binary>, картинка для публикации.
group - integer or null, id сообщества.
```

## Статичная документация API.

```
http://127.0.0.1:8000/redoc/
```




