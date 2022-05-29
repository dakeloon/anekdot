# anekdot
import requests
from bs4 import BeautifulSoup as b
import random
import telebot

URL = "https://www.anekdot.ru/last/good/"
API_Key = "5445774760:AAEsdh9b_7QBwHyQoD-KDJ1YGE4FtetsQ8M"
def parser(url):
    r = requests.get(URL)
    soup = b(r.text, "html.parser")
    anekdots = soup.find_all("div", class_="text")
    return [c.text for c in anekdots]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_Key)
@bot.message_handler(commands=["начать"])

def hello(message):
    bot.send_message(message.chat.id, "Здравствуйте! Чтобы словить смех введи любую цифру")

@bot.message_handler(content_types=["text"])
def jokes(message):
    if message.text.lower() in "123456789":
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, "Не знаешь что такое цифры?")

bot.polling()
