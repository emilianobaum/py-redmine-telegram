#!/usr/bin/python3
#-*-coding: utf-8-*-
from telethon import TelegramClient
from redminelib import Redmine
from json import load
import asyncio


class RT:
    
    def read_config(self):
        # The path to configuration file is fixed
        config = load("config/configuration.json")
        
    def __init__(self):
        # Read configuration file
        print(self.read_config())
    
    def redmine_connection(self):
        redmine = Redmine('https://redmine.url', username='foo', password='bar')

RT()
# if __name__ == "__main__":
#     RT