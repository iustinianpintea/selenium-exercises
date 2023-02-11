from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()
# chrome.get("https://formy-project.herokuapp.com/")
# sleep(5)
# chrome.find_element(By.XPATH,"/html/body/div/div/li[2]/a").click()
# sleep(3)
# chrome.find_element(By.ID,"btnGroupDrop1").click()
# sleep(5)
# chrome.find_element(By.LINK_TEXT,"Dropdown link 2").click()
# sleep(5)

# chrome.get("https://formy-project.herokuapp.com/")
# sleep(3)
# chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# chrome.find_element(By.CSS_SELECTOR,"body > div > div > li:nth-child(15) > a").click()
# sleep(3)
# chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# chrome.find_element(By.ID,"name").send_keys("Iustinian")
# sleep(2)
# chrome.find_element(By.ID,"date").send_keys("23/07/1996")
# sleep(4)


# chrome.get("https://www.emag.ro/")
# sleep(4)
# chrome.find_element(By.ID, "my_account").click()
# sleep(4)
# chrome.find_element(By.PARTIAL_LINK_TEXT , "Ai nevoie").click()
# sleep(3)





