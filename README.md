# Uno-Python
## its uno in python

## How to play
To start the game, run main.py

## Customisation
Edit customisation section of main.py

To add another bot, type this:
bot = Bot('name',turns)
turns.add(bot)

To add another player (player allows human input, however there is no multiplayer), type this:
player = Human('name',turns)
turns.add(player)

## What the other files do
Entity.py contains the base class containing the functions both players and bots can use, E.g drawing cards, playing cards

Human,py contains the extra functions required for humans to play. E.g taking player inputs

Bot.py contains the extra functions required for bots to play. E.g choosing which card to play

## Why I made this
I was bored, wanted to code, and no one played uno with me
