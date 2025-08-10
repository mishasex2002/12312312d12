# - *- coding: utf- 8 - *-
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")
BOT_TOKEN = config["settings"]["token"]
main_admin = config["settings"]["main_admin"]

bot_version = "2.9"
bot_description = f"/b></a>"
