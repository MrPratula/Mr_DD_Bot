
from utils.db import connect


def has_class(char_id):

    db = connect()
    cursor = db.cursor(prepared=True)

    sql_query = "SELECT class FROM `character` WHERE char_id = %s"

    try:
        cursor.execute(sql_query, (char_id,))
    except:
        print("can not retriever character class")

    result = cursor.fetchall()

    if result[0][0] is None:
        return False
    else:
        return True
