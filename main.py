import os
from selenium import webdriver
from time import sleep

def main():
    codigoS = input()
    senhaS = input()
    path = os.path.dirname(os.path.realpath(__file__))
    driver = webdriver.Chrome(path + '/chromedriver')
    driver.get('https://stopots.com.br')
    driver.maximize_window()
    driver.implicitly_wait(15)
    anonimo = driver.find_element_by_xpath('/html/body/header/div/div[2]/div/form/button')
    anonimo.click()
    driver.implicitly_wait(15)
    nome = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/input')
    nome.clear()
    sleep(2)
    nome.send_keys('descubrah')
    driver.implicitly_wait(15)
    salaC = driver.find_element_by_xpath('//*[@id="screenHome"]/div[2]/div[2]/button[3]')
    salaC.click()
    buscaS = driver.find_element_by_xpath('//*[@id="search"]')
    buscaS.send_keys(codigoS)
    sleep(2)
    entraS = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[1]/ul/li[1]')
    entraS.click()
    entrar = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/button[2]')
    entrar.click()
    sleep(2)
    if senhaS != '':
        senha = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div[1]/input')
        senha.send_keys(senhaS)
        entrarSenha = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/div[2]/button')
        entrarSenha.click()
    sleep(10)
    driver.implicitly_wait(15)
    while True:
        letra = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[2]/div/ul/li[1]/span')


if __name__ == '__main__':
    main()