#script d'extraction de données sur des vols (Google Flights)
#version 1 : format CSV

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.firefox.options import Options
import sqlite3

def afficher_resultat(driver): #affiche résultats page
    resultats = driver.find_elements_by_xpath("//div[contains(@class, 'gws-flights-results__collapsed-itinerary gws-flights-results__itinerary')]")
    for resultat in resultats:
        resultats_liste = resultat.text.split('\n')
        if url == "http://www.google.fr/flights#flt=/m/05qtj./m/02_286.2019-01-06;c:EUR;e:1;sd:1;t:f;tt:o":
            print("1;2;{};{}".format(resultats_liste[1],resultats_liste[-1]), file=fichier)
        else:
            print("2;1;{};{}".format(resultats_liste[1],resultats_liste[-1]), file=fichier)
def firefox_extraire(url):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10) #attend 10 secondes MAX avant de continuer (plus tôt si tout est dispo)
    try: #va sur la page google et recherche un nom de ville (argument)
        driver.get(url)
        afficher_resultat(driver) #affiche les résultats
    finally:
        driver.quit()

villes = ["Paris", "New York"]
urls = ["http://www.google.fr/flights#flt=/m/05qtj./m/02_286.2019-01-06;c:EUR;e:1;sd:1;t:f;tt:o", "http://www.google.fr/flights#flt=/m/02_286./m/05qtj.2019-01-04;c:EUR;e:1;sd:1;t:f;tt:o"]

with open("vols.csv", "w") as fichier:
    print("ville_dep;ville_arr;compagnie;prix", file=fichier)
    for url, ville in zip(urls,villes):
        firefox_extraire(url)
