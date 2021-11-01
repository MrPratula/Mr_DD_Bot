# Progetto di Ingegneria Informatica
Lorenzo Prada   10529212    869775

# Mr_DD_Bot
Mr D&D Bot is a Telegram bot which can help a group of friends to play Dungeons and Dragons. It can handle the characters' sheet, manage the die rolls and more.

## Introduction
Mr D&D Bot is implemented using the [python-telegram-bot](https://python-telegram-bot.readthedocs.io/en/latest/index.html?highlight=examples) library.
The Bot is entirely developed in Python.
The persistance is guaranteed by a SQL database and some configuration files.

### Configuration Files

In order to use this Bot, a folder named "files" must be created inside the Mr_DD_Bot folder. It must contain the following files:
- key.txt
- dbAccessData.json

###### key.txt
This file must contain only the Bot Key.

###### dbAccessData.json
This file contains the data for the database connection. It has to be a dictionary with these keys:

```
"host": "my_host",
"user": "my_user",
"password": "my_secret_password",
"database": "my_database_name"
```
Inside the database folder there is the database structure.

### Functions

Mr D&D Bot can respond to the following commands:

- /start
- /help

- /new
- /char
- /prof
- /life
- /cfg
- /class

- /lang
- /dm

- /roll
- /check
- /attack

### Intro Functions
#### /start
/start provides a short intro about the bot, that registers the user into the database.
#### /help
/help provides a list of all the commands, with a short description.

### Character management functions
Those functions are needed to manage all user's characters. When a character is created, a user should use all of these functions to set the character up properly.
#### /new
Allows a user to create a new character.
#### /char
This shows all the user's characters. He can set an active character, which will become the character used to make all the other functions, edit one of his characters or delete some of them.
#### /prof
Allows a user to set his active character's proficiency.
#### /cfg
Used to set which spells a character know or which weapons he has.
#### /class
Used to specify character's class.

#### /lang
Change bot global language. Right now English, Italian and Espanol are available.
#### /dm
Set a user as DM or not. This may be usefull for further function not implemented yet.

### In-Game Functions
This functions should be used in-game.
#### /roll
Roll a die. User can choose if roll a d4, d6, d8, d10, d12 or a d20.
#### /check
Make an ability check with active character. Character's proficiency are considered too.
#### /attack
Allow a user to cast a spell or make an attack with his active character. If a character casts a spell the user has to choose beethween the spells the character know, then the Spell Save DC, the spell Attack or the spell Attack damage are calculated.
If a character attacks, the user has to choose a weapon the character own and then, based on the weapon, choose the proper option for finesse, or versatile weapons. 
Then the Attack and the Attack damage are calculated.
#### /life
Allow a user to edit his active character life points.

### NOTE
All rolls have a main roll and an Advantage/Disadvantage roll. You have to always consider the first roll, then if you have advantage consider the second and choose the highest value, if you have disadvantage consider the second and choose the lowest one.
