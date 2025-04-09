# Flask Form App 🧾

Многофайловое Flask-приложение с формой на Bootstrap и архитектурой, приближённой к рекомендованной официальной документацией.

## 🚀 Структура проекта

```
flask_form_app/
├── app/
│   ├── __init__.py         # Инициализация Flask приложения
│   ├── config.py           # Конфигурация (SECRET_KEY и др.)
│   ├── routes/
│   │   └── main.py         # Основные маршруты
│   └── templates/
│       └── index.html      # Шаблон формы
├── run.py                  # Точка входа в приложение
```

## 🔧 Установка и запуск

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/RoKols2017/VD06.git
   cd VD06
   ```

2. Создай и активируй виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Для Windows: venv\Scripts\activate
   ```

3. Установи зависимости:
   ```bash
   pip install flask
   ```

4. Запусти приложение:
   ```bash
   python run.py
   ```

5. Открой в браузере:
   ```
   http://127.0.0.1:5000/
   ```

## 📦 Используемые технологии

- Flask
- Bootstrap 5
- Application Factory Pattern
- Blueprint
- Конфигурация через Config-класс

## ✅ Функциональность

- Отображение формы для ввода имени, города, хобби и возраста
- Отображение введённых данных после отправки
- Простая и расширяемая архитектура проекта

## 🧩 Возможные улучшения

- Валидация через Flask-WTF
- Хранение данных в БД (Flask-SQLAlchemy)
- Авторизация (Flask-Login / Flask-JWT)
- REST API через Flask-RESTX

## 🔒 Конфигурация секретного ключа

```python
# app/config.py
SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
```

Рекомендуется установить переменную окружения перед деплоем:
```bash
export SECRET_KEY='your-production-secret'
```

---

👨‍💻 Автор: RoKols2017  
📅 Версия: 1.0.0  
📬 Лицензия: MIT
