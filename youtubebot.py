from selenium import webdriver
from time import sleep
import os

cwd = os.getcwd()
xoli = f'{cwd}'.replace(' \ '.strip(), ('/') )
xoli = xoli + '/geckodriver.exe'
driver = webdriver.Firefox(executable_path=xoli)
driver.get("https://www.youtube.com/watch?v=AWzLP25pm5Q")
sleep(2)
reproduzir = driver.find_element_by_xpath('//Button[@title="Reproduzir (k)"]')
reproduzir.click()
while True:
    sleep(12)
    reiniciar = driver.find_element_by_xpath('//Button[@title="Reiniciar"]')
    reproduzir.click()
