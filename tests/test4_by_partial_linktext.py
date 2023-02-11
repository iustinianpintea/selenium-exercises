# librari gratuite care ne trebuie sa accesam selenium si sa avem acces la chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window() #marire fereastra
chrome.get("https://the-internet.herokuapp.com/login")
#daca elementul e de tip a si e foarte lung  folosim by.text si copiem textul cu negru partial
sleep(4) # ingreuneaza , testele ar trebui sa fie cat mai rapide
chrome.find_element(By.PARTIAL_LINK_TEXT, "Elemental").click()
sleep(10)