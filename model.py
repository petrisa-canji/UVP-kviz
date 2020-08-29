import json
import uuid
from bottle import request, response

class Model:
    def __init__(self, data_path, Star_Wars_junaki_path):
        sel.uporabnik = {}

    with open(data_path) as file:
        self.vprasanja = json.load(file)
    
    with open(Star_wars_junaki_path) as file:
        self.Star_Wars_junaki = json-load(file)

    def pridobite_vprasanja(self, id):
        return self.vprasanja[id]
    
    def dobljena_vprasanja(self, id):
        return 0 <= id < len(self.vprasanja)

    def odgovor(self, uporabnik, id, odgovor):
        vprasanje = self.vprasanja[id]

        user.dodaj_tocke(self, vprasanje['mozni odgovori'][odgovor])

    def pridobitev_rezultatov(self, uporabnik):
        return sorted(zip(self.Star_Wars-junaki, uporabnik.points), key=lambda e: (-e[1], e[0]['ime']))

    #dodatek po priporočilu kolegici iz FERI

    def sedanji_uporabnik(self):
        cookie = request.get_cookie('uporabnik')
        if not cookie or cookie not in self.uporabniki:
            uporabnik = Uporabnik(uuid.uuid4().hex)
            self.uporabniki[uporabnik.uuid] = uporabnik
            response.set_cookie('uporabnik', user.uuid)
            return uporabnik
        else:
            return self.uporabnik[cookie]

    def spusti_uporabnika(self, uporabnik):
        self.uporabniki.pop(uporabnik.uuid)
        response.delete_cookie('uporabnik')
    
class Uporabnik:
    
    def __init__(self):
        self.points = [0] * 16

    def dodaj_tocke(self, model, Star_Wars_junaki):
        for junak in Star_Wars_junaki:
            self.points[model-get_Star_Wars_junaki_index(junak)] += 1
