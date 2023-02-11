#librari gratuite care ne trebuie sa accesam selenium si sa avem acces la chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam chrome - un tab gol de chrome sau ce alt browser vrem
#salvam in variabila chrome tabul gol de chrome

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

chrome.maximize_window() #marire fereastra
chrome.get("https://the-internet.herokuapp.com/login")
#daca are atributul name adica vedem name = "...." putem folosi by.name
sleep(5) # ingreuneaza , testele ar trebui sa fie cat mai rapide
chrome.find_element(By.NAME, "username").send_keys("tomsmith")
chrome.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")
sleep(10)
chrome.quit()#quit inchide de tot fereastra, close inchide doar fereastra