from telegram.ext import Updater, CommandHandler
from telegrambotcalendar.secrets import API_TOKEN
from henlers import create_note, read_note, update_note, delete_note, read_all_notes

updater = Updater(token=API_TOKEN)

def create_note_handler(update, context):
    try:
        note_text = update.message.text
        note_name = update.message.chat_id
        create_note(note_text, note_name)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} создана.")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")

def read_note_handler(update, context):
    try:
        note_name = update.message.chat_id
        text = read_note(note_name)
        context.bot.send_message(chat_id=update.message.chat_id, text=text)
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")

def update_note_handler(update, context):
    try:
        note_name = update.message.chat_id
        note_text = update.message.text
        update_note(note_name, note_text)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} обновлена.")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")

def delete_note_handler(update, context):
    try:
        note_name = update.message.chat_id
        delete_note(note_name)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} удалена.")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")

def read_all_note_handler(update, context):
    try:
        note_name = update.message.chat_id
        list_notes = '\n'.join(read_all_notes(note_name))
        context.bot.send_message(chat_id=update.message.chat_id, text=list_notes)
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")


updater.dispatcher.add_handler(CommandHandler('create', create_note_handler))
updater.dispatcher.add_handler(CommandHandler('read', read_note_handler))
updater.dispatcher.add_handler(CommandHandler('update', update_note_handler))
updater.dispatcher.add_handler(CommandHandler('delete', delete_note_handler))

updater.start_polling()