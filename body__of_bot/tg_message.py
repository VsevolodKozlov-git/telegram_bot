from telegram.ext import CallbackContext, Filters
from telegram import Update
from tools_package.abstract_classes import TgMessage


class TextMessage(TgMessage):
    @staticmethod
    def get_func():
        def func(update: Update, context: CallbackContext):
            update.message.reply_text('text message')
        return func

    @staticmethod
    def get_filter():
        return Filters.text & (~Filters.command)


class UnknownCommand(TgMessage):
    @staticmethod
    def get_func():
        def func(update: Update, context: CallbackContext):
            update.message.reply_text("I don't know this command. Plz use /help")
        return func

    @staticmethod
    def get_filter():
        return Filters.command

