# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup
import time
from vk_functions import *

verified_users = [677594685, 1388614078]

def echo(update, context):
    if update.message.from_user.id not in verified_users:
        update.message.reply_text(
            access_denied_message.format(id=update.message.from_user.id))
    else:
        update.message.reply_text(simple_message)
    # update.message.reply_text(update.message.text)


def append_friends(update, context):
    if update.message.from_user.id in verified_users:
        try:
            update.message.reply_text('Начиаем отправлять заявки :З')
            data = get_suggestionslist()
            i = 1
            success = 0
            vk_session = vk_api.VkApi(LOGIN, PASSWORD)
            vk_session.auth()
            vk = vk_session.get_api()
            for elem in data['items']:
                if i != 62:
                    mutual = vk.friends.getMutual(target_uid=elem['id'])
                    if len(mutual) >= quantity_mutual_friends:
                        vk.friends.add(user_id=elem['id'])
                        update.message.reply_text(a_lot_of_mutual_friends.format(elem["id"], i))
                        success += 1
                    else:
                        update.message.reply_text(few_or_no_mutual_friends.format(quantity_mutual_friends, i))
                    i += 1
                else:
                    update.message.reply_text(f'Попытались отправить {i} заявок. Из них {success} удачно.')
                    break
            i = 1
            success = 0
        except Exception as exep:
            update.message.reply_text(f'{exep}')
            update.message.reply_text(f'Попытались отправить {i} заявок. Из них {success} удачно.')

    else:
        update.message.reply_text(
            access_denied_message.format(id=update.message.from_user.id))


if __name__ == '__main__':
    while True:
        try:
            updater = Updater('1717505411:AAE3OCVeoifIq83By3Hbl7mOciXbndxWp9w', use_context=True)
            dp = updater.dispatcher
            dp.add_handler(CommandHandler("add", append_friends))
            text_handler = MessageHandler(Filters.text, echo)
            dp.add_handler(text_handler)
            updater.start_polling()
            updater.idle()
        except Exception as e:
            time.sleep(3)
            print(e)