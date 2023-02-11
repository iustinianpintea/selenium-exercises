# librari gratuite care ne trebuie sa accesam selenium si sa avem acces la chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window() #marire fereastra
chrome.get("https://the-internet.herokuapp.com/login")
#daca elementul e de tip a folosim by.linktext si copiem textul cu negru
sleep(4) # ingreuneaza , testele ar trebui sa fie cat mai rapide
chrome.find_element(By.LINK_TEXT, "Elemental Selenium").click()
sleep(10)