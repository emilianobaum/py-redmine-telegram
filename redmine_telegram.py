#!/usr/bin/python3
#-*-coding: utf-8-*-
from telethon import TelegramClient
from redminelib import Redmine
from json import load
import asyncio


class RT():
    
    def read_config():
        # The path to configuration file is fixed
        config = load("config/configuration.json")
    def __init__ ():
        # Read configuration file
        print(read_config())
        

if __name__ == "__main__":
    RT()