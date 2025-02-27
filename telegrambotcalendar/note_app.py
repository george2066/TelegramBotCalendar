from telegram.ext import Updater, CommandHandler

from telegrambotcalendar.henlers import create_event
from telegrambotcalendar.secrets import API_TOKEN
from henlers import create_event

updater = Updater(token=API_TOKEN)

def create_note_handler(update, context):
    try:
        event_text = update.message.text
        event_name = update.message.chat_id
        create_event(event_text, event_name)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {event_name} создана.")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")




updater.dispatcher.add_handler(CommandHandler('create', create_note_handler))

updater.start_polling()