
import random
import os
import sys

print("Žaidimas \"Kas, Kur, Kada\" \n")

def zaidimas():
    print("Ką norėtumėte veikti: ")
    print("1. Žaisti žaidimą? Parašykite Z ir spauskite Enter.")
    print("2. Peržiūrėti ankstesnių žaidimų rezultatus? Parašykite R ir spauskite Enter.")
    print("3. Ištrinti buvusių žaidimų istoriją? Parašykite T ir spauskite Enter.")
    print("4. Išeiti iš žaidimo? Parašykite Q ir spauskite Enter")
    x = input("\nJūsų pasirinkimas? ")
    print(" ")
    if x == "z" or x == "Z" or x == "1":
        def kartot():
            print("Parašykite atsakymus į klausimus ir spauskite \"Enter\"! \n")
            Kada = input("Kada? ")
            a = ("Afrikoje", "Šiaurės ašigalyje", "didžiausiam pasaulio užpakalyje", "geriau neklausk kur", "Nikaragvoje", "Pabezdūnų kaime", "Sėdmaišių karalystėje", "senos raganos trobelėje", "svečiuose pas Talibaną", "Putino bunkeryje", "pragare", "srutų duobėje")
            Kur = random.choice(a)
            Kas = input("Kas? ")
            b = ("Vaivorykštiniu vienaragiu", "jo didenybe Radžiu", "tavo motina", "Nitanu Gauseda", "mažuoju Hitleriu Gražuliu", "bomžu", "Daukantu", "Olegu", "visų ertmių gydytoju", "žmogumi šaldytuvu", "Voodoo lėle")
            Su_kuo = random.choice(b)
            c = ("medžioja", "patruliuoja", "hipnotizuoja", "operuoja", "galvoja", "ovuliuoja", "svajoja apie", "klaidžioja po", "myli", "draugiškai nekenčia", "tiesiog stovi", "apsimeta pavasariu")
            Ka_veikia = random.choice(c)
            Ka = input("Ką? ")
            print(" ")
            txt ="{}, {} {} su {} {} {} \n"
            print(txt.format(Kada, Kur, Kas, Su_kuo, Ka_veikia, Ka))
            failas = open("Zaidimo_istorija.txt", "a", encoding='utf-8-sig')
            failas.write(txt.format(Kada, Kur, Kas, Su_kuo, Ka_veikia, Ka))
            failas.close()
            print(" ")
            return zaidimas()
        kartot()
    elif x == "r" or x == "R" or x == "2":
        def istorija():
            if os.path.isfile("Zaidimo_istorija.txt"):
                with open("Zaidimo_istorija.txt", encoding='utf-8-sig') as file:
                    failas = file.read()
                    print(failas) 
                    print(" ")
                    return zaidimas()
            else:
                print("Žaidimo istorija neegzistuoja, Jūs, greičiausiai, dar nežaidėte nei vieno žaidimo. \n")
                return zaidimas()
        istorija()
    elif x == "t" or x == "T" or x == "3":
        def istrint():
            try:
                if os.path.isfile("Zaidimo_istorija.txt"):
                    os.remove("Zaidimo_istorija.txt")
                    print("Žaidimo istorija sėkmingai ištrinta! \n")
                    return zaidimas()
            except OSError as error:
                    print("Ištrinti žaidimo istorijos nepavyko, pabandykite perkrauti savo kompiuterį. Gerai, gerai, juokauju! \n")
                    print("O jei rimtai, tai failo trynimo funkcija neveikia, jei prieš tai būni paleidęs failo perskaitymo funkciją. Nes Windowsai kažkodėl palieka failą atidarytą atmintyje, nors kodas ir sako, uždaryti failą po perskaitymo \n")
                    return zaidimas()
            else:
                print("Žaidimo istorija neegzistuoja, Jūs, greičiausiai, dar nežaidėte nei vieno žaidimo. \n")
                return zaidimas()
        istrint()
    elif x == "q" or x == "Q" or x == "5":
        def quit():
            sys.exit()
    else:
        print("Jūs, Ponas(-ia), nemokate rašyti ! ! ! \n")
        return zaidimas()
zaidimas()