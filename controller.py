from flask import Flask, render_template, request, redirect, url_for
from model import Site,Station,Observations

app = Flask(__name__)

# salut

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



@app.route('/corse', methods=['GET', 'POST'])
def corse():
    route_path = 'corse'
    departements = Site.search_departement("CORSE")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)

@app.route('/centrevdl', methods=['GET', 'POST'])
def centrevdl():
    route_path = 'centrevdl'
    departements = Site.search_departement("CENTRE-VAL DE LOIRE")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)



@app.route('/bretagne', methods=['GET', 'POST'])
def bretagne():
    route_path = 'bretagne'
    departements = Site.search_departement("BRETAGNE")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)

@app.route('/bfc', methods=['GET', 'POST'])
def bfc():
    route_path = 'bfc'
    departements = Site.search_departement("BOURGOGNE-FRANCHE-COMTE")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)

@app.route('/grandest', methods=['GET', 'POST'])
def grandest():
    route_path = 'grandest'
    departements = Site.search_departement("GRAND EST")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)


@app.route('/occitanie', methods=['GET', 'POST'])
def occitanie():
    route_path = 'occitanie'
    departements = Site.search_departement("OCCITANIE")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)

@app.route('/hautsdefr', methods=['GET', 'POST'])
def hautsdefr():
    route_path = 'hautsdefr'
    departements = Site.search_departement("HAUTS-DE-FRANCE")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)

@app.route('/ara', methods=['GET', 'POST'])
def ara():
    route_path = 'ara'
    departements = Site.search_departement("AUVERGNE-RHONE-ALPES")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)

# Continuer pour les autres routes...

@app.route('/normandie', methods=['GET', 'POST'])
def normandie():
    route_path = 'normandie'
    departements = Site.search_departement("NORMANDIE")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)

@app.route('/pdll', methods=['GET', 'POST'])
def pdll():
    route_path = 'pdll'
    departements = Site.search_departement("PAYS DE LA LOIRE")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)

@app.route('/paca', methods=['GET', 'POST'])
def paca():
    route_path = 'paca'
    departements = Site.search_departement("PROVENCE-ALPES-COTE D'AZUR")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)

@app.route('/idf', methods=['GET', 'POST'])
def idf():
    route_path = 'idf'
    departements = Site.search_departement("ILE-DE-FRANCE")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)

@app.route('/nouvellea', methods=['GET', 'POST'])
def nouvellea():
    route_path = 'nouvellea'
    departements = Site.search_departement("NOUVELLE-AQUITAINE")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)

@app.route('/guyane', methods=['GET', 'POST'])
def guyane():
    route_path = 'guyane'
    departements = Site.search_departement("GUYANE")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)

@app.route('/martinique', methods=['GET', 'POST'])
def martinique():
    route_path = 'martinique'
    departements = Site.search_departement("MARTINIQUE")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)

@app.route('/mayotte', methods=['GET', 'POST'])
def mayotte():
    route_path = 'mayotte'
    departements = Site.search_departement("MAYOTTE")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)

@app.route('/guadeloupe', methods=['GET', 'POST'])
def guadeloupe():
    route_path = 'guadeloupe'
    departements = Site.search_departement("GUADELOUPE")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)

@app.route('/reunion', methods=['GET', 'POST'])
def reunion():
    route_path = 'reunion'
    departements = Site.search_departement("LA REUNION")
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement.html', departements=departements, route_path=route_path)





@app.route('/region', methods=['GET', 'POST'])
def region():
    regions = Site.get_all_region()
    if request.method == 'POST':
        if "regionss" in request.form:
            
            region_name = request.form.get('regionss')
            return redirect(url_for('departement', region_name=region_name))
        elif "Commune" in request.form:
            commune_name = request.form['Commune']
            
            return redirect(url_for('search_result', commune_name=commune_name))
    return render_template('region.html', regions=regions)

@app.route('/search_result/<commune_name>', methods=['GET', 'POST'])
def search_result(commune_name):
    result = Station.research_tab(commune_name)
    if "stationss" in request.form:
        code_station = request.form.get('stationss')
        return redirect(url_for('stationsinfo', code_station=code_station))
    return render_template('search_result.html', result=result)



@app.route('/departement/<region_name>', methods=['GET', 'POST'])
def departement(region_name):
    departements = Site.search_departement(region_name)
    for i in departements:
        print(i.libelle_departement)
    if request.method == 'POST':
        departement_name = request.form.get('departementss')
        return redirect(url_for('communes', departement_name=departement_name))
    return render_template('departement1.html', departements=departements, region_name=region_name)


@app.route('/communes/<departement_name>', methods=['GET', 'POST'])
def communes(departement_name):
    communes = Site.search_commune(departement_name)
    if request.method == "POST":
        commune_name = request.form.get('communess')
        return redirect(url_for('sites', commune_name=commune_name))
    return render_template('communes.html', communes=communes,departement_name=departement_name)

@app.route('/sites/<commune_name>', methods=['GET', 'POST'])
def sites(commune_name):
    sites = Site.search_sites(commune_name)
    if request.method == "POST":
        code_site = request.form.get('sitess')
        return redirect(url_for('stations', code_site=code_site))
    return render_template('sites.html', sites=sites,commune_name=commune_name)

@app.route('/stations/<code_site>', methods=['GET', 'POST'])
def stations(code_site):
    stations = Station.search_station(code_site)

    if request.method == "POST":

        if "stationss" in request.form:
            code_station = request.form.get('stationss')
            return redirect(url_for('stationsinfo', code_station=code_station))
        
        elif "station_tr" in request.form:
            code_station = request.form.get('station_tr')
            obscheck = Observations.get_obs_tr(code_station)
            if not obscheck:
                return redirect(url_for('error404.html'))
            return redirect(url_for('stations_obs_tr', code_station=code_station))
        
        elif "station_date" in request.form:
            code_station = request.form.get('station_date')
            return redirect(url_for('stations_obs_date', code_station=code_station, date=None))
        
    return render_template('station.html', stations=stations, code_site=code_site)


@app.route('/stationsinfo/<code_station>', methods=['GET', 'POST'])
def stationsinfo(code_station):
    stationsinfo = Station.get_all_info(code_station)
    return render_template('stationsinfos.html', stationsinfo=stationsinfo, code_station=code_station)


@app.route('/stations_obs_tr/<code_station>', methods=['GET', 'POST'])
def stations_obs_tr(code_station):
    observations = Observations.get_obs_tr(code_station)
    return render_template('station_obs_tr.html', observations=observations, code_station=code_station) 


@app.route('/stations_obs_date/<code_station>', methods=['GET', 'POST'])
def stations_obs_date(code_station):
    date = request.args.get('date')
    print(date)
    observations = Observations.get_obs_date(code_station, date)
    
    if request.method == "POST":
        if "get_date" in request.form:
            date = request.form.get('date')
            return redirect(url_for('stations_obs_date', code_station=code_station, date=date))
    return render_template('station_obs_date.html', observations=observations, date=date, code_station=code_station)

if __name__ == '__main__':
    app.run(debug=True)