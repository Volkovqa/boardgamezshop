# Boardgamezshop

# Описание
Мой проект по разработке онлайн-магазина с применением фреймворка Django.

На сайте настроена аутентификация - функции системы CRUD для товаров недоступны для неавторизорванных пользователей.

# Инструкция по запуску

## Виртуальное окружение
В проекте используется пакетный менеджер pip. 
Чтобы установить зависимости, нужно запустить виртуальное окружение и установить все установленные пакеты:
`$ pip install -r requirements.txt`


## База данных
Необходимо выбрать базу данных и создать БД для работы проекта

## Переменные окружения
Необходимо создать файл .env, из которого будут тянуться данные для работы с БД, Django и почтой для рассылки.
Файл должен содержать значения для ключей:
- SECRET_KEY - значение вашего ключа будет в config/settings.py после установки Django в виртуальное окружение
- ENGINE - указание БД, с которой будет работать проект
- NAME - название БД для проекта
- HOST - указание хоста для работы с БД
- USER - имя пользователя для работы с БД
- PASSWORD - пароль пользователя для работы с БД
- PORT - указание порта для работы с БД
- EMAIL_HOST_PASSWORD - пароль для почты, осуществляющей рассылку писем (остальные параметры для почты прописаны в config/settings.py)
- CACHE_ENABLED - рычаг для активации работы кэша (True/False)
- CACHE_LOCATION - модуль и адрес для работы с кэшем

## Примененить миграции
Для корректной работы моделей и взаимодействия с БД нужно сделать миграции: 
`$ python3 manage.py makemigrations`
`$ python3 manage.py migrate`

## Регистрация
Если все прудыдущие шаги выполнены верно и настройка прошла успешно, необходимо зарегистрировать пользователя (если надо - superuser).
Т.к. работа с пользователями была переопределена, для создания superuser необходимо:
- в файле users/management/commands/create_custom_superuser.py прописать необходимые e-mail, атрибуты, пароль
- выполнить команду: `python3 manage.py create_custom_superuser`

Если хотите пройти стандартный процесс регистрации, можно зарегистрироваться через интерфейс проекта в браузере - тогда нужно будет подтвердить e-mail - 
вам на почту будет выслано письмо со ссылкой-подтверждением.

# Стек
- Бэкенд - Python 3.10, Django 4.2.3, Pillow 10.0.0, psycopg2-binary 2.9.6, python-dotenv 1.0.0, 
- Фронт - HTML, Bootstrap 5.3.0

# Дополнительно
При разворачивании проекта в новой среде с новой БД, при запуске в браузере не будет информации о продуктах и записях в блоге
(также о юзерах, но об этом выше).
В корне проекта в папке fix_data находятся фикстуры, загрузка которых даст продукты и записи в блоге для отображения в браузере.
Команда для загрузки данных из фикстур: `python3 manage.py fill_db`
Если нужно переопределить команду, она находится в catalog/management/commands/fill_db.py
