import random

suits = ('hearts', 'diamonds', 'clubs', 'spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    '''
    This class defines the cards, deals a card and checks its validity
    '''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return (f'{self.rank} of {self.suit}')

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.deck.append(card)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)

class Hand:

    def __init__(self)
        self.cards = []  
        self.value = 0   
    
    def add_card(self,card):
        self.cards.append(card)
        if card.rank != 'Ace':
            self.value += card.value
        else:
            self.adjust_for_ace()
    
    def adjust_for_ace(self):
        if self.value <= 10:
            self.value += 11
        else:
            self.value += 1


class Wallet:
    '''
    A wallet to store and make the bets
    '''
    def __init__(self, amount=0):
        self.amount = amount

    def add_to_wallet(self, amount):
        self.amount += amount
        return self.amount
    
    def check_bet(self, bet_amount, win = False):
        if win:
            self.amount += bet_amount
            return self.amount
        else:
            self.amount -= bet_amount
            return self.amount
    
    def show_wallet(self):
        return self.amount

class Player:

    def __init__(self, wallet, hand):
        self.wallet = wallet
        self.hand = hand
    

def make_bet(self, wallet):
    bet_amount= int(input(f"How much would you like to bet? Your wallet contains {wallet.amount}.\n"))
    if bet_amount > wallet.amount:
        print("The bet was too large!")
        return False
    else:
        return bet_amount


def hit_card(deck, hand):
    card = deck.deal()
    hand.add_card(card)
       
def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    if playing:
        hit_card(deck, hand)

def show_some(player,dealer):
    print(f'Player hand value {player.value}')
    print (f'Dealer hand value {dealer.value - dealer.cards[0].value}')
    
def show_all(player,dealer):
    print (f'Player hand value {player.value}')
    print (f'Dealer hand value {dealer.value}')

def player_busts(player):
    if player.hand.value > 21:
        return True
    else:
        return False

def player_wins(player1, player2):
    if player2.hand.value < player1.hand.value <= 21:
        return True
    else:
        return False
    
def push():
    print("its a tie")


def playing_game():


    while 