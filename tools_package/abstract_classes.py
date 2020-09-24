from abc import ABC, abstractmethod
from telegram.ext import CallbackContext
from telegram import Update


class TgCommand(ABC):
    @staticmethod
    @abstractmethod
    def get_func():
        def func(update: Update, context: CallbackContext):
            pass

        return func

    @staticmethod
    @abstractmethod
    def get_name():
        pass

    @staticmethod
    @abstractmethod
    def show_in_help():
        pass


class TgMessage(ABC):
    @staticmethod
    @abstractmethod
    def get_func():
        def func(update: Update, context: CallbackContext):
            pass
        return func

    @staticmethod
    @abstractmethod
    def get_filter():
        pass
