from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import CommandHandler
import tg_message, tg_commands
from tools_package import tools, abstract_classes
import inspect
import logging
import json


def load_token():
    with open('aut_data.json') as j_file:
        data = json.load(j_file)
        return data['token']


updater = Updater(token=load_token(), use_context=True)
dispatcher = updater.dispatcher


def add_command_handlers():
    classes = tools.get_classes(tg_commands, abstract_classes.TgCommand)
    for _class in classes:
        func = _class.get_func()
        name = _class.get_name()

        dispatcher.add_handler(CommandHandler(command=name, callback=func))


def add_help_command():
    def help_string():
        res = ''
        classes = tools.get_classes(tg_commands, abstract_classes.TgCommand)
        filt_func = lambda x: x.show_in_help()
        classes = list(filter(filt_func, classes))
        for _class in classes:
            res += f'/{_class.get_name()}: {_class.__doc__} \n'
        return res

    def func(update: Update, context: CallbackContext):
        update.message.reply_text(help_string())

    dispatcher.add_handler(CommandHandler(command='help', callback=func))


def add_message_handler():
    classes = tools.get_classes(tg_message, abstract_classes.TgMessage)
    for _class in classes:
        func = _class.get_func()
        mes_filter = _class.get_filter()
        dispatcher.add_handler(MessageHandler(filters=mes_filter, callback=func))


def main():
    """
        Function that doing all general launch
        all required functions
    """
    # start logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    # !it's important too add command handler first because of UnknownCommand
    add_command_handlers()
    add_help_command()
    add_message_handler()
    # start work of bot
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
