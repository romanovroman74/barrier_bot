Barrier Bot

Это телеграм-бот, позволяющий зарегистрированным пользователям по команде открывать шлагбаум (или выполнять другой запрограммированный вызов).

Оглавление

Особенности и функциональность

Требования

Установка и настройка

Структура проекта

Использование

Дополнительно

Особенности и функциональность

Регистрация пользователяПри запуске бота (/start) проверяется, есть ли пользователь в базе данных.Если пользователя нет, бот запрашивает номер телефона и сохраняет данные в базе (MySQL).

Открытие шлагбаумаЗарегистрированный пользователь может отправить команду /open, после чего вызывается функция, совершающая звонок или отправляющая сигнал на указанный в config номер (config.barrier_phone).

Работа с базой данныхИспользуется модуль mysql_handler для взаимодействия с MySQL (проверка и добавление пользователей).

Обработка ошибокПри проблемах с подключением к базе или другими неполадками бот отправит пользователю сообщение об ошибке.

Требования

Python 3.6+ (рекомендуется последняя стабильная версия Python 3)

Установленные библиотеки (PyTelegramBotAPI и др.)

Настроенная база данных MySQL (или совместимая)

Токен телеграм-бота (от BotFather)

Корректный номер / способ вызова barrier_phone (в config.py), который используется для фактического открытия шлагбаума

Установка и настройка

Клонировать репозиторий (или скачать и распаковать):

git clone https://github.com/your_username/barrier_bot.git
cd barrier_bot

Создать виртуальное окружение (рекомендуется):

python -m venv venv
source venv/bin/activate        # для Linux/macOS
venv\Scripts\activate           # для Windows

Установить зависимости:

pip install -r requirements.txt

Настроить файл config.py:

token = "YOUR_TELEGRAM_BOT_TOKEN"
barrier_phone = "PHONE_NUMBER_OR_ENDPOINT"

Настроить базу данных в mysql_handler.py (параметры подключения и функции для проверки и добавления пользователей).

Запустить бота:

python barrier_bot.py

Структура проекта

barrier_bot/
├── barrier_bot.py         # Основной файл для запуска бота
├── mysql_handler.py       # Модуль для работы с MySQL
├── uis_handler.py         # Модуль для управления шлагбаумом
├── config.py              # Конфигурационный файл (токен, телефон)
├── .gitignore             # Исключенные файлы (__pycache__, config.py и т.д.)
└── requirements.txt       # Список зависимостей

Использование

Запуск бота:

python barrier_bot.py

Взаимодействие с ботом в Telegram:

Отправьте команду /start для регистрации или входа.

Отправьте команду /open для открытия шлагбаума.

Если бот не отвечает, проверьте лог в консоли на наличие ошибок.

Дополнительно

Файл .gitignoreДобавьте в репозиторий, чтобы исключить:

__pycache__/
config.py

Рекомендации по безопасности:Не храните чувствительные данные в репозитории.

Надеемся, этот бот поможет вам упростить процесс управления доступом к шлагбауму!
