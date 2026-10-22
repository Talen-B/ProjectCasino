import random

from helpers import *

SUITS = {"♠", "♥", "♦", "♣"}
RANKS = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"}
LOSS = 0
DRAW = 1
WIN = 2
DEALER_BUST = 3
player_hand = []
dealer_hand = []

def create_deck():
    deck = [f"{suit}{rank}"for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck

def draw_card_player(deck):
    if not player_hand:
        player_hand.extend([deck.pop(0), deck.pop(0)])
    else:
        player_hand.extend([deck.pop(0)])

def draw_card_dealer(deck):
    if not dealer_hand:
        dealer_hand.extend([deck.pop(0), deck.pop(0)])
    else:
        dealer_hand.extend([deck.pop(0)])

def calc_value(hand):
    value = 0
    aces = 0
    for card in hand:
        if card[1:] in ("J", "Q", "K"):
            value += 10
        elif card[1:] == "A":
            value += 11
            aces += 1
        else:
            value += int(card[1:])
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1

    return value

def show_player_hand():
    print("Jouw hand:", " | ".join(player_hand), f"\nJouw totaal: {calc_value(player_hand)}")

def show_dealer_hand():
    print("Dealer hand:", " | ".join(dealer_hand))

def determine_result(result, saldo, inzet):
    match result:
        case 0: #LOSS
            print("Helaas je hebt niet gewonnen.")
            saldo -= inzet
            return saldo
        case 1: #DRAW
            print("Gelijkspel! Je krijgt je inzet terug")
            return saldo
        case 2: #WIN
            print(f"Je wint van de dealer! Je wint €{inzet*0.5}")
            saldo += inzet * 0.5
            return saldo
        case 3: #DEALER_BUST
            print(f"De dealer heeft teveel! Je wint €{inzet}")
            saldo += inzet
            return saldo
    return None

def calc_result():
    player_score = calc_value(player_hand)
    dealer_score = calc_value(dealer_hand)
    if player_score > dealer_score:
        return WIN
    elif player_score == dealer_score:
        return DRAW
    else:
        return LOSS

def play_turn(deck):
    result = None
    while True:
        hit_stand = input("Kies hit of stand: ")
        if hit_stand == "hit":
            draw_card_player(deck)
            show_player_hand()
            if calc_value(player_hand) > 21:
                result = LOSS
                return result
        else:
            break
    while calc_value(dealer_hand) < 17:
        show_dealer_hand()
        draw_card_dealer(deck)
        print(f"De dealer trekt: {dealer_hand[-1]}")
        show_dealer_hand()
        if calc_value(dealer_hand) > 21:
            result = DEALER_BUST
            return result
    if result is None:
        result = calc_result()

    return result

def show_result():
    print(f"""===Resultaat===
Jouw score: {calc_value(player_hand)}
Dealer score: {calc_value(dealer_hand)}
""")

def play_blackjack(saldo):
    while True:
        show_title("Blackjack")
        inzet = input_bet(saldo)
        if inzet == 0:
            break

        player_hand.clear()
        dealer_hand.clear()

        deck = create_deck()
        draw_card_player(deck)
        draw_card_dealer(deck)
        show_player_hand()

        print(f"Dealer toont: {dealer_hand[0]} | ??")
        result = play_turn(deck)

        show_result()
        saldo = determine_result(result, saldo, inzet)
        print(f"Je nieuwe saldo is: € {saldo}")
        game_end = int(input("Kies 1 om opnieuw te spelen of 0 om af te sluiten\nKeuze: "))
        if game_end == 1:
            play_blackjack(saldo)

    return saldo
