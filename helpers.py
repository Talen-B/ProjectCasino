LINE_BREAK = "-" * 25
def show_title(name):
    print(f"""Casino de Gouden driehoek | {name}
{LINE_BREAK}""")

def input_bet(saldo):
    while True:
        inzet = int(input(f"Je saldo is € {saldo:.2f}\n0 om te annuleren\nWat is je inzet?: € "))
        if inzet == 0:
            break
        elif inzet > saldo:
            print("Niet genoeg saldo.")
            continue
        elif inzet > 0:
            return inzet
        else:
            print("Voer een geldig getal in")
            continue

    return inzet