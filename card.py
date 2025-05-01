class Card:
    def __init__(self):
        self.pin = "0123"
        # self.account = account # TODO move to account
        self.stolen_cards = [
            '4539 1488 0343 6467',  # Visa
            '4716 6210 1190 0496',  # Visa
            '4485 7162 2397 4351',  # Visa
            '5500 0000 0000 0004',  # MasterCard
            '5404 7203 1502 1991',  # MasterCard
            '2223 0000 4845 0010',  # MasterCard (new range)
            '3714 4963 5398 4315',  # Amex
            '3782 8224 6310 0055',  # Amex
            '3440 1234 5678 9501',  # Amex
            '6011 0009 9013 9424'  # Discover (extra)
        ]
        self.valid_cards = [
            '4556 7375 8689 9855',  # Visa
            '4532 4198 5027 2346',  # Visa
            '4916 1298 6381 7933',  # Visa
            '5289 1611 9602 0143',  # MasterCard
            '5342 6281 3977 7887',  # MasterCard
            '2224 0000 3234 0025',  # MasterCard (new range)
            '3787 3449 3671 0300',  # Amex
            '3711 8782 3110 0045',  # Amex
            '3491 5481 0365 4788',  # Amex
            '6011 0010 0492 0086'  # Discover (extra)
        ]

        self.correct_pin_code = '1234'

    def stolen_card(self, unknown_card):
        for stolen_card in self.stolen_cards:
            if stolen_card == unknown_card:
                return True
            else:
                return False

    def valid_card(self, unknown_card):
        for valid_card in unknown_card:
            if valid_card in self.valid_cards:
                return True
            else:
                return False

    def test_pin_code(self, pin_code):
        if pin_code == self.correct_pin_code:
            return True
        else:
            return False


