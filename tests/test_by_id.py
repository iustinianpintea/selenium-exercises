#daca functioneaza butonul login
#textele de pe pagina - de facut acasa

# daca ne permite sa scriem caractere speciale

#daca exista limitainferioara/superioara de caractere

#testare negativa
#bagam un usernam cu caactere special
#daca schimbam intre ele username cu parola daca merge
#daca merge sa ne logam cu id/parola gresit

#daca ne logam si delogam si logam iar
#daca dupace ne logam ne raman datele salvate
#daca dam logout si apoi refresh
#textele de pe pagina
#merge linkul de emental selenium


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

sleep(5) # ingreuneaza , testele ar trebui sa fie cat mai rapide
username_input = chrome.find_element(By.ID, "username")
username_input.send_keys("tomsmith")
chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
sleep(10)
chrome.quit()#quit inchide de tot fereastra, close inchide doar fereastra
