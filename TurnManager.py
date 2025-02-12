import random

class TurnManager:
    def __init__(self):
        self.deck = []
        self.shuffle_deck()

        while True:#make sure first card is not a power card
            self.before = self.deck[0]
            del self.deck[0]
            if type(self.before[1]) != str:#if not power card
                break
        
        self.turn_order = {}
        self.current = 0

        self.winvar = False

    def shuffle_deck(self):
        deck = []
        colors = ['r','b','g','y']
        nums = [1,2,3,4,5,6,7,8,9,0,'+2','skip','reverse']
        powers = ['wheel','+4']

        for c in colors:
            for n in nums:
                deck.append([c,n])
        for p in powers:
            deck.append(['p',p])

        random.shuffle(deck)

        try:
            for e in turns.turn_order:
                for c in e.hand:
                    deck.remove(c)
        except NameError:
            pass

        self.deck = deck

    def win(self,who):
        print(f'🏆 {who} wins!')
        self.winvar = True

    def add(self,entity):
        self.turn_order[entity] = True
        entity.draw(7)

    def inflict_effect(self,effect):
        #get the effects without targets out of the way
        if effect == 'reverse':
            self.turn_order = dict(reversed(list(self.turn_order.items())))
            return#dont need to go through the rest as the effect is done
        elif effect == 'wheel':
            return#dont need to go through the rest as the effect is done and handled in the Entity and Human or Bot code

        #effects that have a target
        #get target index (target being the next player)
        if self.current == len(self.turn_order)-1:
            target = 0
        else:
            target = self.current + 1
        #convert index into Entity in turn order so can call functions
        target = list(self.turn_order)[target]

        #apply effects
        if effect == 'skip':
            self.turn_order[target] = False
        elif effect == '+2':
            target.draw(2)
            print(target.name, 'has drawn 2 cards!')#so player can see something happened
        elif effect == '+4':
            target.draw(4)
        
    def next_turn(self):
        if self.current == len(self.turn_order)-1:
            self.current = 0
        else:
            self.current += 1

        target = list(self.turn_order)[self.current]
        #allows skip cards to work
        if self.turn_order[target]:
            target.turn()
        else:
            self.turn_order[target] = True
            self.next_turn()
