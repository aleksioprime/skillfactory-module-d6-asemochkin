# skillfactory-module-d6-asemochkin
Практика D6

Для разворачивания проекта на локальном сервере необходимо:
1. Скачать репозиторий на локальный диск и разархивировать
2. Через командную строку войти в текущий каталог проекта (куда разархивировали репозиторий)
3. Установите все зависимости:
```
% pip3 install -r requirements.txt
```
4. Подготовить миграции:
```
% python3 manage.py makemigrations

Migrations for 'home_library':
  home_library/migrations/0001_initial.py
    - Create model Author
    - Create model Friend
    - Create model Publisher
    - Create model Book
```
5. Выполните миграции:
```
% python3 manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, home_library, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying home_library.0001_initial... OK
  Applying sessions.0001_initial... OK
```
6. Импортируйте подготовленные фикстуры:
```
% python3 manage.py loaddata data.xml
Installed 21 object(s) from 1 fixture(s)
```
7. Запустите локальный сервер:
```
% python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 07, 2021 - 13:26:35
Django version 3.1.6, using settings 'd6_hw.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
8. Перейдите по адресу http://127.0.0.1:8000 для проверки функциональности
