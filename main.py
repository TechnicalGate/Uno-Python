from Human import Human
from Bot import Bot
from TurnManager import TurnManager

turns = TurnManager()

bot = Bot('Bot',turns)
me = Human('You',turns)
turns.add(bot)
turns.add(me)
while True:
    turns.next_turn()
    if turns.winvar == True:
        break
print('Thanks for playing! Re-run this file to play again!')
