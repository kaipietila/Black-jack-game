from black_jack_game import *

class TestClasses(object):

    def test_card(self):
        card = Card('hearts', 5)
        assert print(card) == "5 of hearts"