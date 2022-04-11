from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Bot
import requests

def main(message=None):
    bot = Bot('5250509573:AAGqAfn6OMu7p2SnWCSzVGhaVHUvtDqVNCQ')
    bot.send_message(chat_id=-1001562929409, text="{}".format(message))
