from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters



# updater => contain api key  use as identifier to our bot
# update => act as lisner to commands
# call backcontext work internaly like callback
# commandHandler used to handle commands
# messageHandler handle message sent by user to bot
# filtter filet meassage and sent message

# functions
# first connect with our bot using API token
updater = Updater("5752150581:AAHJipMUWjEi0Cs18ytEkEuCib1xr2Guyts",
                  use_context=True)

# starting message                  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hi there , Welcome Back to the energy level bot")

# help functions        
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /getSinglePower - To get deatils of single device
    /getPowerList - To get details of all devices""")
# get device power
def get_power(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Your current is   10 A\
         Voltage  is       30V ")
  
# youtube_function
def get_all_details(update: Update, context: CallbackContext):
    update.message.reply_text("now dummy data =>\
    https://www.google.com/")

# unknown_function
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)  
#unknow text
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
            
 
# handler-section

updater.dispatcher.add_handler(CommandHandler('start' ,start))       
updater.dispatcher.add_handler(CommandHandler('getSinglePower', get_power)) 
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('getPowerList', get_all_details))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    # Filters out unknown commands
    Filters.command, unknown))
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))    #please varify


updater.start_polling()