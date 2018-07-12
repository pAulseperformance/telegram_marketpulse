# Telegram Message Handler UI
# This is the main program to run to activate telegram bot
# It will handle user input and assign tasks to submodules for further processing
# when processing is complete callbacks will be assigned to message handler and displayed to user

# Import API keys
import api_keys.tele_keys as tk

# Enable Telegram Module for Bot handling
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, Bot)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler)

# Enable submodule for Analysis and Notifications
import Cryptocurrency.analysis as ana
import Cryptocurrency.cryptocompare_wrapper as ccw

# Enable logging
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Assign Telegram Token and Channel ID
TOKEN = tk.Token
MYChannelID = tk.MYChannelID
BOT = Bot(token=TOKEN)

CATEGORY, ACTION, ANALYSIS, NOTIFICATIONS, ASSET = range(5)

def start(bot, update):
    reply_keyboard = [['Cryptocurrency', 'Stocks', 'Forex']]

    update.message.reply_text(
        'Hi! My name is MarketpAulsebot. I will analyze the markets for you.\n '
        'My creator made me because analyzing the markets manually takes a lot of time and dedication \n'
        'After years of manual labor and data analysis he learned how to code so he could automate many of these tasks \n'
        'I use a blend of analysis techniques to help you decide where to put your money! \n'
        'Select an asset category to get started \n'
        'Send /cancel to stop talking to me.\n\n'
        'What are you looking to invest in today?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return CATEGORY

def Category(bot, update):
    reply_keyboard = [['Analysis', 'Notifications']]
    user = update.message.from_user
    category = update.message.text
    logger.info("%s has selected %s", user.first_name, category)

    output  = 'Great! {} is a hot new market. \n '.format(category)
    output += 'Do you want me to analyze something for you or send a notification if I see an opportunity? '
    update.message.reply_text(output,
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return ACTION

def Action(bot, update):
    if update.message.text == 'Analysis':
        output  = 'Ok, {}. What coin do you want me to analyze?\n'.format(update.message.from_user.first_name)
        output += 'Type in your entry, for example "BTC-USD" '
        update.message.reply_text(output,reply_markup=ReplyKeyboardRemove())

        return ANALYSIS

    if update.message.text == 'Notifications':
        update.message.reply_text('I can analyze the markets 24/7 for you!\n'
                                  'Select a trigger point and I\'ll send you a message '
                                  'when I see an opportunity in the making!\n '
                                  'There are many different strategies we can monitor, \n'
                                  'but we like to keep it simple for now\n\n')


        # TODO: do something here

        return NOTIFICATIONS
    else:
        update.message.reply_text('Please make a valid selection to continue ')

        return CATEGORY

        # TODO: Give option to CANCEL and restart at every point

def Analysis(bot, update):
    # TODO: must filter regex for hyphenated pairs
    symbol = update.message.text
    message  = 'Analyzing... This should only take a second\n\n'
    update.message.reply_text(message)
    # TODO: Telegram has a function that shows bot is working Add that here.
    output = ana.asset_info_day(symbol)
    update.message.reply_text(output)

    return ConversationHandler.END


def Notifications(bot, update):
    # TODO: Check is user is subscribed or limit user to only one notification for sampling
    output = "Sorry, {} you need to subscribe in order to do that".format(update.message.from_user)
    update.message.reply_text(output)

    return ConversationHandler.END


def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states Cryptocurrency, Stocks, Forex
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            CATEGORY: [MessageHandler(Filters.text, Category)],

            ACTION: [MessageHandler(Filters.text, Action)],

            ANALYSIS: [MessageHandler(Filters.text, Analysis)],

            NOTIFICATIONS: [MessageHandler(Filters.text, Notifications)]

        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

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
