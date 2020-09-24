from  abc import ABC, abstractmethod
from telegram.ext import  CallbackContext
from  telegram import Update
from tools_package.abstract_classes import  TgCommand
from tools_package.tools import get_classes


class Start(TgCommand):
    """user start with this command"""
    @staticmethod
    def get_func():
        def func(update: Update, context: CallbackContext):
            """command for starting of a work"""
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Ready for a work")
        return func

    @staticmethod
    def get_name():
        return 'start'

    @staticmethod
    def show_in_help():
        return True


class Caps(TgCommand):
    """ Make all sended arguments upper"""
    @staticmethod
    def get_func():
        def func(update: Update, context: CallbackContext):
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=' '.join(context.args).upper())
        return func

    @staticmethod
    def get_name():
        return 'caps'

    @staticmethod
    def show_in_help():
        return True


if __name__ == '__main__':
    from inspect import getmembers, isclass
    print(getmembers(__name__), isclass)
    print(get_classes(__name__, TgCommand))



