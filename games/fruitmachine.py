from random import random
LINE_BREAK = "-" * 25

#TODO
def show_fruitmachine_options():
    print(LINE_BREAK)
    print("""Welkom bij de Fruitmachine!
Zet een inzet in en spin to win!""")

def assign_slot_value():
    while True:
        random_value = random()

        if random_value <= 0.333:
            return "Ster"
        elif random_value <= 0.666:
            return "Maan"
        else:
            return "Zon"

def determine_result(slot1, slot2, slot3):
    win = False
    if slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
        win = True
    elif slot1 == slot2 == slot3:
        win = "Jackpot"
    return win


def play_fruitmachine(saldo):
    while True:
        show_fruitmachine_options()
        menu_input = input("Druk op enter om door te gaan of 0 om te annuleren: ")
        if menu_input == "0":
            break
        while True:
            inzet = input(f"Je saldo is € {saldo:.2f}\n0 om te annuleren\nWat is je inzet?: € ")
            if inzet.isdigit():
                inzet = int(inzet)
            else:
                print("Voer een geldig getal in")
                continue
            if inzet == 0:
                continue

            if inzet > int(saldo):
                print("Niet genoeg saldo.")
                continue
            slot1 = assign_slot_value()
            slot2 = assign_slot_value()
            slot3 = assign_slot_value()

            win = determine_result(slot1, slot2, slot3)
            print(LINE_BREAK)
            print(f"Rollen: {slot1} | {slot2} | {slot3}")
            if win:
                print(f"Je wint € {inzet:.2f}")
                saldo = saldo + inzet
                print(f"Je nieuwe saldo is: €{saldo:.2f}")
            elif win == "Jackpot":
                print(f"Je wint de jackpot!! € {inzet:.2f}")
                saldo = saldo + (inzet*3)
                print(f"Je nieuwe saldo is: €{saldo:.2f}")
            else:
                print(f"Helaas, je verliest € {inzet:.2f}")
                saldo = saldo - inzet
                print(f"Je nieuwe saldo is: € {saldo:.2f}")
            input("Druk op enter om door te gaan: ")
            continue

