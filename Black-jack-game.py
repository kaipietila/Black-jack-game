class Card:
    '''
    This class defines the cards, deals a card and checks its validity
    '''
    def __init__(self,suit=0,value=0):
        self.suit = suit
        self.value = value

    def deal(self):
        from random import randint  
        '''
        generates a card with a random suit and a random value as dealing from a card deck
        '''
        self.suit = randint(1,4)
        self.value = randint(1,14)
        print(self.suit,self.value)
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

    def card_actual_value(self):
        '''
        Gives the true value of the card. For cards 1-9 returns the value given. For 10,jack,queen,king returns value 10
        and for aces returns value 11.
        '''
        if self.value < 10:
            return self.value
        elif self.value >= 10 and self.value < 14:
            return 10
        else:
            return 11


class Wallet:
    '''
    A wallet to store and make the bets
    '''
    def __init__(self, amount=0):
        self.amount = amount

    def add_to_wallet(self, amount):
        self.amount += amount
        return self.amount
    
    def make_bet(self):
        bet_amount= int(input(f"How much would you like to bet? Your wallet contains {self.amount}.\n"))
        if bet_amount > self.amount:
            print("The bet was too large!")
            return False
        else:
            return bet_amount
    
    def check_bet(self, bet_amount, win = False):
        if win:
            self.amount += bet_amount
            return self.amount
        else:
            self.amount -= bet_amount
            return self.amount
    
    def show_wallet(self):
        return self.amount

def playing_game():

    player_hand = []
    dealer_hand = []
    player_hand_value = 0
    dealer_hand_value = 0
    stop = False
    player_turn = True
    pass

wallet1 = Wallet()
wallet1.add_to_wallet(500)
if wallet1.make_bet():
    x = wallet1.make_bet()
else:
    x = 0
y = wallet1.check_bet(x,True)
print(y)


