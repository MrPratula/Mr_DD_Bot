
from utils.db import connect


def get_active(chat_id):

    db = connect()
    cursor = db.cursor(prepared=True)
    query = "SELECT char_id FROM active WHERE chat_id = %s"

    try:
        cursor.execute(query, (chat_id,))
    except:
        print("can not retriever char_id from active")

    result = cursor.fetchall()
    char_id = int(result[0][0])

    if not result:
        return None

    query = "SELECT char_name FROM `character` WHERE char_id = %s"

    try:
        cursor.execute(query, (char_id,))
    except:
        print("can not retriever char name from character")

    if not result and result[0][0] is not None:
        return None
    else:
        return char_id
