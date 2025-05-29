from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Xin chào, tôi là Chủ tịch Phạm Tuấn Dũng. Bạn cần gì?")

app = ApplicationBuilder().token("7868411673:AAFhQ2e8Mfm_aoVpB-YdZJC0O6RlNLAZJKM").build()
app.add_handler(CommandHandler("start", start))

print("Bot đang chạy...")
await application.bot.delete_webhook(drop_pending_updates=True)
app.run_polling()
