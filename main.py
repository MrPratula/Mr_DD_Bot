
import logging

from bot.start import start
from bot.help import help
from bot.character import character, char_view_button, char_active_button, char_edit_button, char_delete_button, \
                            char_stat_button, char_close
from utils.conversation_handler import new_char_handler
from bot.dm import dm
from bot.roll import roll, button_roll
from bot.check import check, first_check_button, second_check_button
from bot.proficiency import proficiency, proficiency_button
from bot.attack import attack, attack_choose_weapon_spell, make_attack_button, cast_spell_button, \
                        finesse_attack_button, versatile_attack_button
from bot.lang import language, language_button
from bot.life import life, life_button
from bot.config import config, config_first_button, config_spell_button, config_weap_button
from bot.char_class import char_class, class_select

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

if __name__ == '__main__':

    try:
        with open("files/key.txt", "r") as fKey:
            key = fKey.readline()
    except FileNotFoundError:
        print("can't open key.txt file")
        exit(1)

    updater = Updater(token=key, use_context=True)
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('char', character))
    dispatcher.add_handler(CommandHandler('dm', dm))
    dispatcher.add_handler(CommandHandler('roll', roll))
    dispatcher.add_handler(CommandHandler('check', check))
    dispatcher.add_handler(CommandHandler('prof', proficiency))
    dispatcher.add_handler(CommandHandler('attack', attack))
    dispatcher.add_handler(CommandHandler('lang', language))
    dispatcher.add_handler(CommandHandler('life', life))
    dispatcher.add_handler(CommandHandler('cfg', config))
    dispatcher.add_handler(CommandHandler('class', char_class))

    dispatcher.add_handler(CallbackQueryHandler(button_roll, pattern="^d_.*$"))

    dispatcher.add_handler(CallbackQueryHandler(char_view_button, pattern="^char_view.*$"))
    dispatcher.add_handler(CallbackQueryHandler(char_active_button, pattern="^char_active.*$"))
    dispatcher.add_handler(CallbackQueryHandler(char_edit_button, pattern="^char_edit.*$"))
    dispatcher.add_handler(CallbackQueryHandler(char_stat_button, pattern="^char_stat.*$"))
    dispatcher.add_handler(CallbackQueryHandler(char_close, pattern="^char_close.*$"))
    dispatcher.add_handler(CallbackQueryHandler(char_delete_button, pattern="^char_delete.*$"))

    dispatcher.add_handler(CallbackQueryHandler(first_check_button, pattern="^check1_.*$"))
    dispatcher.add_handler(CallbackQueryHandler(second_check_button, pattern="^check2_.*$"))

    dispatcher.add_handler(CallbackQueryHandler(proficiency_button, pattern="^prof_.*$"))

    dispatcher.add_handler(CallbackQueryHandler(attack_choose_weapon_spell, pattern="attack_1_.*$"))
    dispatcher.add_handler(CallbackQueryHandler(make_attack_button, pattern="^attack_2_weapon_.*$"))
    dispatcher.add_handler(CallbackQueryHandler(versatile_attack_button, pattern="^attack_3_.*$"))
    dispatcher.add_handler(CallbackQueryHandler(finesse_attack_button, pattern="^attack_4_.*$"))

    dispatcher.add_handler(CallbackQueryHandler(cast_spell_button, pattern="^attack_2_spell_.*$"))

    dispatcher.add_handler(CallbackQueryHandler(language_button, pattern="^lang_.*$"))

    dispatcher.add_handler(CallbackQueryHandler(life_button, pattern="^life_.*$"))

    dispatcher.add_handler(CallbackQueryHandler(config_first_button, pattern="^config_1_.*$"))
    dispatcher.add_handler(CallbackQueryHandler(config_weap_button, pattern="^config_2_weap_.*$"))
    dispatcher.add_handler(CallbackQueryHandler(config_spell_button, pattern="^config_2_spell_.*$"))

    dispatcher.add_handler(CallbackQueryHandler(class_select, pattern="^class_.*$"))

    dispatcher.add_handler(new_char_handler)    # /new

    updater.start_polling()

    print("bot online")
