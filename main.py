from Human import Human
from Bot import Bot
from TurnManager import TurnManager

turns = TurnManager()

#===CUSTOMISATION SECTION===
bot = Bot('Bot',turns)
me = Human('You',turns)
turns.add(bot)
turns.add(me)
#===END OF CUSTOMISATION SECTION===

while True:
    turns.next_turn()
    if turns.winvar == True:
        break
print('Thanks for playing! Re-run this file to play again!')
