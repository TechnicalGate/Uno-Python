from Entity import Entity

class Human(Entity):
    def turn(self):
        card = self.choose_card()
        self.play(card)
    
    def display_cards(self):
        print(f'\nCurrent card on table: {self.tm.before}')
        print('\nYour Hand:')
        for n,i in enumerate(self.hand):
            print(f'({n}) {i}')
        print(f'({len(self.hand)}) draw another card')
        print('\nType " uno" after the card to say uno')
    
    def get_input(self,maxi,string):
        card = input(string)
        uno = False

        #check if said uno
        card = card.split(' ')
        try:
            _ = card[1]
            uno = True
        except:
            pass

        card = card[0]
        
        try:#format check
            card = int(card)
        except:
            return self.get_input(maxi,string)
        
        if card < 0 or card > maxi:#range check
            return self.get_input(maxi,string)

        return card,uno
        
    def choose_card(self):
        self.display_cards()
        #card
        card,uno = self.get_input(len(self.hand),'Play which card: ')
        print('')

        #if drawing a card
        if card == len(self.hand):
            #check if can draw card
            for i in self.hand:
                if i[0] == self.tm.before[0] or i[0] == 'p' or i[1] == self.tm.before[1]:
                    print('You still have playable cards, and cannot draw another card at this time.')
                    return self.choose_card()
            
            self.draw(1)
            return self.choose_card()

        #if playing a card
        card = self.hand[card]
        #check if card is legal
        card = self.card_check(card,uno)
        if card == False:#illegal card
            print('You cannot play this card at the moment')
            return self.choose_card()
        else:#legal card
            if len(self.hand) == 2:#if 1 card left after this card is played
                if uno == False:#if didnt say uno
                    print('You did not say uno, draw 2 cards.')
                    self.draw(2)
                    
            return card
    
    def choose_color(self):
        colors = ['r','g','b','y']
        for n,i in enumerate(colors):
            print(f'({n}) {i}')
        color = colors[self.get_input(3,'Which color: ')[0]]
        return color
