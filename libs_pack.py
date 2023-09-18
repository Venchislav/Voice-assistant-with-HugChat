import speech_recognition as sr
from rcgnize import recognize_user
import subprocess
from data import TOKEN
from termcolor import colored
from hugchat import hugchat
from hugchat.login import Login
from config import email, passwd
import webbrowser as wb
from _tts import say
from pc_controls import open_
import random
from translate import Translator
translator = Translator(to_lang="ru")

sign = Login(email, passwd)
cookies = sign.login()


cookie_path_dir = "./cookies_snapshot"
sign.saveCookiesToDir(cookie_path_dir)


chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
