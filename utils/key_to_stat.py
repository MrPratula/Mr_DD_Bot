
def get_stat(choice):

    if choice == "str":
        main_stat = "strength"
        stat = "strength"
    elif choice == "str_sav":
        main_stat = "strength"
        stat = "strength_saving_throw"
    elif choice == "ath":
        main_stat = "strength"
        stat = "athletics"
    elif choice == "dex":
        main_stat = "dexterity"
        stat = "dexterity"
    elif choice == "dex_sav":
        main_stat = "dexterity"
        stat = "dexterity_saving_throw"
    elif choice == "acr":
        main_stat = "dexterity"
        stat = "acrobatics"
    elif choice == "sle":
        main_stat = "dexterity"
        stat = "sleight_of_hand"
    elif choice == "stl":
        main_stat = "dexterity"
        stat = "stealth"
    elif choice == "con":
        main_stat = "constitution"
        stat = "constitution"
    elif choice == "con_sav":
        main_stat = "constitution"
        stat = "constitution_saving_throw"
    elif choice == "int":
        main_stat = "intelligence"
        stat = "intelligence"
    elif choice == "int_sav":
        main_stat = "intelligence"
        stat = "intelligence_saving_throw"
    elif choice == "arc":
        main_stat = "intelligence"
        stat = "arcana"
    elif choice == "his":
        main_stat = "intelligence"
        stat = "history"
    elif choice == "inv":
        main_stat = "intelligence"
        stat = "investigation"
    elif choice == "nat":
        main_stat = "intelligence"
        stat = "nature"
    elif choice == "rel":
        main_stat = "intelligence"
        stat = "religion"
    elif choice == "wis":
        main_stat = "wisdom"
        stat = "wisdom"
    elif choice == "wis_sav":
        main_stat = "wisdom"
        stat = "wisdom_saving_throw"
    elif choice == "ani":
        main_stat = "wisdom"
        stat = "animal_handling"
    elif choice == "ins":
        main_stat = "wisdom"
        stat = "insight"
    elif choice == "med":
        main_stat = "wisdom"
        stat = "medicine"
    elif choice == "per":
        main_stat = "wisdom"
        stat = "perception"
    elif choice == "sur":
        main_stat = "wisdom"
        stat = "survival"
    elif choice == "cha":
        main_stat = "charisma"
        stat = "charisma"
    elif choice == "cha_sav":
        main_stat = "charisma"
        stat = "charisma_saving_throw"
    elif choice == "dec":
        main_stat = "charisma"
        stat = "deception"
    elif choice == "itm":
        main_stat = "charisma"
        stat = "intimidation"
    elif choice == "prf":
        main_stat = "charisma"
        stat = "performance"
    elif choice == "prs":
        main_stat = "charisma"
        stat = "persuasion"
    elif choice == "pro":
        main_stat = "proficiency"
        stat = "proficiency"
    else:
        main_stat = "end"
        stat = "end"

    return [stat, main_stat]


def stat_name(val):

    if val == 0:
        return "STR"
    elif val == 1:
        return "DEX"
    elif val == 2:
        return "CON"
    elif val == 3:
        return "INT"
    elif val == 4:
        return "WIS"
    elif val == 5:
        return "CHA"
    else:
        return "PRO"


def prof_name(pos):

    if pos == 0:
        return "strength_saving_throw"
    elif pos == 1:
        return "athletics"
    elif pos == 2:
        return "dexterity_saving_throw"
    elif pos == 3:
        return "acrobatics"
    elif pos == 4:
        return "sleight_of_hands"
    elif pos == 5:
        return "stealth"
    elif pos == 6:
        return "constitution_saving_throw"
    elif pos == 7:
        return "intelligence_saving_throw"
    elif pos == 8:
        return "arcana"
    elif pos == 9:
        return "history"
    elif pos == 10:
        return "investigation"
    elif pos == 11:
        return "nature"
    elif pos == 12:
        return "religion"
    elif pos == 13:
        return "wisdom_saving_throw"
    elif pos == 14:
        return "animal_handling"
    elif pos == 15:
        return "insight"
    elif pos == 16:
        return "medicine"
    elif pos == 17:
        return "perception"
    elif pos == 18:
        return "survival"
    elif pos == 19:
        return "charisma_saving_throw"
    elif pos == 20:
        return "deception"
    elif pos == 21:
        return "intimidation"
    elif pos == 22:
        return "performance"
    else:
        return "persuasion"
