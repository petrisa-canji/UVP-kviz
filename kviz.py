import json #sprememba python data string v json data string
import random #random number generator
import getpass #bere userinput, dokler user ne pritisne pass

def igra():
    print("\n ======== ZAČNI KVIZ ========")
    tocke = 0 #točke, ki se beležijo z odgovori, imajo najprej vsoto 0
    with open("vprasanja.json", 'r+') as f: #'r+' pomeni for reading and writing

        j = json.load(f) #dodatek okrajšave za lažje pisanje

        for i in range(10): #ker bo izmed 30 vprašanj naključno izbralo 10
            stevilo_vprasanj = len(j)
            ch = random.randint(0, stevilo_vprasanj - 1)
            #print("test")
            #print(f"\nQ{i + 1} {j[ch]['vprasanje']}\n")
            print(f'\nQ{i + 1}{j[ch]["vprasanje"]}\n') #\n je new line
            #zgornja koda je zakomentirana in ponovno napisana, ker na enem računalniko ni pognalo, na drugem pa je, vrstici 15 in 16 sta posledici tega

            for option in j[ch]["mozni odgovori"]: #predstavitev možnih odgovorov
                print(option)
            odgovor = input("\n Odgovor:")

            if odgovor.upper() == "DA": #kako program šteje - če uporabnik izbere odgovor, kateri je bil označen z DA (za tem "DA" se skrivajo osebnosti), prišteje 1
                tocke += 1
            else:
                pass


            del j[ch] #zbriše tisto vprašanje iz seznama vprašanj

        #print("test")
        #print(f"\n KONČNI REZULTAT: Število DA - {tocke}, Število NE - {10-tocke}")
        print(f'\n KONČNI REZULTAT: Število DA - {tocke}, Število NE - {10-tocke}')  #f replaces the expressions with their values
        #zgornja koda je zakomentirana in ponovno napisana, ker na enem računalniko ni pognalo, na drugem pa je, vrstici 15 in 16 sta posledici tega



def vprasanja_kviza(): #omogoča možnost dodajanja vprašanj, če ima uporabnik administrativno vlogo (se prepozna po uporabniškem imenu)
    if len(uporabnik) == 0:
        print("Preden lahko dodajate vprašanja, se morate prijaviti!")

    elif len(uporabnik) == 2:
        if uporabnik[1]:
            print('\n ======== DODAJ VPRAŠANJA ========')
            vpr = input("Dodaj želeno vprašanje, Jedi Master: \n")
            opt = []
            print("Dodaj 2 možnosti odgovora, ki ju poimenuj (DA, NE)")
            for _ in range(2):
                opt.append(input())
            odg = input("Dodaj vprašanje: \n")

            with open("vprasanja.json", 'r+') as f: #možnost dodajanja vprašanj, ki se zabeležijo v vprasanja.json file
                vprasanja = json.load(f)
                dic = {"vprašanje": vpr, "možnosti": opt, "odgovor": odg}
                vprasanja.append(dic)
                f.seek(0)
                json.dump(vprasanja, f)
                f.truncate #truncate zmanjša velikost file-a
                print( "Vprašanje je bilo uspešno dodano.")

        else:
            print("Nimate dovoljenja dodajati vprašanja. To je dovoljeno le adminom in Jedi Masters, you are but a Stormtrooper!")


def ustvari_racun(): #omogoča uporabniku ustvariti račun
    print("\n ======== USTVARI RAČUN ========")
    uporabnisko_ime = input("Izberite si UPORABNIŠKO IME, Youngling: ")
    geslo = getpass.getpass(prompt= 'Izberite si GESLO, Youngling: ')
    with open('uporabnik_account.json', 'r+') as uporabniski_racuni:
        uporabniki = json.load(uporabniski_racuni)

        if uporabnisko_ime in uporabniki.keys():
            print("Račun s tem imenom že obstaja. \n May the Force be with you in se vrni na prijavo.")
        else:
            uporabniki[uporabnisko_ime] = {'geslo': geslo, 'ADMIN': False}
            uporabniski_racuni.seek(0)
            json.dump(uporabniki, uporabniski_racuni, indent=1)
            uporabniski_racuni.truncate()
            print("Uporabniški račun je bil uspešno ustvarjen, dobrodošli v Jedi order!")

def prijava_racun(): #uporabniku omogoča prijavo v prej ustvarjen račun
    print('\n ======== PRIJAVA ========')
    uporabnisko_ime = input("UPORABNIŠKO IME: ")
    geslo = getpass.getpass(prompt= 'GESLO: ')

    with open('uporabnik_account.json', 'r') as uporabniski_racuni:
        uporabniki = json.load(uporabniski_racuni)

    if uporabnisko_ime not in uporabniki.keys():
        print("Račun s tem imenom ne obstaja. \n Prosim, najprej si ustvarite račun!")
    elif uporabnisko_ime in uporabniki.keys():
        if uporabniki[uporabnisko_ime]['geslo'] == geslo:
            print("Uspešno ste se prijavili. \n")
            return [uporabnisko_ime, uporabniki[uporabnisko_ime]['geslo']]
        else:
            print("Vaše geslo ni pravilno.\n Prosim, ponovno vnestie geslo in poskusite znova.")

def odjava(): #uporabniku omogoča odjavo
    global uporabnik
    if uporabnik == []:
        print("Odjavljeni ste.")
    else:
        uporabnik = []
        print("Uspešno ste se odjavili. May the Force be with you!")


def pravila(): #da ne bo igranje dvoumno, so tukaj pravila
    print(''' \n ======== PRAVILA ========
    1. Vsak krog sestavlja 10 vprašanj, ki so Vam postavljena naključno. Da odgovorite, morate pritisniti DA/NE (lahko tudi da/ne).
    2. Vsako vprašanje Vam prinese do eno točko. Če odgovorite narobe, ne dobite minus točk, le 0 (za razliko od kvizov pri analizi ;).
    3. Lahko si ustvarite uporabniški račun s pomočjo panela USTVARI RAČUN.
    4. Lahko se prijavite s pomočjo panela PRIJAVA.
    ''')


def o_kvizu():
    print(''' \n ======== O NASTANKU KVIZA (Ali Geneza) ========
    Ta kviz je bil ustvarjen za projektno nalogo pri predmetu Programiranje 1, 2. semester leta 2019/2021.
    ''')

if __name__ == "__main__": #to se najprej pojavi v terminalu, ko se program zažene
    moznost = 0
    uporabnik = 0
    while moznost != 7:
        print(' \n ======== MAY THE FORCE BE WITH YOU; KO REŠUJETE KVIZ! ========')
        print('-----------------------------------------------------------------')
        print('1. ZAČNI Z REŠEVANJEM')
        print('2. DODAJ VPRAŠANJA')
        print('3. USTVARI RAČUN')
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
            uporabnik = prijava_racun()
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




