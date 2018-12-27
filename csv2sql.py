#version du cours sans commentaires

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.firefox.options import Options
import sqlite3

def afficher_resultat(driver): #affiche résultats page
    resultats = driver.find_elements_by_css_selector("h3.LC20lb")
    i = 0
    for resultat in resultats:
        print(resultat.text)
        c.execute("INSERT INTO Titre VALUES (NULL, ?, (SELECT id from Villes WHERE nom=?))", (resultat.text, ville))

def firefox_extraire(ville):
    driver = webdriver.Firefox()

    driver.implicitly_wait(10) #attend 10 secondes MAX avant de continuer (plus tôt si tout est dispo)

    try: #va sur la page google et recherche un nom de ville (argument)
        driver.get("http://google.com")
        inputElement = driver.find_element_by_name("q")
        inputElement.send_keys(ville)
        inputElement.submit()

        afficher_resultat(driver) #affiche les résultats

        for i in range(2,11): #récupère les liens de pagination
            page = driver.find_element_by_css_selector("a#pnnext")
            page.click()
            afficher_resultat(driver)

    finally:
        driver.quit()

conn = sqlite3.connect('villes.db')
c = conn.cursor()

villes = ["Paris", "New York"]
for ville in villes:
    firefox_extraire(ville)

conn.commit()
conn.close()
