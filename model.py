import requests
import math
import datetime
import matplotlib.pyplot as plt
import sqlite3


DATABASE_FILE = "db_hydro.db"


conn = sqlite3.connect(DATABASE_FILE, check_same_thread=False)
cursor = conn.cursor()

class Observations:
    def __init__(self, code_station=None, date_debut_serie=None, date_fin_serie=None, date_obs=None, resultat_obs=None, continuite_obs_hydro=None):
        self.code_station = code_station
        self.date_debut_serie = date_debut_serie
        self.date_fin_serie = date_fin_serie
        self.date_obs = date_obs
        self.resultat_obs = resultat_obs
        self.continuite_obs_hydro = continuite_obs_hydro

    def __repr__(self):
        return (f"Observation(code_station={self.code_station}, date_debut_serie={self.date_debut_serie}, "
                f"date_fin_serie={self.date_fin_serie}, date_obs={self.date_obs}, "
                f"resultat_obs={self.resultat_obs}, continuite_obs_hydro={self.continuite_obs_hydro})")

    def get_obs_tr(code_station):
        url = f'https://hubeau.eaufrance.fr/api/v1/hydrometrie/observations_tr?code_entite={code_station}&pretty&grandeur_hydro=H&fields=code_station,date_debut_serie,date_fin_serie,date_obs,resultat_obs,continuite_obs_hydro&cursor=&size=1'
        # Télécharger le contenu du fichier JSON
        response = requests.get(url)
        
        # Vérifier que la requête a réussi (code de statut 200)
        if response.status_code == 206 and Station.station_actif(code_station) == "Actif":
            # Charger le contenu JSON
            data = response.json()  # json.loads(response.text) aussi fonctionnera
            
            # Accéder à des éléments spécifiques
            observations = data['data']
            tab = []
            for obs in observations:
                date_debut_serie = obs['date_debut_serie']
                date_fin_serie = obs['date_fin_serie']
                date_obs = obs['date_obs']
                resultat_obs = obs['resultat_obs']
                continuite_obs_hydro = obs['continuite_obs_hydro']
            tab.append(Observations(code_station, date_debut_serie, date_fin_serie, date_obs, resultat_obs, continuite_obs_hydro))
            
            return tab
            
        else:
            return False
    
    def get_obs_date(code_station, date):
        if date is not None:
            url = f'https://hubeau.eaufrance.fr/api/v1/hydrometrie/observations_tr?code_entite={code_station}&date_debut_obs={date}'
            # Télécharger le contenu du fichier JSON
            response = requests.get(url)
            
            # Vérifier que la requête a réussi (code de statut 200)
            if response.status_code in (200, 206):
                if Station.station_actif(code_station) == "Actif":
                    # Charger le contenu JSON
                    data = response.json()  # json.loads(response.text) aussi fonctionnera
                    tab=[]
                    # Accéder à des éléments spécifiques
                    observations = data['data']
                    if observations:  # Vérifier s'il y a des observations disponibles
                        obs = observations[0]
                        date_debut_serie = obs['date_debut_serie']
                        date_fin_serie = obs['date_fin_serie']
                        date_obs = obs['date_obs']
                        resultat_obs = obs['resultat_obs']
                        continuite_obs_hydro = obs['continuite_obs_hydro']
                        tab.append(Observations(code_station, date_debut_serie, date_fin_serie, date_obs, resultat_obs, continuite_obs_hydro))

                        return tab
                    else:
                        return None
                else:
                    return f"La Station est malheureusement {Station.station_actif(code_station)} "
            else:
                return f"Impossible d'accéder aux observations de la station"
        else:
            return None
    
    
    def get_evol_obs(code_station):
    # Prendre la date d'aujourd'hui
        aujourdhui = datetime.date.today()
        tab_temp = []
        tab_jour = []
        
        # Itérer et imprimer les 30 derniers jours
        for i in range(1, 30):
            jour_précédent = aujourdhui - datetime.timedelta(days=i)
            observation = Observations.get_obs_date(code_station, jour_précédent)
            
            if observation is not None:
                tab_jour.append(i)
                for i in observation:
                    tab_temp.append(i.resultat_obs)
        
        Observations.create_graph(tab_temp, tab_jour)
        return tab_temp, tab_jour
    
    def create_graph(tab_evol,tab_jour):
        plt.plot(tab_jour,tab_evol)

        # Step 4: Customize Plot
        plt.title('Courbe d\'évolution de l\'hydrométrie')
        plt.xlabel('Nombre de Jours')
        plt.ylabel('Observations (mesure?)')
        plt.grid(True)

        # Step 5: Display Plot
        plt.savefig('static\\graph.png', bbox_inches='tight')


class Site:

    #Constructeur pour les détails du site
    def __init__(self, 
                code_site=None, 
                libelle_site=None, 
                type_site=None, 
                coordonnee_x_site=None, 
                coordonnee_y_site=None, 
                longitude_site=None, 
                latitude_site=None, 
                altitude_site=None, 
                code_systeme_alti_site=None, 
                libelle_commune=None, 
                code_departement=None, 
                code_region=None, 
                libelle_region=None, 
                code_cours_eau=None, 
                grandeur_hydro=None, 
                date_maj_sites=None, 
                libelle_departement=None, 
                number=None):
        self.code_site = code_site
        self.libelle_site = libelle_site
        self.type_site = type_site
        self.coordonnee_x_site = coordonnee_x_site
        self.coordonnee_y_site = coordonnee_y_site
        self.longitude_site = longitude_site
        self.latitude_site = latitude_site
        self.altitude_site = altitude_site
        self.code_systeme_alti_site = code_systeme_alti_site
        self.libelle_commune = libelle_commune
        self.code_departement = code_departement
        self.code_region = code_region
        self.libelle_region = libelle_region
        self.code_cours_eau = code_cours_eau
        self.grandeur_hydro = grandeur_hydro
        self.date_maj_sites = date_maj_sites
        self.libelle_departement = libelle_departement
        self.number = number

    def tout_station_dep(code_departemental):
        cursor.execute(f"SELECT COUNT(*) FROM Sites where code_departement = {code_departemental}")
        results = cursor.fetchall()

        return results

    # Preshot : fonction au cas où si on a besoin
    def get_all_site():
        cursor.execute("SELECT * FROM Sites")
        results = cursor.fetchall()
        tab = []

        for row in results:
            tab.append(Site(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 
            row[8], row[9], row[10], row[11], row[12], row[13], row[14], 
            row[15],row[16], 0))

        return tab
    
    # Preshot : fonction au cas où si on a besoin
    def get_all():
        cursor.execute("SELECT * FROM Sites")
        results = cursor.fetchall()
        dictio = {}

        for row in results:
            dictio[Site(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 
            row[8], row[9], row[10], row[11], row[12], row[13], row[14], 
            row[15], row[16], 0)]= Station.get_all_station(row[0])
        
        return dictio

    # Affiche les info du site séléctionné
    def get_site_info(code_site):
        cursor.execute("SELECT * FROM Sites where code_site = ?", (code_site,))
        results = cursor.fetchall()
        tab = []

        for row in results:
            tab.append(Site(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 
            row[8], row[9], row[10], row[11], row[12], row[13], row[14], 
            row[15],row[16], 0))

        return tab

    def get_all_region():
        cursor.execute("SELECT DISTINCT libelle_region from sites")
        result = cursor.fetchall()
        tab  =[]

        for row in result:
            if row[0] is not None:
                tab.append(Site(libelle_region=row[0]))

        return tab

    def search_departement(region):
        cursor.execute("SELECT DISTINCT sites.libelle_departement, sites.code_departement, COUNT(libelle_station) FROM sites, stations where sites.code_site = stations.code_site AND sites.libelle_region LIKE ? group by libelle_departement ", (region,) )
        result = cursor.fetchall()
        tab = []

        for row in result:
            if row[0] is not None:
                tab.append(Site(libelle_departement=row[0], code_departement=row[1], number=row[2], libelle_region=region ))

        return tab
    
    # Affiche les commune disponibles dans le départements
    def search_commune(departement):
        cursor.execute("SELECT DISTINCT sites.libelle_commune, COUNT(libelle_station) FROM sites, stations where sites.code_site = stations.code_site AND sites.libelle_departement LIKE ? group by libelle_station", (departement,) )
        result = cursor.fetchall()
        tab = []

        for row in result:
            if row[0] is not None:
                tab.append(Site(libelle_commune=row[0], number=row[1], libelle_departement=departement))
        return tab 
    

    #Affiche les sites disponible dans la commune
    def search_sites(commune):
        cursor.execute("SELECT sites.libelle_site, sites.code_site, COUNT(libelle_station) FROM sites, stations WHERE sites.code_site = stations.code_site and sites.libelle_commune LIKE ? group by sites.libelle_site ", (commune,) )
        result = cursor.fetchall()
        tab = []
        for row in result:
            if row[0] is not None:
                tab.append(Site(libelle_site=row[0],code_site=row[1],number=row[2], libelle_commune=commune))
        return tab

class Station:
    # Constructeur pour les détails de la station
    def __init__(self, 
                 code_station=None, 
                 code_site=None, 
                 libelle_site=None, 
                 libelle_station=None, 
                 type_station=None, 
                 coordonnee_x_station=None, 
                 coordonnee_y_station=None, 
                 longitude_station=None, 
                 latitude_station=None, 
                 altitude_ref_alti_station=None, 
                 code_commune_station=None, 
                 libelle_commune=None, 
                 code_departement=None, 
                 code_region=None, 
                 libelle_region=None, 
                 en_service=None, 
                 date_fermeture_station=None, 
                 date_ouverture_station=None):
        self.code_station = code_station
        self.code_site = code_site
        self.libelle_site = libelle_site
        self.libelle_station = libelle_station
        self.type_station = type_station
        self.coordonnee_x_station = coordonnee_x_station
        self.coordonnee_y_station = coordonnee_y_station
        self.longitude_station = longitude_station
        self.latitude_station = latitude_station
        self.altitude_ref_alti_station = altitude_ref_alti_station
        self.code_commune_station = code_commune_station
        self.libelle_commune = libelle_commune
        self.code_departement = code_departement
        self.code_region = code_region
        self.libelle_region = libelle_region
        self.en_service = en_service
        self.date_fermeture_station = date_fermeture_station
        self.date_ouverture_station = date_ouverture_station


    def __repr__(self):
        return (f"{self.code_station} {self.code_site} {self.libelle_site} "
                f"{self.libelle_station} {self.type_station} "
                f"{self.coordonnee_x_station} {self.coordonnee_y_station} "
                f"{self.longitude_station} {self.latitude_station} "
                f"{self.altitude_ref_alti_station} {self.code_commune_station} "
                f"{self.libelle_commune} {self.code_departement} "
                f"{self.code_region} {self.libelle_region} {self.en_service} "
                f"{self.date_fermeture_station} {self.date_ouverture_station})")

    
    # Affiche toute les infos du site
    def get_all_info(code_station):
        cursor.execute("SELECT * FROM stations where code_station = ?", (code_station,))
        result = cursor.fetchall()
        
        tab = []
        for row in result:
            tab.append(Station(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 
                row[8], row[9], row[10], row[11], row[12], row[13], row[14], 
                Station.station_actif(row[0]), row[16], row[17]))
            
        return tab
    
    # Affiche les stations disponibles disponibles du site
    def search_station(code_site):
        cursor.execute("SELECT code_station, libelle_station, type_station FROM stations where code_site = ?", (code_site,))
        result = cursor.fetchall()
        tab = []

        for row in result:
            tab.append(Station(code_station = row[0],libelle_station=row[1],type_station=row[2],en_service=Station.station_actif(row[0])))
        return tab        
    
    def research_tab(nom_ville):
        like = "%"
        like += nom_ville + like
        cursor.execute("SELECT code_station, libelle_station, type_station FROM stations where libelle_commune LIKE ? ", (like,))
        result = cursor.fetchall()
        tab = []

        for row in result:
            tab.append(Station(code_station = row[0],libelle_station=row[1],type_station=row[2],en_service=Station.station_actif(row[0])))
        return tab   

    def station_actif(code_station):
        cursor.execute("SELECT en_service, date_fermeture_station FROM stations where code_station = ?", (code_station,))
        result = cursor.fetchall()
        for row in result:
            if row[0] == 0:
                date_str = row[1]
                formatted_date_str = date_str.replace("-", "/")
                return f"Inactif depuis le : {formatted_date_str}"
            else:
                return "Actif"
            