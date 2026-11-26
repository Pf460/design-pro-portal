## Проект design-pro-portal

---

### Инструкция по запуску

1. Клонирование репозитория
````bash
git clone https://github.com/Pf460/design-pro-portal.git
````

2. Создание виртуального окружения
````bash
python -m venv .venv

Активации в соответсвии с вашей ОС

Linux/macOS
source .venv/bin/activate

Windows
.venv\Scripts\Activate
````

3. Установка зависимостей
````bash
pip install -r requirements.txt
````

4. Создание .env файла
````bash
cp .env.example .env
````

4. Миграции
````bash
python manage.py makemigrations
python manage.py migrate
````

5. Создание суперпользователя
````bash
python manage.py createsuperuser
````

6. Запуск сервера
````bash
python manage.py runserver
````

----

### Доступные url-aдреса

- Главная страница: http://localhost:8089/
- Стандартная админка: http://localhost:8089/admin
- Своя админская панель: http://localhost:8089/superadmin
- Api: http://localhost:8089/api/snippets/

----