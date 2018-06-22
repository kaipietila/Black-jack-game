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
            print("card is not in any hand")
            print(card)
            return True

    def card_actual_value(self):
        '''
        Gives the true value of the card. For cards 1-9 returns the value given. For 10,jack,queen,king returns value 10
        and for aces returns value 11.
        '''
        if self.value < 10:
            print(self.value)
            return self.value
        elif self.value >= 10 and self.value < 14:
            print(10)
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


def hit_card(player_card, player_hand, dealer_hand):
    if card.check_valid_card(player_card, player_hand, dealer_hand):
        player_hand.append(player_card)
        player_turn = False
        player_hand_value += card.card_actual_value()
        card_count += 1
    

def win_check():
    '''
    To check if the player_hand_value is 21 or over and then to compare that to the dealer_hand_value.
    If player_hand_value is below 21 the dealer will draw cards until same or over player_hand_value. 
    If dealer_hand_value exceeds 21 the player wins.
    '''
    pass

def playing_game():

    player_hand = []
    dealer_hand = []
    player_hand_value = 0
    dealer_hand_value = 0
    game_end = False
    stop = False
    player_turn = True
    card_count = 0
    '''
    Need to make a new def called deal_card that uses classes and deals one call on demand. since the game
    logic goes two cards to both and then the player gets to choose hit or stop until he stops.another while loop until stop
    '''

    while game_end is not True:
        if player_turn:
            card = Card()
            player_card = card.deal()
            hit_card(player_card, player_hand, dealer_hand)
            elif card_count >= 4:
                choice = input("Do you want to hit or stop? ") 
                if choice is "hit":
                    continue
                else:

            else:
                continue
        else:
            card = Card()
            dealer_card = card.deal()
            if card.check_valid_card(dealer_card, player_hand, dealer_hand):
                dealer_hand.append(dealer_card)
                player_turn = True
                dealer_hand_value += card.card_actual_value()
                card_count += 1
'''        
if __name__ == "__main__":
    playing_game()
'''

player_hand = []
dealer_hand = []

card = Card()
assigned_card = card.deal()
card.card_actual_value()
card.check_valid_card(assigned_card, player_hand, dealer_hand)



