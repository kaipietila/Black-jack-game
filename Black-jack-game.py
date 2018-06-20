class Card:
    import randint from random 
    '''
    This class defines the cards, deals a card and checks its validity
    '''
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def deal(self):
        '''
        generates a card with a random suit and a random value as dealing from a card deck
        '''
        self.suit = randint(0,4)
        self.value = randint(0,14)
        return (self.suit,self.value)

    def check_valid_card(self,card,player_hand,dealer_hand):
        '''
        checks if the card is already in the player or the dealers hand, if its in a hand then card is invalid
        '''
        if card in player_hand:
            return False
        elif card in dealer_hand:
            return False
        else:
            return True

    def card_actual_value(self,card)
        '''
        Gives the true value of the card. For cards 1-9 returns the value given. For 10,jack,queen,king returns value 10
        and for aces returns value 11.
        '''
        if self.value < 10:
            return self.value
        elif self.value >= 10 and < 14:
            return 10
        else:
            return 11

class Hand:

    def __init__(self):
        self.player_hand = []
        self.dealer_hand = []
    
    def add_to_hand(self,player_card):
        raise NotImplementedError

    def hand_value(self,hand_value):
        pass


    
class PlayerHand(Hand):

    def add_to_hand(self,player_card):
        if Card.check_valid_card(player_card, player_hand, dealer_hand):
            player_hand.append(player_card)
        else:
            return False

    
class DealerHand(Hand):

    def add_to_hand(self,dealer_card):
        if Card.check_valid_card(dealer_card, player_hand, dealer_hand):
            dealer_hand.append(dealer_card)
            return True
        else:
            return False



def playing_game():

    player_hand_value = 0
    dealer_hand_value = 0
    stop = False
    player_turn = True

    while stop is not True and card_value >= 21:
        if player_turn is True
            player_card = Card.deal()
            if PlayerHand.add_to_hand(player_card):
                player_hand_value += Card.card_actual_value(player_card)
                player_turn = False
            else:
                continue
        else:
            dealer_card = Card.deal()
            if DealerHand.add_to_hand(dealer_card):
                dealer_hand_value += Card.card_actual_value(dealer_card)
                player_turn = True
            else:
                continue
            
pass

    
