import random

suits = ('hearts', 'diamonds', 'clubs', 'spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
turns_playing = 0

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
    
    def __str__(self):
        deck_comp = ''  
        for card in self.deck:
            deck_comp += '\n '+card.__str__() 
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)

class Hand:

    def __init__(self):
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
    def __init__(self, amount=100):
        self.amount = amount
        self.bet_amount = 0

    def add_to_wallet(self, amount):
        self.amount += amount
        print("Your wallet now contains: ", self.amount)
    
    def check_bet(self, bet_amount, win = False):
        if win:
            self.amount += bet_amount
        else:
            self.amount -= bet_amount
    
    def show_wallet(self):
        print(f"Your wallet contains {self.amount} ")
'''
if I want to add class player for each player, but with two you dont really need it
class Player:

    def __init__(self, wallet, hand):
        self.wallet = wallet
        self.hand = hand
'''
    

def make_bet(wallet):
    while True:
        try:
            bet_amount= int(input(f"How much would you like to bet? You wallet contains {wallet.amount}\n"))
            return bet_amount
        except:
            ValueError("not a valid amount!")
        else:
            if bet_amount > wallet.amount:
                print("The bet was too large!")
            else:
                break


def hit_card(deck, hand):
    card = deck.deal()
    hand.add_card(card)
       
def hit_or_stand(deck, hand):
    global playing
    while True: 
        player_input = input("Do you want to hit or to stand? h/s ")
        if player_input is "h":
            hit_card(deck, hand)
            show_some(player_hand, dealer_hand)
            if player_busts(player_hand):
                print("player has busted!")
                playing = False
            else:
                continue
        elif player_input is "s":
            playing = False
            print("player stands, dealers turn! ")
        else:
            print("do not understand!")
            continue
        break


def show_some(player,dealer):
    print("\nPlayer's Hand: ", *player.cards, sep = "\n")
    print(f"Player hand has a value of {player_hand.value}")
    print ("\nDealer's Hand:\n First card hidden\n", dealer.cards[1])
    
def show_all(player,dealer):
    print ("\nPlayer's Hand", *player.cards, sep = "\n")
    print ("Value: ", player.value)
    print ("\nDealer's Hand: ", *dealer.cards, sep = "\n")
    print ("Value: " , dealer.value)

def player_busts(player):
    if player_hand.value > 21:
        return True
    else:
        return False

def dealer_busts(dealer):
    if dealer_hand.value > 21:
        return True
    else:
        return False

def player_wins(player, dealer):
    if dealer_hand.value < player_hand.value <= 21:
        return True
    else:
        return False
def dealer_wins(player, dealer):
    if player_hand.value < dealer_hand.value <= 21:
        return True
    else:
        return False
    
def push():
    print("its a tie")




while True:
    deck = Deck()
    if turns_playing == 0:
        wallet = Wallet()
    bet_amount = 0
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    bet_amount = make_bet(wallet)
    show_some(player_hand, dealer_hand)
    win = False
    while playing:
        hit_or_stand(deck,player_hand)

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit_card(deck, dealer_hand)
        else:
            show_all(player_hand,dealer_hand)
            if dealer_busts(dealer_hand):
                win = True
                print(" Dealer busts and player wins!")
            elif player_wins(player_hand, dealer_hand):
                win = True
                print("player wins!")
            elif dealer_wins(player_hand, dealer_hand):
                print("dealer wins!")
            else:
                push()
    
    if win:
        wallet.check_bet(bet_amount, True)
        wallet.show_wallet()
    else:
        wallet.check_bet(bet_amount, False)
        wallet.show_wallet()
    
    new_game = input("Do you want to play again? y/n ")

    if new_game is "y":
        playing = True
        turns_playing += 1
        continue
    else:
        print("Thanks for playing!")
        break



        


