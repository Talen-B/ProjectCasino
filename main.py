from datetime import datetime
MIN_AGE = 18

toegangsticket = 5.00
gok_belasting = 2.50
drinken = 5.50
vaste_kosten = toegangsticket + gok_belasting + drinken
line_break = "-" * 25

naam = input("Wat is je naam?: ").title()
geboortedatum = input("Wat is je geboortedatum? Gebruik DD-MM-YYYY: ")

geboorte_dag, geboorte_maand, geboorte_jaar = geboortedatum.split("-")

if datetime.now().year - int(geboorte_jaar) < 18:
    exit("Je bent niet oud genoeg voor het casino!")

geslacht = input("Wat is je geslacht? Man, Vrouw of Anders: ").capitalize()
if geslacht == "Man":
    aanroep = "Meneer"
elif geslacht == "Vrouw":
    aanroep = "Mevrouw"
else:
    aanroep = ""
startbedrag = float(input("Wat is je startbedrag in € ").replace(",", "."))
saldo = startbedrag - vaste_kosten

print(f"""Casino de Gouden driehoek
{line_break}
Welkom, {aanroep} {naam}

Startbudget:    €{startbedrag:.2f}
Vaste Kosten:   €{vaste_kosten:.2f}
Saldo:          €{startbedrag - vaste_kosten:.2f}
{"Je hebt nog genoeg budget voor toegang tot het casino." if saldo > 0 else "Je budget is op! Laad meer op"}
Klik enter om door te gaan naar de roulettes!""")
input("")

# Opdracht 2
while True:
    print(f"""Casino de Gouden driehoek
{line_break}
Welkom bij roulettes! Kies uit de volgende opties:
 1 - Rood
 2 - Zwart
 3 - Even
 4 - Oneven
 0 - Stoppen met spelen""")
    roulette_keuze = int(input("Keuze: "))
    if int(roulette_keuze) == 0 :
        break
    #Roulette logica
    while True:
        inzet = input(f"Je saldo is € {saldo:.2f}\n0 om te annuleren\nWat is je inzet?: € ")
        if inzet.isdigit():
            inzet = int(inzet)
        else:
            print("Voer een geldig getal in")
            continue

        if inzet > int(saldo):
            print("Niet genoeg saldo.")
            continue

        round_number = 1
        color = ""
        odd_even = ""
        spin = (round_number * 7) % 37
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

        print(line_break)
        print(f"De bal valt op {color}, {odd_even} ({spin}).")
        if win:
            print(f"Je wint € {inzet:.2f}")
            saldo = saldo + inzet
            print(f"Je nieuwe saldo is: €{saldo:.2f}")
        else:
            print(f"Helaas, je verliest € {inzet:.2f}")
            saldo = saldo - inzet
            print(f"Je nieuwe saldo is: € {saldo:.2f}")
        round_number += 1
        input("Druk op enter om door te gaan:")
        break
