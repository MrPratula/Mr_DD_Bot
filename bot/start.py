import mysql.connector


from utils.lang import text
from utils.db import connect


def start(update, context):

    db = connect()
    cursor = db.cursor(prepared=True)
    query = "SELECT username FROM user WHERE chat_id = %s"

    chat_id = update.message.from_user.id

    if update.message.from_user.username is not None:
        name = update.message.from_user.username
    else:
        name = update.message.from_user.first_name

    try:
        cursor.execute(query, (chat_id,))
    except:
        print("can not retriever user username in start")

    result = cursor.fetchall()

    if not result:

        query = "INSERT INTO user (chat_id, username) VALUES (%s, %s)"
        data = (chat_id, name)

        try:
            cursor.execute(query, data)
            db.commit()
        except mysql.connector.errors.IntegrityError:
            print("can not add user into db")

        query = "INSERT INTO active (chat_id, char_id) VALUES (%s, %s)"
        data = (chat_id, None)

        try:
            cursor.execute(query, data)
            db.commit()
        except mysql.connector.errors.IntegrityError:
            print("can not init active table for new user")

        message = text("start_new")

    else:
        message = text("start").format(name)

    context.bot.send_message(chat_id=chat_id, text=message)
