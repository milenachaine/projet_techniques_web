#script d'extraction de données de pages web (titre, url, description) sur Wikipedia
#version 1 : sortie au format CSV

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.firefox.options import Options

def afficher_resultat(driver): #affiche résultats page
    titres = driver.find_elements_by_xpath("//tr/td[1]/a")
    liens = [titre.get_attribute('href') for titre in titres]
    for titre, lien in zip(titres,liens):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        try:
            driver.get(lien)
            paragraphe = driver.find_element_by_xpath("//p[1]")
            paragraphe_full = paragraphe.text
        finally:
            driver.quit()
        if not paragraphe_full.empty():
            print("{};{};{};{}".format(ville, titre.text, lien, paragraphe_full.replace(";",":")), file=fichier)


def firefox_extraire(url):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10) #attend 10 secondes MAX avant de continuer (plus tôt si tout est dispo)
    try: #va sur la page google et recherche un nom de ville (argument)
        driver.get(url)
        afficher_resultat(driver) #affiche les résultats
    finally:
        driver.quit()


villes = ["Paris", "New York"]
urls = ["http://en.wikipedia.org/wiki/List_of_museums_in_Paris", "https://en.wikipedia.org/wiki/List_of_museums_in_New_York_City"]
with open("sites.csv", "w") as fichier:
    print("ville;nom;url;desc", file=fichier)
    for url, ville in zip(urls,villes):
        firefox_extraire(url)
