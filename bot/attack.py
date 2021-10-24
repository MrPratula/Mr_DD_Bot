
import re

from telegram import InlineKeyboardMarkup

from utils.get_active import get_active
from utils.lang import text
from utils.keyboard import keyboard_attack, keyboard_attack_2, keyboard_attack_ask1, keyboard_attack_ask2
from utils.db import connect
from utils.die import roll


def attack(update, context):
    char_id = get_active(update.message.from_user.id)

    if char_id is None:
        update.message.reply_text(text("info_no_active"))
        return

    keyboard = keyboard_attack()

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.user_data.update({"char_id": char_id})

    update.message.reply_text(text("attack_init"), reply_markup=reply_markup)


def attack_choose_weapon_spell(update, context):

    query = update.callback_query
    choice = query.data[9:]
    char_id = context.user_data["char_id"]

    options = get_attacks(choice, char_id)

    keyboard = keyboard_attack_2(options, choice)

    if choice == "weapon":

        if not keyboard:
            message = text("attack_no_weapons")
            query.edit_message_text(message)

        else:
            reply_markup = InlineKeyboardMarkup(keyboard)
            message = text("attack_choose_weapon")
            query.edit_message_text(message, reply_markup=reply_markup)

    else:

        if not keyboard:
            message = text("attack_no_spells")
            query.edit_message_text(message)

        else:
            reply_markup = InlineKeyboardMarkup(keyboard)
            message = text("attack_choose_spells")
            query.edit_message_text(message, reply_markup=reply_markup)


def make_attack_button(update, context):

    query = update.callback_query
    weapon_name = query.data[16:]
    char_id = context.user_data["char_id"]

    db = connect()
    cursor = db.cursor(prepared=True)

    sql_query = "SELECT damage, versatile_dmg, `mod` FROM weapons WHERE name = %s"

    try:
        cursor.execute(sql_query, (weapon_name,))
    except:
        print("can not retriever weapon details")

    result = cursor.fetchall()

    dmg = result[0][0]
    versatile_dmg = result[0][1]
    mod = result[0][2]

    sql_query = "SELECT char_name, strength, dexterity, proficiency FROM `character` WHERE char_id = %s"

    try:
        cursor.execute(sql_query, (char_id,))
    except:
        print("can not get character stat for attack")

    result = cursor.fetchall()

    char_name = result[0][0]
    strength = int(result[0][1])
    dexterity = int(result[0][2])
    proficiency = int(result[0][3])

    context.user_data.update({"char_name": char_name})
    context.user_data.update({"weapon_name": weapon_name})
    context.user_data.update({"proficiency": proficiency})
    context.user_data.update({"dmg": dmg})
    context.user_data.update({"versatile_dmg": versatile_dmg})
    context.user_data.update({"strength": strength})
    context.user_data.update({"dexterity": dexterity})

    if versatile_dmg is not None:

        if mod == "strength":
            mod_value = strength // 2 - 5
        else:
            mod_value = dexterity // 2 - 5

        context.user_data.update({"mod_value": mod_value})

        keyboard = keyboard_attack_ask1()
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = text("attack_choose_versatile")
        query.edit_message_text(message, reply_markup=reply_markup)

    elif mod == "finesse":
        keyboard = keyboard_attack_ask2(strength // 2 - 5, dexterity // 2 - 5)
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = text("attack_choose_mod")
        query.edit_message_text(message, reply_markup=reply_markup)

    else:

        if mod == "strength":
            mod_value = strength // 2 - 5
        else:
            mod_value = dexterity // 2 - 5

        if not is_proficient(char_id, weapon_name):
            proficiency = 0

        roll1 = roll("d20")[0]
        roll2 = roll("d20")[0]
        roll3 = roll(dmg)
        damage = " + ".join(str(n) for n in roll3)
        tot_damage = 0
        for n in roll3:
            tot_damage += int(n)

        message = text("attack_normal").format(char_name.capitalize(),
                                               weapon_name.capitalize(),
                                               roll1,
                                               mod_value,
                                               proficiency,
                                               roll1 + mod_value + proficiency,
                                               roll2,
                                               roll2 + mod_value + proficiency,
                                               damage,
                                               tot_damage)

        context.user_data.clear()
        query.edit_message_text(message)


def versatile_attack_button(update, context):

    query = update.callback_query
    choice = query.data[9:]

    data = context.user_data
    char_name = data["char_name"]
    weapon_name = data["weapon_name"]
    proficiency = data["proficiency"]
    dmg = data["dmg"]
    versatile_dmg = data["versatile_dmg"]
    mod_value = data["mod_value"]

    if choice == "1":
        var = dmg
    else:
        var = versatile_dmg

    roll1 = roll("d20")[0]
    roll2 = roll("d20")[0]
    roll3 = roll(var)
    damage = " + ".join(str(n) for n in roll3)
    tot_damage = 0
    for n in roll3:
        tot_damage += int(n)

    message = text("attack_normal").format(char_name.capitalize(),
                                           weapon_name.capitalize(),
                                           roll1,
                                           mod_value,
                                           proficiency,
                                           roll1 + mod_value + proficiency,
                                           roll2,
                                           roll2 + mod_value + proficiency,
                                           damage,
                                           tot_damage)

    context.user_data.clear()
    query.edit_message_text(message)


def finesse_attack_button(update, context):

    query = update.callback_query
    choice = query.data[9:]

    data = context.user_data
    char_name = data["char_name"]
    weapon_name = data["weapon_name"]
    proficiency = data["proficiency"]
    dmg = data["dmg"]
    strength = data["strength"]
    dexterity = data["dexterity"]

    if choice == "str":
        mod_value = strength // 2 - 5
    else:
        mod_value = dexterity // 2 - 5

    roll1 = roll("d20")[0]
    roll2 = roll("d20")[0]
    roll3 = roll(dmg)
    damage = " + ".join(str(n) for n in roll3)
    tot_damage = 0
    for n in roll3:
        tot_damage += int(n)

    message = text("attack_normal").format(char_name.capitalize(),
                                           weapon_name.capitalize(),
                                           roll1,
                                           mod_value,
                                           proficiency,
                                           roll1 + mod_value + proficiency,
                                           roll2,
                                           roll2 + mod_value + proficiency,
                                           damage,
                                           tot_damage)

    context.user_data.clear()
    query.edit_message_text(message)


def cast_spell_button(update, context):

    query = update.callback_query
    spell_name = query.data[15:]
    char_id = context.user_data["char_id"]

    db = connect()
    cursor = db.cursor(prepared=True)

    sql_query = "SELECT text FROM cantrip WHERE name = %s"

    try:
        cursor.execute(sql_query, (spell_name,))
    except:
        print("can not retriever cantrip text")

    result = cursor.fetchall()
    cantrip_text = result[0][0]

    message = parse_spell(cantrip_text, char_id)

    context.user_data.clear()
    query.edit_message_text(message)


def get_attacks(choice, char_id):
    db = connect()
    cursor = db.cursor(prepared=True)

    sql_query = ""

    if choice == "weapon":

        sql_query = "SELECT weapon FROM has_weapon WHERE char_id = %s "

    else:  # choice == 'spell'
        sql_query = "SELECT spell_name FROM has_spell WHERE char_id = %s "

    try:
        cursor.execute(sql_query, (char_id,))
    except:
        print("can not get character's weapons")

    result = cursor.fetchall()
    options = []

    for option in result:
        options.append(option[0])

    return options


def is_proficient(char_id, weapon):

    db = connect()
    cursor = db.cursor(prepared=True)

    query1 = "SELECT type FROM weapons WHERE name = %s"
    query2 = "SELECT class FROM `character` WHERE char_id = %s"

    try:
        cursor.execute(query1, (weapon,))
    except:
        print("can not retriever weapon type")

    result = cursor.fetchall()
    weapon_type = result[0][0]

    try:
        cursor.execute(query2, (char_id,))
    except:
        print("can not retriever char class")

    result = cursor.fetchall()
    char_class = result[0][0]

    if weapon_type == "martial" or weapon_type == "martial_ranged":
        ask = "martial_proficiency"
    else:
        ask = "simple_proficiency"

    sql_query = "SELECT IF({} = true, 'true', specific_proficiency) " \
                "FROM class WHERE name = %s".format(ask)

    try:
        cursor.execute(sql_query, (char_class,))
    except:
        print("can not know if character is proficient with a weapon")

    result = cursor.fetchall()
    result = result[0][0]

    if result is None:
        return False

    elif result == "true":
        return True

    else:
        result = result.split(",")

        if weapon in result:
            return True
        else:
            return False


def parse_spell(rule, char_id):

    db = connect()
    cursor = db.cursor(prepared=True)

    query = "SELECT char_name, level, intelligence, wisdom, charisma, proficiency, class " \
            "FROM `character` WHERE char_id = %s"

    try:
        cursor.execute(query, (char_id,))
    except:
        print("can not retriever char name")

    result = cursor.fetchall()
    char_name = result[0][0]

    try:
        char_level = int(result[0][1])
    except:
        char_level = 1

    rule = re.sub("{name}", char_name.capitalize(), rule)
    rolls = re.findall("{xd+[0-9]}", rule)
    rolls_number = get_rolls(char_level)

    # FIX HERE

    for r in rolls:

        r = r.replace("x", str(rolls_number))
        r = r.replace("{", "")
        r = r.replace("}", "")

        rolls_array = roll(r)
        rolls_string = " + ".join(str(n) for n in rolls_array)
        rolls_total = 0
        for i in rolls_array:
            rolls_total += i

        final = rolls_string + " = " + str(rolls_total)

        rule = re.sub("{xd+[0-9]}", final, rule, 1)

    # TILL HERE

    intelligence = result[0][2]
    wisdom = result[0][3]
    charisma = result[0][4]
    proficiency = result[0][5]
    character_class = result[0][6]

    query = "SELECT spellcasting FROM class WHERE name = %s"

    try:
        cursor.execute(query, (character_class,))
    except:
        print("can not retriever class spellcasting ability")

    result = cursor.fetchall()
    spellcasting_ability = result[0][0]

    print(spellcasting_ability)

    if spellcasting_ability == "intelligence":
        spellcasting_ability = intelligence // 2 - 5
    elif spellcasting_ability == "wisdom":
        spellcasting_ability = wisdom // 2 - 5
    else:
        spellcasting_ability = charisma // 2 - 5

    die = roll("d20")[0]

    attack_text = "{} + {} + {} = {}".format(str(die), str(proficiency), str(spellcasting_ability),
                                                 die + proficiency + spellcasting_ability)

    rule = re.sub("{spell_attack}", attack_text, rule)

    save_dc_text = "8 + {} + {} = {}".format(str(proficiency), spellcasting_ability,
                                             8 + proficiency + spellcasting_ability)

    rule = re.sub("{spell_save_dc}", save_dc_text, rule)

    print(intelligence)
    print(spellcasting_ability)

    return rule


def get_rolls(level):

    if 5 <= level < 11:
        return 2
    elif 11 <= level < 17:
        return 3
    elif level > 17:
        return 4
    else:
        return 1
