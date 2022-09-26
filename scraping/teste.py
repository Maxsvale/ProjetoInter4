# Vamos utilizar o pacote Selenium Python para manipular browsers via código:
# https://selenium-python.readthedocs.io/
#
# Para isso, ele precisa ser instalado via pip (de preferência com o VS Code fechado):
# python -m pip install selenium
#
# Depois de instalar o Selenium Python, é necessário instalar o driver referente
# ao browser que será utilizado:
#
# Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
# Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# Firefox: https://github.com/mozilla/geckodriver/releases
# Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/
#
# Depois de baixar o driver, garantir que ele seja instalado/descompactado em uma
# pasta que pertença ao PATH global do sistema (de preferência com o VS Code fechado).
#
# No Linux, podem ser as pastas /usr/bin, /usr/local/bin ou outra que esteja no PATH.
# Para adicionar outra pasta ao PATH, basta editar o arquivo ~/.bashrc, e adicionar
# uma linha parecida com essa:
# export PATH=/nova/pasta/para/adicionar:${PATH}
#
# No Windows, o PATH pode ser editado clicando com o botão direito sobre o ícone do
# Computador (no Windows Explorer), depois no menu "Propriedades", em seguida "Configurações
# avançadas do sistema" e, por fim, em "Variáveis de Ambiente".

#s = Service('usr/local/bin/chromedriver')

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

# FUNCÕES DROGASIL
def coletar_preco_drogasil(hotlink = ''):
	driver.get(hotlink)
	preco = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div[2]/span/div'))
	)
	print(preco.text)
	return preco.text
	
def coletar_drogasil():
	links_drogasil = [
		'https://www.drogasil.com.br/dipirona-sodica-ems-gen-500mg-1x10-comprimidos.html', #dipirona
		'https://www.drogasil.com.br/advil-extra-alivio-400mg-analgesico-blister-com-8-capsulas-gelatinosas.html' #advil
	]
	
	for i in links_drogasil:
		coletar_preco_drogasil(i)

#FUNÇÕES DROGA RAIA

def coletar_preco_drogaraia(hotlink = ''):
	driver.get(hotlink)
	preco = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[3]/div/div[2]/div/div[1]/div[1]/span[2]'))
	)
	print(preco.text)
	return preco.text

def coletar_drogaraia():
	links_drogaraia = [
		'https://www.drogaraia.com.br/dipirona-sodica-ems-gen-500mg-1x10-comprimidos.html', #dipirona
		'https://www.drogaraia.com.br/advil-extra-alivio-400mg-analgesico-blister-com-8-capsulas-gelatinosas.html' #advil
	]
	
	for i in links_drogaraia:
		coletar_preco_drogaraia(i)

#FUNÇÕES DROGARIA SÃO PAULO

def coletar_preco_drogariasp(hotlink = ''):
	driver.get(hotlink)
	preco = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, '//*[@id="inicio-conteudo"]/div[1]/div/div/div[4]/div/div[1]/div[3]/div/p[1]/em[2]/strong'))
	)
	print(preco.text)
	return preco.text

def coletar_drogariasp():
	links_drogariasp = [
		'https://www.drogariasaopaulo.com.br/dipirona-sodica-500mg-generico-ems-10-comprimidos/p', #dipirona
		'https://www.drogariasaopaulo.com.br/advil-400mg-8-capsulas/p' #advil
	]
	
	for i in links_drogariasp:
		coletar_preco_drogariasp(i)


coletar_drogasil()
coletar_drogaraia()
coletar_drogariasp()


driver.close()