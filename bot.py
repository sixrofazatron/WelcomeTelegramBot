from dublib.Methods.JSON import ReadJSON 
import telebot
# import time  # Добавляем импорт модуля time для задержки
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


Settings = ReadJSON("tok.json")
bot = telebot.TeleBot(Settings["token"])

@bot.chat_join_request_handler()
def handle_join_request(message: telebot.types.ChatJoinRequest):

    # Создать клавиатуру с кнопкой
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(
        text="Я НЕ РОБОТ!", 
        url="https://t.me/"  # замените на корректный URL
    )
    keyboard.add(button)
    
    text = 'Чтобы присоединиться к каналу, подтвердите, что вы не робот, нажмите кнопку ниже и заявка автоматически одобрится. Извините, но это сделано для борьбы с ботами. Кнопка👇'

    # Первое сообщение
    bot.send_message(
        chat_id=message.from_user.id,
        text=text,
        parse_mode='HTML',  # Важно: включаем HTML-разметку
        reply_markup=keyboard
    )

if __name__ == '__main__':
    try:
        bot.infinity_polling(allowed_updates=telebot.util.update_types)
    except Exception as e:
        print(f"Ошибка: {e}")
