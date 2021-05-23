from selenium import webdriver
from time import sleep
import os

cwd = os.getcwd()
xoli = f'{cwd}'.replace(' \ '.strip(), ('/') )
xoli = xoli + '/geckodriver.exe'
driver = webdriver.Firefox(executable_path=xoli)

while True:
    try:
        tmp = int(input("Digite os segundos do vídeo: ")) + 2
    except:
        print("\033[31mERRO! Numero inválido\033[m")
    else:
        break


while True:
    try:
        url = str(input("Escreva a URL: "))
        driver.get(f"{url}")
    except:
        print("\033[31mError! Tem certeza que eessa é a URL?\033[m")
    else:
        driver.get(f"{url}")


sleep(10)
reproduzir = driver.find_element_by_xpath('//Button[@title="Reproduzir (k)"]')
reproduzir.click()
while True:
    sleep(tmp)
    reiniciar = driver.find_element_by_xpath('//Button[@title="Reiniciar"]')
    reproduzir.click()