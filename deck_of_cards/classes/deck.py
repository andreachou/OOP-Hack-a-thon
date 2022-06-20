from classes import card
import random

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def pick_a_card(self):
        num = random.randint(1, 53)
        pick_card = self.cards[num]
        suit_card = pick_card.suit
        num_card = pick_card.point_val
        print(suit_card, num_card)
        return suit_card, num_card

# draw = Deck()
# draw.pick_a_card()