from utils.lang import text


def help(update, context):

    chat_id = update.message.from_user.id
    message = text("help")

    context.bot.send_message(chat_id=chat_id, text=message)
