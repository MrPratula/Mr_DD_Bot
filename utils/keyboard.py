from telegram import InlineKeyboardButton


def keyboard_language():
    keyboard = [[InlineKeyboardButton("English  🇺🇸", callback_data="lang_en"),
                 InlineKeyboardButton("Italiano  🇮🇹", callback_data="lang_it")],

                [InlineKeyboardButton("Español  🇪🇸", callback_data="lang_es")]]

    return keyboard


def keyboard_die():
    keyboard = [[InlineKeyboardButton("d4", callback_data="d_4"),
                 InlineKeyboardButton("d6", callback_data="d_6")],

                [InlineKeyboardButton("d8", callback_data="d_8"),
                 InlineKeyboardButton("d10", callback_data="d_10")],

                [InlineKeyboardButton("d12", callback_data="d_12"),
                 InlineKeyboardButton("d20", callback_data="d_20")]]

    return keyboard


def keyboard_ability():
    keyboard = [[InlineKeyboardButton("Strength", callback_data="check1_str"),
                 InlineKeyboardButton("Dexterity", callback_data="check1_dex")],

                [InlineKeyboardButton("Constitution", callback_data="check1_con"),
                 InlineKeyboardButton("Intelligence", callback_data="check1_int")],

                [InlineKeyboardButton("Wisdom", callback_data="check1_wis"),
                 InlineKeyboardButton("Charisma", callback_data="check1_cha")]]

    return keyboard


def keyboard_sub_ability(ability):
    keyboard = []

    if ability == "str":

        keyboard = [[InlineKeyboardButton("Strength", callback_data="check2_str"),
                     InlineKeyboardButton("Saving Throws", callback_data="check2_str_sav")],

                    [InlineKeyboardButton("Athletics", callback_data="check2_ath")]]

    elif ability == "dex":

        keyboard = [[InlineKeyboardButton("Dexterity", callback_data="check2_dex"),
                     InlineKeyboardButton("Saving Throws", callback_data="check2_dex_sav")],

                    [InlineKeyboardButton("Acrobatics", callback_data="check2_acr"),
                     InlineKeyboardButton("Sleight of Hands", callback_data="check2_sle")],

                    [InlineKeyboardButton("Stealth", callback_data="check2_stl")]]

    elif ability == "con":

        keyboard = [[InlineKeyboardButton("Constitution", callback_data="check2_con"),
                     InlineKeyboardButton("Saving Throws", callback_data="check2_con_sav")]]

    elif ability == "int":

        keyboard = [[InlineKeyboardButton("Intelligence", callback_data="check2_int"),
                     InlineKeyboardButton("Saving Throws", callback_data="check2_int_sav")],

                    [InlineKeyboardButton("Arcana", callback_data="check2_arc"),
                     InlineKeyboardButton("History", callback_data="check2_his")],

                    [InlineKeyboardButton("Investigation", callback_data="check2_inv"),
                     InlineKeyboardButton("Nature", callback_data="check2_nat")],

                    [InlineKeyboardButton("Religion", callback_data="check2_rel")]]

    elif ability == "wis":

        keyboard = [[InlineKeyboardButton("Wisdom", callback_data="check2_wis"),
                     InlineKeyboardButton("Saving Throws", callback_data="check2_wis_sav")],

                    [InlineKeyboardButton("Animal Handling", callback_data="check2_ani"),
                     InlineKeyboardButton("Insight", callback_data="check2_ins")],

                    [InlineKeyboardButton("Medicine", callback_data="check2_med"),
                     InlineKeyboardButton("Perception", callback_data="check2_per")],

                    [InlineKeyboardButton("Survival", callback_data="check2_sur")]]

    elif ability == "cha":

        keyboard = [[InlineKeyboardButton("Charisma", callback_data="check2_cha"),
                     InlineKeyboardButton("Saving Throws", callback_data="check2_cha_sav")],

                    [InlineKeyboardButton("Deception", callback_data="check2_dec"),
                     InlineKeyboardButton("Intimidation", callback_data="check2_itm")],

                    [InlineKeyboardButton("Performance", callback_data="check2_prf"),
                     InlineKeyboardButton("Persuasion", callback_data="check2_prs")]]

    return keyboard


def keyboard_proficiency():
    keyboard = [[InlineKeyboardButton("Strength ST", callback_data="prof_str"),
                 InlineKeyboardButton("Athletics", callback_data="prof_ath")],

                [InlineKeyboardButton("Dexterity ST", callback_data="prof_dex"),
                 InlineKeyboardButton("Acrobatics", callback_data="prof_acr")],

                [InlineKeyboardButton("Sleight of Hand", callback_data="prof_sle"),
                 InlineKeyboardButton("Stealth", callback_data="prof_stl")],

                [InlineKeyboardButton("Constitution ST", callback_data="prof_con"),
                 InlineKeyboardButton("Intelligence ST", callback_data="prof_int")],

                [InlineKeyboardButton("Arcana", callback_data="prof_arc"),
                 InlineKeyboardButton("History", callback_data="prof_his")],

                [InlineKeyboardButton("Investigation", callback_data="prof_inv"),
                 InlineKeyboardButton("Nature", callback_data="prof_nat")],

                [InlineKeyboardButton("Religion", callback_data="prof_rel"),
                 InlineKeyboardButton("Wisdom ST", callback_data="prof_wis")],

                [InlineKeyboardButton("Animal Handling", callback_data="prof_ani"),
                 InlineKeyboardButton("Insight", callback_data="prof_ins")],

                [InlineKeyboardButton("Medicine", callback_data="prof_med"),
                 InlineKeyboardButton("Perception", callback_data="prof_per")],

                [InlineKeyboardButton("Survival", callback_data="prof_sur"),
                 InlineKeyboardButton("✅ SAVE ✅", callback_data="prof_end")]]

    return keyboard


def keyboard_attack():
    keyboard = [[InlineKeyboardButton("Physical Attack  ⚔", callback_data="attack_1_weapon"),
                 InlineKeyboardButton("Cast a Spell  🪄", callback_data="attack_1_spell")]]

    return keyboard


def keyboard_attack_2(options, kind):
    keyboard = []

    for option in options:

        data = "attack_2_" + kind + "_" + option

        if keyboard == [] or len(keyboard[len(keyboard) - 1]) == 2:
            keyboard.append([InlineKeyboardButton(option.capitalize().replace("_", " "), callback_data=data)])
        else:
            keyboard[len(keyboard) - 1].append(InlineKeyboardButton(option.capitalize().replace("_", " "),
                                                                    callback_data=data))

    return keyboard


def keyboard_attack_ask1():

    keyboard = [[InlineKeyboardButton("One Hand", callback_data="attack_3_1"),
                 InlineKeyboardButton("Two Hands", callback_data="attack_3_2")]]

    return keyboard


def keyboard_attack_ask2(strength, dexterity):

    keyboard = [[InlineKeyboardButton("STR = "+str(strength), callback_data="attack_4_str"),
                 InlineKeyboardButton("DEX = "+str(dexterity), callback_data="attack_4_dex")]]

    return keyboard

