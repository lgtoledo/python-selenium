import time
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("http://localhost:8109")
elemento1 = driver.find_element(By.ID, "user")
elemento1.clear()
elemento1.send_keys("root")

elemento2 = driver.find_element(By.NAME, "pass")
elemento2.clear()
elemento2.send_keys("password")

driver.find_element(By.XPATH, "//div[3]/div/input").click()
driver.get("http://localhost:8109")
time.sleep(20)

# Crear nuevo ticket
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[6]/form[2]/div[1]/input").click()
campoAsunto = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[1]/div[2]/div[1]/div/div[2]/div/div/div[4]/div[2]/input")
campoAsunto.send_keys("prueba de asunto del ticket")

# pulso en botón Crear
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[1]/div[2]/div[2]/div/div/div[2]/input").click()
time.sleep(10)
driver.close()