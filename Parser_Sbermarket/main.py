from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from my_parser import parse_site


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Введи ссылку на страницу сбермаркета, которую хочешь спарсить.')
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = update.message.text
    await parse_site(update, context, url)

def main() -> None:
    application = Application.builder().token('ВВЕДИ СЮДА СВОЙ ТОКИН БОТА').build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    application.run_polling()


if __name__ == '__main__':
    main()