from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import CommandHandler
import logging
import json


def load_token():
    with open('aut_data.json') as j_file:
        data = json.load(j_file)
        return data['token']


def start_command(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Ready for a work")


def caps_command(update: Update, context: CallbackContext):
    """ Make all sended arguments upper"""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=' '.join(context.args).upper())


def unknown_command(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="sorry, i don't understand this command")


def message_handler(update: Update, context: CallbackContext):
    update.message.reply_text(text='Sample text')


def main():
    """
        Function that doing all general launch
        all required functions
    """
    # creating updater and local dispatcher
    updater = Updater(token=load_token(), use_context=True)
    dispatcher = updater.dispatcher
    # adding logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    # adding handlers
    mes_filter = Filters.text & (~Filters.command)

    dispatcher.add_handler(MessageHandler(mes_filter, message_handler))
    dispatcher.add_handler(CommandHandler('caps', caps_command ))
    dispatcher.add_handler(CommandHandler('start', start_command))
    # this handler must be added last!
    dispatcher.add_handler(MessageHandler(Filters.command, unknown_command))
    # start work of bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()