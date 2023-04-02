### Описание

API для проекта Yatube.

### Локальный запуск:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/chelumbas/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Реализованные API:

Доступный функционал сервиса без УЗ

```
GET api/v1/posts/ - Получить все публикации.
GET api/v1/posts/{id}/ - Получить публикацию по ID
GET api/v1/groups/ - Получить сообщества
GET api/v1/groups/{id}/ - Получить сообщества по ID
GET api/v1/{post_id}/comments/ - Получить комментарии к постам
GET api/v1/{post_id}/comments/{id}/ - Получить комментарий к посту по ID
```