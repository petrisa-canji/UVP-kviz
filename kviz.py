import json #sprememba python data string v json data string
import random #random number generator
import getpass #bere userinput, dokler user ne pritisne pass

uporabnik = []

def igra():
    print("\n ======== ZAČNI KVIZ ========")
    tocke = 0
    with open("vprasanja.json", 'r+') as f: #'r+' pomeni for reading and writing

        j = json.load(f)

        for i in range(10):
            stevilo_vprasanj = len(j)
            ch = random.randint(0, stevilo_vprasanj - 1)
            print(f'\nQ{i + 1} {j[ch]["vprašanje"]}\n') #\n je new line

            for option in j[ch]["options"]:
                print(option)
            odgovor = input("\n Odgovor:")

            if j[ch]["odgovor"][0] == odgovor[0].upper():
                print("\n Pravilno!")
                tocke += 1
            else:
                print("\nNarobe...")
            
            del j[ch]
        
        print(f'\n KONČNI REZULTAT: {tocke}') #f replaces the expressions with their values


def vprasanja_kviza():
    if len(uporabnik) == 0:
        print("Preden lahko dodajate vprašanja, se morate prijaviti!")
    
    elif len(uporabnik) == 2:
        if uporabnik[1] == "ADMIN":
            print('\n ======== DODAJ VPRAŠANJA ========')
            vpr = input("Dodaj želeno vprašanje, Jedi Master: \n")
            opt = []
            print("Dodaj 3 možnosti odgovora, ki jih poimenuj (A, B, C)")
            for _ in range(3):
                opt.append(input())
            odg = input("Dodaj vprašanje: \n")

            with open("vprasanja.json", 'r+') as f:
                vprasanja = json.load(f)
                dic = {"vprašanje": vpr, "možnosti": opt, "odgovor": odg}
                vprasanja.append(dic)
                f.seek(0)
                json.dump(vprasanja, f)
                f.truncate #truncate zmanjša velikost file-a
                print( "Vprašanje je bilo uspešno dodano.")
        
        else: 
            print("Nimate dovoljenja dodajati vprašanja. To je dovoljeno le adminom in Jedi Masters, you are but a Stormtrooper!")


def ustvari_racun():
    print("\n ======== USTVARI RAČUN ========")
    uporabnisko_ime = input("Izberite si UPORABNIŠKO IME, Youngling: ")
    geslo = getpass.getpass(prompts = 'Izberite si GESLO, Youngling: ')
    with open('uporabnik_account.json', 'r+') as uporabniski_racuni:
        uporabniki = json.load(uporabniski_racuni)

        if uporabnisko_ime in uporabnik.keys():
            print("Račun s tem imenom že obstaja. \n May the Force be with you in se vrni na prijavo.")
        else: 
            uporabnik[uporabniki] = [geslo, "IGRALEC"]
            uporabniski_racuni.seek(0)
            json.dump(uporabniki, uporabniski_racuni)
            uporabniski_racuni.truncate()
            print("Uporabniški račun je bil uspešno ustvarjen, dobrodošli v Jedi order!")


def prijava_racun():
    print('\n ======== PRIJAVA ========')
    uporabnisko_ime = input("UPORABNIŠKO IME: ")
    geslo = getpass.getpass(prompt= 'GESLO: ')

    with open('uporabnik_account.json', 'r') as uporabniski_racuni:
        uporabniki = json.load(uporabniski_racuni)

    if uporabnisko_ime not in uporabnik.keys():
        print("Račun s tem imenom ne obstaja. \n Prosim, najprej si ustvarite račun!")
    elif uporabnisko_ime in uporabnik.keys():
        if uporabniki[uporabnisko_ime][0] != geslo:
            print("Vaše geslo ni pravilno.\n Prosim, ponovno vnestie geslo in poskusite znova.")
        elif uporabniki[uporabnisko_ime][0]== geslo:
            print("Uspešno ste se prijavili. \n")
            uporabnik.append(uporabnisko_ime)
            uporabnik.append(uporabniki[uporabnisko_ime][1])


def odjava():
    global uporabnik
    if len(uporabnik) == 0:
        print("Odjavljeni ste.")
    else:
        uporabnik = []
        print("Uspešno ste se odjavili. May the Force be with you!")


def pravila():
    print(''' \n ======== PRAVILA ========
    1. Vsak krog sestavlja 10 vprašanj, ki so Vam postavljena naključno. Da odgovorite, morate pritisniti A/B/C (lahko tudi a/b/c).
    2. Vsako vprašanje Vam prinese do eno točko. Če odgovorite narobe, ne dobite minus točk, le 0 (za razliko od kvizov pri analizi ;).
    3. Lahko si ustvarite uporabniški račun s pomočjo panela USTVARI RAČUN.
    4. Lahko se prijavite s pomočjo panela PRIJAVA.
    ''')


def o_kvizu():
    print(''' \n ======== O NASTANKU KVIZA (Ali Geneza) ========
    Ta kviz je bil ustvarjen za projektno nalogo pri predmetu Programiranje 1, 2. semester leta 2019/2021. 
    ''')

if __ime__ == "__main__":
    moznost = 1
    while moznost != 7:
        print(' \n ======== MAY THE FORCE BE WITH YOU; KO REŠUJETE KVIZ! ========')
        print('-----------------------------------------------------------------')
        print('1. ZAČNI Z REŠEVANJEM')
        print('2. DODAJ VPRAŠANJA')
        print('3 USTVARI RAČUN')
        print('4. PRIJAVA')
        print('5. ODJAVA')
        print('6. NAVODILA IGRE (če slučajno niste Jedi, ki lahko bere misli ustvarjalcev kviza)')
        print('7. IZHOD')
        print('8. GENEZA')
        moznost = int(input('IZBERI MOŽNOST (in s tem izberi prihodnost)'))

        if moznost == 1:
            igra()
        elif moznost == 2:
            vprasanja_kviza()
        elif moznost == 3:
            ustvari_racun()
        elif moznost == 4:
            prijava_racun()
        elif moznost == 5:
            odjava()
        elif moznost == 6:
            pravila()
        elif moznost == 7:
            break
        elif moznost == 8:
            o_kvizu()
        else:
            print("Neveljavna izbira, poskusi znova!")



   
