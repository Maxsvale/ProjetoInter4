
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

# FUNCÕES PAGUE MENOS
def coletar_preco_paguemenos(hotlink = ''):
	driver.get(hotlink)
	produto = []
	preco = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[4]/div/div/div/section/div/div/div/div[1]/div[2]/div/div[3]/div/div[5]/div/div[1]/div[1]/div/div[2]/div/div[2]/span/span'))
	)
	nome = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[4]/div/div/div/section/div/div/div/div[1]/div[2]/div/div[3]/div/div[3]/h1/span'))
	)
	print(nome.text)
	print(preco.text)
	produto.append(nome.text)
	produto.append(preco.text)
	print(produto)
	return produto

def coletar_paguemenos():
	links_paguemenos = [
		'https://www.paguemenos.com.br/dipirona-500mg-envelope-com-10-comprimidos-generico-ems/p', #dipirona
		'https://www.paguemenos.com.br/advil-400mg-leve-8-pague-6-capsulas/p', #advil
	]
	paguemenos = []
	for i in links_paguemenos:
		coleta = coletar_preco_paguemenos(i)
		paguemenos.append(coleta)
	print(paguemenos)

#FUNÇÕES DROGA RAIA

def coletar_preco_drogaraia(hotlink = ''):
	driver.get(hotlink)
	produto = []
	preco = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[3]/div/div[2]/div/div[1]/div[1]/span[2]'))
	)
	nome = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[3]/div/div[2]/div/div[2]/div/h1'))
	)
	print(nome.text)
	print(preco.text)
	produto.append(nome.text)
	produto.append(preco.text)
	print(produto)
	return produto

def coletar_drogaraia():
	links_drogaraia = [
		'https://www.drogaraia.com.br/dipirona-sodica-ems-gen-500mg-1x10-comprimidos.html', #dipirona
		'https://www.drogaraia.com.br/advil-extra-alivio-400mg-analgesico-blister-com-8-capsulas-gelatinosas.html' #advil
	]
	drogaraia = []
	for i in links_drogaraia:
		coleta = coletar_preco_drogaraia(i)
		drogaraia.append(coleta)
	print(drogaraia)

#FUNÇÕES DROGARIA SÃO PAULO

def coletar_preco_drogariasp(hotlink = ''):
	driver.get(hotlink)
	produto = []
	preco = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, '//*[@id="inicio-conteudo"]/div[1]/div/div/div[4]/div/div[1]/div[3]/div/p[1]/em[2]/strong'))
	)
	nome = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, '//*[@id="inicio-conteudo"]/div[1]/div/div/div[2]/h1/div'))
	)
	print(nome.text)
	print(preco.text)
	produto.append(nome.text)
	produto.append(preco.text)
	print(produto)
	return produto

def coletar_drogariasp():
	links_drogariasp = [
		'https://www.drogariasaopaulo.com.br/dipirona-sodica-500mg-generico-ems-10-comprimidos/p', #dipirona
		'https://www.drogariasaopaulo.com.br/advil-400mg-8-capsulas/p' #advil
	]
	drogariasp = []
	for i in links_drogariasp:
		coleta = coletar_preco_drogariasp(i)
		drogariasp.append(coleta)


coletar_paguemenos()
coletar_drogaraia()
coletar_drogariasp()


driver.close()