#!/usr/bin/python

from lib import redminelib
from json import load
from lib import telegramlib

class RT():

    def load_config(self):
        with open("config/configuration.json") as fp:
            data = load(fp)
        return data["redmine"], data["telegram"]
    
    def __get_redmine_data(self, issues=None):
        redmine, telegram = self.load_config()
        conn = redminelib.Redmine(redmine["host"], (redmine["user"], redmine["passwd"]))
        print("CONN: ",conn)
        print(conn.getIssues())
        return(conn.getIssues())
    
    def __send_to_telegram(self, message=None):
        telegramlib.main(message)
        
    def __init__(self):
        print("inicia")
        for n in self.__get_redmine_data():
            print(n)
            #self.__send_to_telegram(n)

r = RT()

r()