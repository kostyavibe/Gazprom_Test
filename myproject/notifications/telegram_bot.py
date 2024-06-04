from telegram.ext import Updater, CommandHandler
import logging
from django.contrib.auth.models import User

# Настройки логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater("YOUR_TELEGRAM_TOKEN", use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text('Welcome to the Birthday Notification Bot!')

def subscribe(update, context):
    update.message.reply_text('You have been subscribed to birthday notifications.')

def unsubscribe(update, context):
    update.message.reply_text('You have been unsubscribed from birthday notifications.')

start_handler = CommandHandler('start', start)
subscribe_handler = CommandHandler('subscribe', subscribe)
unsubscribe_handler = CommandHandler('unsubscribe', unsubscribe)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(subscribe_handler)
dispatcher.add_handler(unsubscribe_handler)

updater.start_polling()
updater.idle()
