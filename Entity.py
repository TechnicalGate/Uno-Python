class Entity():
    def __init__(self,name,tm):
        self.name = name
        self.hand = []
        self.tm = tm

    def draw(self,amount):
        for i in range(amount):
            try:#if there are enough cards
                self.hand.append(self.tm.deck[0])
                del self.tm.deck[0]
            except IndexError:
                #reshuffle deck
                self.tm.shuffle_deck()

    def wincheck(self):
        if len(self.hand) == 0:
            self.tm.win(self.name)

    def turn(self):
        pass#replace with human/bot logic in Human or Bot class

    def choose_card(self):
        pass#replace with human/bot logic in Human or Bot class

    def choose_color(self):
        pass#replace with human/bot logic in Human or Bot class

    def card_check(self,card,uno):
        #power cards legal
        if card[0] == 'p':
            return card
        #check if same color
        if card[0] == self.tm.before[0]:
            return card
        #check if same number
        if card[1] == self.tm.before[1]:
            return card
        
        return False

    def play(self,card):
       fx = None
       print(f'{self.name} has played {card}')

       #play card
       self.tm.before = card
       self.hand.remove(card)
       #check if 0 cards after playing
       self.wincheck()

        #check if its a power
       if type(card[1]) == str:
           fx = card[1]
           
           #if card requires color choosing
           if fx == '+4' or fx == 'wheel':
               #reassign color of before
               self.tm.before[0] = self.choose_color()

           self.tm.inflict_effect(fx)
    
