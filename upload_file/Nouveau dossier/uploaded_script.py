from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Initialiser le navigateur
driver = webdriver.Chrome()

# Ouvrir la page spécifiée
driver.get('https://www.sitew.com/Se-connecter-pour-modifier-mon-site')

# Remplir les champs du formulaire
username_input = driver.find_element(By.ID, "user_login")
password_input = driver.find_element(By.ID, "user_password")

username_input.send_keys("votre_nom_utilisateur")
password_input.send_keys("votre_mot_de_passe")

# Attendre quelques secondes pour que la page se charge
time.sleep(4)

# Soumettre le formulaire
password_input.send_keys(Keys.RETURN)
connect_button = driver.find_element_By.ID("se_connecte")
connect_button.click()

#Attendre quelques secondes pour que la page se charge
time.sleep(7)

#Fermer le navigateur
driver.quit()
