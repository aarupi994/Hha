# telegram_lookup_bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

# Replace with your bot token
BOT_TOKEN = "8294178048:AAFHWvl_MS9VdLsCsl9p28hNSq1nZIp1AXg"

# ------------------- Functions -------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "Привет! Я бот для поиска информации.\n\n"
        "Используй команды:\n"
        "/phone <номер> - поиск по номеру\n"
        "/email <почта> - поиск по email"
    )
    await update.message.reply_text(welcome_text)

async def probivnomer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Использование: /phone <номер>")
        return
    number = context.args[0]
    api_url = f"https://api.depsearch.digital/quest={number}?token=bdIUze7ym7OqJ7kd4GHJ3S9wgDOqTDmE&lang=ru"
    try:
        response = requests.get(api_url)
        data = response.json()
        results = data.get("results", [])
        if not results:
            await update.message.reply_text("Ничего не найдено 😕")
        else:
            for result in results:
                text = "\n".join([f"{k}: {v}" for k, v in result.items()])
                await update.message.reply_text(text)
    except Exception as e:
        await update.message.reply_text(f"Ошибка API: {e}")

async def probivpochta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Использование: /email <почта>")
        return
    email = context.args[0]
    api_url = f"https://api.depsearch.digital/quest={email}?token=bdIUze7ym7OqJ7kd4GHJ3S9wgDOqTDmE&lang=ru"
    try:
        response = requests.get(api_url)
        data = response.json()
        results = data.get("results", [])
        if not results:
            await update.message.reply_text("Ничего не найдено 😕")
        else:
            for result in results:
                text = "\n".join([f"{k}: {v}" for k, v in result.items()])
                await update.message.reply_text(text)
    except Exception as e:
        await update.message.reply_text(f"Ошибка API: {e}")

# ------------------- Bot Setup -------------------

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("phone", probivnomer))
    app.add_handler(CommandHandler("email", probivpochta))

    print("Bot запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
