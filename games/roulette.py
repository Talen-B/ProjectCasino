LINE_BREAK = "-" * 25

def show_roulette_options():
    print(f"""Casino de Gouden driehoek
{LINE_BREAK}
Welkom bij roulettes! Kies uit de volgende opties:
 1 - Rood
 2 - Zwart
 3 - Even
 4 - Oneven
 0 - Stoppen met spelen""")

def determine_result(roulette_keuze, color, odd_even):
    win = False
    match roulette_keuze:
        case 1:
            if color == "Rood":
                win = True
        case 2:
            if color == "Zwart":
                win = True
        case 3:
            if odd_even == "Even":
                win = True
        case 4:
            if odd_even == "Oneven":
                win = True
    return win


def play_roulette(saldo):
    round_number = 1
    while True:
        show_roulette_options()

        roulette_keuze = int(input("Keuze: "))
        if roulette_keuze == 0 :
            break
        #Roulette logica
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

            color = ""
            odd_even = ""
            spin = (round_number * 7) % 37
            round_number += 1
            if spin <= 18:
                if spin % 2 == 0:
                    color = "Zwart"
                    odd_even = "Even"
                else:
                    color = "Rood"
                    odd_even = "Oneven"
            else:
                if spin % 2 == 0:
                    color = "Rood"
                    odd_even = "Even"
                else:
                    color = "Zwart"
                    odd_even = "Oneven"

            break

        win = determine_result(roulette_keuze, color, odd_even)
        print(LINE_BREAK)
        print(f"De bal valt op {color}, {odd_even} ({spin}).")
        if win:
            print(f"Je wint € {inzet:.2f}")
            saldo = saldo + inzet
            print(f"Je nieuwe saldo is: €{saldo:.2f}")
        else:
            print(f"Helaas, je verliest € {inzet:.2f}")
            saldo = saldo - inzet
            print(f"Je nieuwe saldo is: € {saldo:.2f}")
        input("Druk op enter om door te gaan:")
    return saldo