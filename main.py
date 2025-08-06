import asyncio
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Token dari @ProScalpersbot
TOKEN = "8101484453:AAFlsP6Af3DsbfdH-dmwze3KHRK8zfdDUW0"

# Fungsi untuk handle perintah /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Bot ProScalpers aktif! 🚀 Siap kirim sinyal!")

# Fungsi utama untuk menjalankan bot
async def main():
    print("🚀 Starting ProScalpers bot...")
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    await application.run_polling()

# Jalankan program
if __name__ == "__main__":
    print("✅ Bot is running...")
    asyncio.run(main())
