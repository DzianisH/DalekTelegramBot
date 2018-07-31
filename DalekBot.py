#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import logging

kb = [[telegram.KeyboardButton('/вперёд'), telegram.KeyboardButton('/назад')],
          [telegram.KeyboardButton('/стоп'), telegram.KeyboardButton('/уничтожить!')],
          [telegram.KeyboardButton('/левее'), telegram.KeyboardButton('/правее')],
		  ]
kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True)
	
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def hold_forward(bot, update):
    reply(bot, update, 'Далек начал движение вперёд')
	
def hold_backward(bot, update):
    reply(bot, update, 'Далек начал движение назад')
	
def stop(bot, update):
    reply(bot, update, 'Далек остановился')
	
def turn_left(bot, update):
    reply(bot, update, 'Далек повернул левее')
	
def turn_right(bot, update):
    reply(bot, update, 'Далек повернул правее')
	
def exterminate(bot, update):
    reply(bot, update, 'Далек уничтожает цель')

def help(bot, update):
    reply(bot, update, 'Приказывайте Далеку, повелитель')
	
def reply(bot, update, text):
    """Reply to user."""
    bot.send_message(chat_id=update.message.chat_id, text=text, reply_markup=kb_markup)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)
	

def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("695206856:AAG52aAF3o0-KLqd6SZk9kuOUdEQ_-RFxYs")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("вперёд", hold_forward))
    dp.add_handler(CommandHandler("назад", hold_backward))
    dp.add_handler(CommandHandler("стоп", stop))
    dp.add_handler(CommandHandler("левее", turn_left))
    dp.add_handler(CommandHandler("правее", turn_right))
    dp.add_handler(CommandHandler("уничтожить!", exterminate))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, help))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()