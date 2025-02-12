from Entity import Entity

class Bot(Entity):
    def display(self):#test only
        print('hand: ')
        for i in self.hand:
            print(i)
        print('before: ',self.tm.before)
    
    def choose_card(self):
        for i in self.hand:
            if self.card_check(i,True):#assume bot is always saying uno
                return i

    def choose_color(self):
        colors = {'r':0,'g':0,'b':0,'y':0}
        #go through every card in hand to see which color it has the most of
        for i in self.hand:
            color = i[0]
            if color != 'p':
                colors[color] += 1
        #return most obtained color
        return max(colors, key=colors.get)
    
    def turn(self):
        print(f'{self.name} has {len(self.hand)} cards\n')
        card = self.choose_card()
        #keep drawing cards if there are no playable cards
        while card == None:
            card = self.choose_card()#see if playable card
            print(f'{self.name} has drawn a card')
            if card != None:
                break
            self.draw(1)
        #play card
        self.play(card)
