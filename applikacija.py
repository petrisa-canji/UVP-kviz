from bottle import route, run, template, request, abort, redirect, static_file
from model import Model

model = Model('vprasanja.json', 'Star_Wars_Junaki.json')


@route('/res/<filename:path>')
def resource(filename):
    return static_file(filename, root='res/')

@route('/')
def main():
    return template('kviz.html')

@rounte('/pravila')
def pravila():
    return template('kviz-pravila.html')

@route('/vprasanje/<spr>')
def vprasanje(spr):
    spr = int(spr)

    if not model.dobljena_vprasanja(spr):
        abort(404, 'Ni takšnega vprašanja.')

    vprasanje = model.pridobite_vprasanja(spr)

    return template('vprasanja.html', text=vprasanje['text'], spr=spr)


@route('/odgovor', method='POST')
def odgovor():
    spr = int(request.forms.get('vprasanje'))
    answer = int(request.forms.get('odgovor'))

    uporabnik = model.sedanji_uporabnik()
    model.odgovor(uporabnik, spr, answer)

    #vrne na prvo stran
    if model.dobljena_vprasanja(spr + 1):
        redirect('/vprasanja/{}'.format(spr + 1))
    else:
        redirect('/prikaz_rezultatov')


@route('/prikaz_rezultatov')
def rezultat():
    return template('rezultati.html')


@route('/pridobitev_rezultatov')
def pridobitev_rezultatov():
    uporabnik = model.sedanji_uporabnik()
    model.spusti_uporabnika(uporabnik)  #podatki uporabnika sedaj niso več potrebni in se lahko zbrišejo

    rezultat = model.pridobitev_rezultatov(uporabnik)
    return template('stran_z_rezultati.html', rezultat=rezultat)


if __name__ == '__main__':
    run()
