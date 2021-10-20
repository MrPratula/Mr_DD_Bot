from telegram.ext import ConversationHandler, Filters, CommandHandler, MessageHandler

from bot.new import (
    new,
    name,
    strength,
    dexterity,
    constitution,
    intelligence,
    wisdom,
    charisma,
    proficiency,
    cancel
)

NAME, STR, DEX, CON, INT, WIS, CHA, PRO = range(8)


new_char_handler = ConversationHandler(

        entry_points=[CommandHandler('new', new)],

        states={

            NAME: [MessageHandler(Filters.text & ~Filters.command, name)],
            STR: [MessageHandler(Filters.text & ~Filters.command, strength)],
            DEX: [MessageHandler(Filters.text & ~Filters.command, dexterity)],
            CON: [MessageHandler(Filters.text & ~Filters.command, constitution)],
            INT: [MessageHandler(Filters.text & ~Filters.command, intelligence)],
            WIS: [MessageHandler(Filters.text & ~Filters.command, wisdom)],
            CHA: [MessageHandler(Filters.text & ~Filters.command, charisma)],
            PRO: [MessageHandler(Filters.text & ~Filters.command, proficiency)],
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )
