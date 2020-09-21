from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from  telegram.ext import  MessageHandler
import json


def load_token():
    with open('aut_data.json') as j_file:
        data = json.load(j_file)
        return data['token']


def message_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Sample text'
    )

def main():
    """
        Function that doing all general launch
        all required functions
    """
    # load token

    updater = Updater(token=load_token(), use_context=True)
    updater.dispatcher.add_handler(MessageHandler(
        filters=Filters.all,
        callback=message_handler
    ))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    print('hello world')
