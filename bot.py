import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

logging.basicConfig(level=logging.INFO)

TOKEN = "7824571767:AAGkLwPpe3V03hc84WsoRsl64b5oN_hf4k4"

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! 👋\nSend /in when you arrive and /out when you leave.")

# Attendance IN
async def check_in(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await update.message.reply_text(f"🟢 Checked IN at: {now}")

# Attendance OUT
async def check_out(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await update.message.reply_text(f"🔴 Checked OUT at: {now}")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("in", check_in))
    app.add_handler(CommandHandler("out", check_out))

    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
