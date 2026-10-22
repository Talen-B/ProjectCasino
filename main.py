from datetime import datetime

from games.blackjack import play_blackjack
from games.fruitmachine import play_fruitmachine
from games.roulette import play_roulette

MIN_AGE = 18
TOEGANGSTICKET = 5.00
GOK_BELASTING = 2.50
DRINKEN = 5.50
VASTE_KOSTEN = TOEGANGSTICKET + GOK_BELASTING + DRINKEN
LINE_BREAK = "-" * 25

def show_main_menu():
    print(f"""Casino de Gouden driehoek
{LINE_BREAK}
 1 - Spellen
 2 - Saldo
 3 - Account
 0 - Stop""")

def show_welcome_message(naam, aanhef, startbedrag, saldo):
    print(f"""Casino de Gouden driehoek
{LINE_BREAK}
Welkom, {aanhef} {naam}

Startbudget:    €{startbedrag:.2f}
Vaste Kosten:   €{VASTE_KOSTEN:.2f}
Saldo:          €{startbedrag - VASTE_KOSTEN:.2f}
{"Je hebt nog genoeg budget voor toegang tot het casino." if saldo > 0 else "Je budget is op! Laad meer op"}""")
    input("Druk enter om door te gaan:")

def calc_age(geboortedatum):
    geboorte_dag, geboorte_maand, geboorte_jaar = geboortedatum.split("-")
    return datetime.now().year - int(geboorte_jaar)

def show_games_menu():
    print(f"""Casino de Gouden driehoek
{LINE_BREAK}
 1 - Roulettes
 2 - Fruitmachine
 3 - Blackjack
 0 - Terug""")

def show_saldo(saldo):
    print(f"""Casino de Gouden driehoek
{LINE_BREAK}
Je huidide saldo is € {saldo}""")
    input("Druk enter om door te gaan:")

def show_account(naam, geboortedatum, aanhef):
    print(f"""Casino de Gouden driehoek
{LINE_BREAK}
 Naam: {naam}
 Aanhef: {aanhef}
 Geboortedatum: {geboortedatum}
 Leeftijd: {calc_age(geboortedatum)}""")
    input("Druk enter om door te gaan:")

def bepaal_aanhef(geslacht):
    if geslacht == "Man":
        aanhef = "Meneer"
    elif geslacht == "Vrouw":
        aanhef = "Mevrouw"
    else:
        aanhef = ""
    return aanhef


def check_age(geboortedatum):
    leeftijd = calc_age(geboortedatum)
    if leeftijd < MIN_AGE:
        exit("Je bent niet oud genoeg voor het casino!")
    else:
        return leeftijd


def main():
    naam = input("Wat is je naam?: ").title()
    geboortedatum = input("Wat is je geboortedatum? Gebruik DD-MM-YYYY: ")
    check_age(geboortedatum)
    aanhef = bepaal_aanhef(input("Wat is je geslacht? Man, Vrouw of Anders: ").capitalize())
    startbedrag = float(input("Wat is je startbedrag in € ").replace(",", "."))
    saldo = startbedrag - VASTE_KOSTEN

    show_welcome_message(naam, aanhef, startbedrag, saldo)
    while True:
        show_main_menu()
        main_input = int(input("Keuze: "))
        match main_input:
            case 1:
                show_games_menu()
                games_input = int(input("Keuze: "))
                match games_input:
                    case 1:
                        saldo = play_roulette(saldo)
                    case 2:
                        saldo = play_fruitmachine(saldo)
                    case 3:
                        saldo = play_blackjack(saldo)
            case 2:
                show_saldo(saldo)
            case 3:
                show_account(naam, geboortedatum, aanhef)

main()