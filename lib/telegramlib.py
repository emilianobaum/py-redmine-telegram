from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Bot
import requests

def main(message=None):
    bot = Bot('xxxxxx:xxxxxxxxxxxxxxxxxx')
    bot.send_message(chat_id=-1111111111111111, text="{}".format(message))
