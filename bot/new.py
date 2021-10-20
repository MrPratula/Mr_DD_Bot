import datetime
import mysql.connector

from telegram.ext import ConversationHandler

from utils.db import connect
from utils.lang import text


NAME, STR, DEX, CON, INT, WIS, CHA, PRO = range(8)


def new(update, context) -> int:
    update.message.reply_text(text("new_start"))

    return NAME


def cancel(update, context) -> int:
    message = text("new_cancel")
    update.message.reply_text(message)

    return ConversationHandler.END


def name(update, context) -> int:
    message = update.message.text
    context.user_data.update({"name": message})
    update.message.reply_text(text("new_strength"))

    return STR


def strength(update, context) -> int:
    message = update.message.text
    context.user_data.update({"strength": message})
    update.message.reply_text(text("new_dexterity"))

    return DEX


def dexterity(update, context) -> int:
    message = update.message.text
    context.user_data.update({"dexterity": message})
    update.message.reply_text(text("new_constitution"))

    return CON


def constitution(update, context) -> int:
    message = update.message.text
    context.user_data.update({"constitution": message})
    update.message.reply_text(text("new_intelligence"))

    return INT


def intelligence(update, context) -> int:
    message = update.message.text
    context.user_data.update({"intelligence": message})
    update.message.reply_text(text("new_wisdom"))

    return WIS


def wisdom(update, context) -> int:
    message = update.message.text
    context.user_data.update({"wisdom": message})
    update.message.reply_text(text("new_charisma"))

    return CHA


def charisma(update, context) -> int:
    message = update.message.text
    context.user_data.update({"charisma": message})
    update.message.reply_text(text("new_proficiency"))

    return PRO


def proficiency(update, context) -> int:
    message = update.message.text
    context.user_data.update({"proficiency": message})

    db = connect()
    cursor = db.cursor(prepared=True)

    query = "INSERT INTO `character` (  char_name, strength, dexterity, constitution, intelligence," \
            "                           wisdom, charisma, proficiency) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    data = context.user_data

    val = [data["name"], data["strength"], data["dexterity"], data["constitution"], data["intelligence"],
           data["wisdom"], data["charisma"], data["proficiency"]]

    try:
        cursor.execute(query, val)
        db.commit()
    except mysql.connector.errors.IntegrityError:
        print("can not add new character into db")

    last_id = cursor.lastrowid
    date = "{}-{}-{}".format(datetime.datetime.now().strftime("%Y"),
                             datetime.datetime.now().strftime("%m"),
                             datetime.datetime.now().strftime("%d"))

    query = "INSERT INTO own (user_id, char_id, creation_date) VALUES (%s, %s, %s)"
    data = (update.message.from_user.id, last_id, date)

    try:
        cursor.execute(query, data)
        db.commit()
    except mysql.connector.errors.IntegrityError:
        print("can not link new character to user")

    context.user_data.clear()
    update.message.reply_text(text("new_end"))

    return ConversationHandler.END
