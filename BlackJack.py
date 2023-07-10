import random


def generate_deck(_suits, _cards):
    random.seed(0)
    n = 0
    deck = [(i, j) for i in _suits for j in _cards]
    random.shuffle(deck)
    while True:
        yield deck[n]
        n += 1
        if n == 52:
            random.shuffle(deck)
            n = 0


suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
shuffled_deck = generate_deck(suits, cards)


def get_next_card():
    return next(shuffled_deck)


sage_money = int(input("Sage’s money:"))
game_number = int(input("Number of games: "))


def card_values(tuple_given):
    if tuple_given[1] == "K":
        if tuple_given[0] == "Diamonds" or tuple_given[0] == "Hearts":
            return 1
        else:
            return 11
    elif tuple_given[1] == "J":
        return 10
    elif tuple_given[1] == "Q":
        return 10
    elif tuple_given[1] == "A":
        return 1
    else:
        return tuple_given[1]


for game in range(game_number):
    game = str(game + 1)
    print("Game " + game)
    sage_cards = [get_next_card(), get_next_card()]
    king_cards = [get_next_card(), get_next_card()]
    print("King's cards: (*)"+ str(king_cards[0]))
    print("Total value:", card_values(king_cards[0]))
    print("Sage's cards: " + str(sage_cards[0])+ str(sage_cards[1]))
    sage_value = int(card_values(sage_cards[0])) + int(card_values(sage_cards[1]))
    king_value = int(card_values(king_cards[0])) + int(card_values(king_cards[1]))
    print("Total value:",sage_value)
    while True:
        if sage_value < 21:
            hit_or_stop = input("Do you want to hit or stand? [H/S]\n")
            if hit_or_stop == "H":
                new_card = get_next_card()
                print("Sage's cards:", sage_cards[0], sage_cards[1], new_card)
                sage_value = sage_value + int(card_values(new_card))
                print("Total value:", sage_value)
            if hit_or_stop == "S":
                break
            else:
                pass
        elif sage_value == 21:
            print("It is Blackking! You won!")
            sage_money += 50
            break
        else:
            print("You busted! You lost!")
            sage_money += -50
            break
    while sage_value <= 21:
        if king_value < 21:
            if king_value < 17:
                new_card_king = get_next_card()
                king_value = king_value + int(card_values(new_card_king))
            else:
                break
        elif king_value > 21:
            print("King busted! You won!")
            sage_money += 50
            break
        else:
            break
    if sage_value < 21 and king_value <= 21:
        if king_value > sage_value:
            print("King has higher value. You lost!")
            sage_money -= 50
        elif sage_value > king_value:
            print("You have higher value. You won!")
            sage_money += 50
        elif sage_value == king_value:
            print("It is a tie!")
    else:
        pass
print("Final money is " + str(sage_money))