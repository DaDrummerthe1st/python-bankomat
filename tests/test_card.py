import pytest

from card import Card

@pytest.fixture # annotation
def test_cards():
    # define variables
    card = Card()  # TODO move acccount to account-class
    unknown_valid_card = card.valid_cards[0]
    unknown_invalid_card = '123456789'
    unknown_stolen_card = card.stolen_cards[0]


def card_valid(test_cards)
    # testmethods
    valid_ok = card.valid_card(unknown_valid_card)
    valid_bad = card.valid_card(unknown_invalid_card)
    stolen_card = card.stolen_card(unknown_stolen_card)
    # assertions
    assert valid_ok == True
    assert valid_bad == False
    assert stolen_card == True

def test_pin_code(test_cards, pincode='0123'):


