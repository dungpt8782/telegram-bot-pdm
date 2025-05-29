import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Xin chào, tôi là Chủ tịch PDM, Phạm Tuấn Dũng. Bạn cần gì?")

async def main():
    application = ApplicationBuilder().token("7868411673:AAFhQ2e8Mfm_aoVpB-YdZJC0O6RlNLAZJKM").build()

    await application.bot.delete_webhook(drop_pending_updates=True)
    application.add_handler(CommandHandler("start", start))

    print("Bot đang chạy...")
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    await application.updater.idle()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
