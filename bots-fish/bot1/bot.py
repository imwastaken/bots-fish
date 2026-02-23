import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.constants import ParseMode

# Вставьте сюда токен вашего бота от BotFather
BOT_TOKEN = "8736098331:AAFcmiDAM_5oLSd7O0k7z6_zK-OsmghuHG8"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    chat_id = update.effective_chat.id

    # Отправка картинки с текстом
    caption = f"<b>✋ Привет, {user_name}! Наш сервис позволяет узнать, как ты записан у других людей. Нажимай на кнопку ниже, и бот выдаст тебе список твоих записей.</b>"

    # Отправка фото с подписью и кнопкой
    await context.bot.send_photo(
        chat_id=chat_id,
        photo=open('photo_2025-12-07_02-35-39.jpg', 'rb'),  # Замените на путь к вашей картинке
        caption=caption,
        parse_mode=ParseMode.HTML,
    )

    # Отправка второго сообщения с эмодзи
    await context.bot.send_message(
        chat_id=chat_id,
        text="👇"
    )


def main():
    # Создание приложения
    application = Application.builder().token(BOT_TOKEN).build()

    # Регистрация обработчика команды /start
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    print("Бот запущен...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()





