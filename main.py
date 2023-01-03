from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, \
    CallbackContext
from func import *
from cons import *
from telegram.ext import Updater, CommandHandler

upd = Updater(TOKEN)
dis = upd.dispatcher
j = upd.job_queue
dis.add_handler(CommandHandler(command='start', callback=start))
dis.add_handler(MessageHandler(Filters.text, next_func))
upd.start_polling()
upd.idle()
