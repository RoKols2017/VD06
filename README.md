# Flask Form App 🧾

Расширенная версия веб-приложения на Flask с использованием Flask-WTF для создания и валидации формы анкеты. Поддерживается серверная валидация, CSRF защита и модульная архитектура.

## 🧱 Структура проекта

```
flask_form_app/
├── app/
│   ├── __init__.py         # Инициализация Flask-приложения
│   ├── config.py           # Конфигурация приложения
│   ├── forms.py            # Flask-WTF форма
│   ├── routes/
│   │   └── main.py         # Основные маршруты
│   └── templates/
│       └── index.html      # HTML-шаблон формы
├── run.py                  # Точка входа в приложение
```

## 🚀 Установка и запуск

1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/yourname/flask_form_app.git
   cd flask_form_app
   ```

2. Установить зависимости:
   ```bash
   pip install flask flask-wtf
   ```

3. Запустить сервер:
   ```bash
   python run.py
   ```

4. Перейти в браузере:
   ```
   http://127.0.0.1:5000/
   ```

## 📄 Функциональность

- Анкета пользователя: имя, город, хобби, возраст
- Используется Flask-WTF + WTForms
- CSRF защита автоматически
- Валидация полей:
  - Имя: 2-50 символов
  - Город: макс. 100 символов
  - Хобби: обязательно
  - Возраст: от 0 до 115 лет
- Bootstrap 5 для стилизации

## 🔐 Конфигурация

```python
# app/config.py
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
```

Рекомендуется задать `SECRET_KEY` в переменной окружения при деплое.

## 📦 Возможные улучшения

- Сохранение данных в сессию или базу данных
- Авторизация с Flask-Login
- Подключение REST API через Flask-RESTX
- Вынос формы редактирования в отдельный Blueprint
---

👨‍💻 Автор: RoKols2017  
📅 Версия: 2.0.0  
📬 Лицензия: MIT
