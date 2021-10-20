
from utils.lang import text
from utils.db import connect


def dm(update, context):

    user = update.message.from_user.id

    db = connect()
    cursor = db.cursor(prepared=True)

    query = "UPDATE user SET is_dm = not is_dm WHERE chat_id = %s "

    try:
        cursor.execute(query, (user,))
        db.commit()
    except:
        print("can not change is_dm")

    query = "SELECT is_dm FROM user WHERE chat_id = %s"

    try:
        cursor.execute(query, (user,))
    except:
        print("can not retriever is_dm after update")

    result = cursor.fetchall()

    if result == [('\x00',)]:
        message = text("dm_false")
    else:
        message = text("dm_true")

    update.message.reply_text(message)
