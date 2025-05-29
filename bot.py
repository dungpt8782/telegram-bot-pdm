from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Xin chào, tôi là Chủ tịch Phạm Tuấn Dũng. Bạn cần gì?")

app = ApplicationBuilder().token("7418220278:AAEm6L3b3ujbCVzE8i_qF-2sUddFFTdryWU").build()
app.add_handler(CommandHandler("start", start))

print("Bot đang chạy...")
app.run_polling()
