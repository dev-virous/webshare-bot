#from selenium import webdriver
import undetected_chromedriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://proxy2.webshare.io/register")
time.sleep(5)
WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "email-input"))).send_keys("a7a@gmail.com")
time.sleep(0.7)
WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, ":r1:"))).send_keys("Mhmd@123")
time.sleep(0.7)
WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, ":r2:"))).click()
input("[!] Enter reCAPTCHA and Press ENTER\n")


driver.close()
