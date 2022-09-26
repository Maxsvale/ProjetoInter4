
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# FUNCÕES DROGASIL
def coletar_preco_drogasil(hotlink = ''):
	driver = webdriver.Chrome()
	driver.get(hotlink)
	preco = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div[2]/span/div'))
	)
	print(preco.text)
	return preco.text
	driver.close()
	
def coletar_drogasil():
	links_drogasil = [
		'https://www.drogasil.com.br/dipirona-sodica-ems-gen-500mg-1x10-comprimidos.html', #dipirona
		'https://www.drogasil.com.br/advil-extra-alivio-400mg-analgesico-blister-com-8-capsulas-gelatinosas.html' #advil
	]
	
	for i in links_drogasil:
		coletar_preco_drogasil(i)

#FUNÇÕES DROGA RAIA

def coletar_preco_drogaraia(hotlink = ''):
	driver = webdriver.Chrome()
	driver.get(hotlink)
	preco = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[3]/div/div[2]/div/div[1]/div[1]/span[2]'))
	)
	print(preco.text)
	return preco.text
	driver.close()	

def coletar_drogaraia():
	links_drogaraia = [
		'https://www.drogaraia.com.br/dipirona-sodica-ems-gen-500mg-1x10-comprimidos.html', #dipirona
		'https://www.drogaraia.com.br/advil-extra-alivio-400mg-analgesico-blister-com-8-capsulas-gelatinosas.html' #advil
	]
	
	for i in links_drogaraia:
		coletar_preco_drogaraia(i)


coletar_drogasil()
coletar_drogaraia()