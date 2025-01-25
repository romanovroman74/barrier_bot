import telebot
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import mysql_handler
import uis_handler
import config

bot = telebot.TeleBot(config.token)

# Команда /menu - отправка кнопки для запроса контакта
@bot.message_handler(commands=['start'])
def request_contact(message):
    user_id = message.from_user.id

    # Проверка наличия пользователя в БД
    exists, error = mysql_handler.check_user_exists(user_id)
    
    if error:
        bot.send_message(message.chat.id, f"Ошибка базы данных: {error}")
        return

    if exists:
        # Если пользователь найден, отправляем inline-меню
        bot.send_message(message.chat.id, "Что бы открыть шлагбаум отправь команду /open", reply_markup=ReplyKeyboardRemove())
    else:
        # Если пользователя нет в БД, запрашиваем номер телефона
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button = KeyboardButton("Отправить номер", request_contact=True)
        markup.add(button)
        bot.send_message(
            message.chat.id, 
            "Вы не зарегистрированы. Пожалуйста, отправьте свой номер телефона, нажав кнопку ниже:", 
            reply_markup=markup
        )

# Обработка полученного контакта
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    if not message.contact:
        bot.send_message(message.chat.id, "Пожалуйста, используйте кнопку для отправки номера.")
        return

    user_id = message.contact.user_id
    phone_number = message.contact.phone_number
    first_name = message.from_user.first_name or "Не указано"
    last_name = message.from_user.last_name or "Не указано"

    # Проверяем, есть ли пользователь в базе
    exists, error = mysql_handler.check_user_exists(user_id)
    if error:
        bot.send_message(message.chat.id, f"Ошибка базы данных: {error}")
        return

    if exists:
        bot.send_message(message.chat.id, "Ваш номер уже зарегистрирован в системе. Теперь ты можешь открывать шлагбаум", reply_markup=ReplyKeyboardRemove())
    else:
        success, error = mysql_handler.add_user(user_id, phone_number, first_name, last_name)
        if success:
            bot.send_message(message.chat.id, "Номер успешно добавлен в базу данных. Теперь вы можете открыть шлагбаум командой /open", reply_markup=ReplyKeyboardRemove())
        else:
            bot.send_message(message.chat.id, f"Ошибка при добавлении номера: {error}")
            return


# Команда /open - открыть шлагбаум
@bot.message_handler(commands=['open'])
def open_barrier(message):
    uis_handler.start_simple_call(config.barrier_phone)
    bot.send_message(message.chat.id, "Шлагбаум открыт. Удачи!")

# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)