from blackjack import *
from unittest.mock import Mock

class TestBlackJack(object):

    def test_card(self):
        card = Mock()
        card.suit = 'hearts'
        assert card.suit == 'hearts'

    def test_deck(self):
        deck = Deck()
        assert len(deck.deck) == 52
        assert str(deck)

    def test_deal(self):
        deck = Mock()
        deck.deal = 'five of spades'
        assert deck.deal == 'five of spades'