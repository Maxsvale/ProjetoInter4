from dataclasses import replace
from os import rename
import sys
import time
from unicodedata import decimal
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
		'https://www.paguemenos.com.br/engov-com-12-comprimidos/p', #engov
		'https://www.paguemenos.com.br/neosaldina-com-10-drageas/p', #neosaldina
		'https://www.paguemenos.com.br/dorflex-36-comprimidos/p' #dorflex
		'https://www.paguemenos.com.br/novalgina-1g-10-comprimidos/p', #novalgina
		'https://www.paguemenos.com.br/sal-de-fruta-eno-efervescente-2-saches-de-5g/p', #eno
		'https://www.paguemenos.com.br/neosoro-solucao-nasal-adulto-com-30-ml/p', #neosoro
		'https://www.paguemenos.com.br/merthiolate-spray-30ml/p', #mertthiolate
		'https://www.paguemenos.com.br/estomazil-em-po-sem-sabor-5g-com-6-envelope/p', #estomazil
		'https://www.paguemenos.com.br/allegra-60mg-com-10-comprimidos/p', #allegra
		'https://www.paguemenos.com.br/descongestionante-vick-vaporub-30g/p', #vic vaborrub
		'https://www.paguemenos.com.br/polaramine-2mg-caixa-com-20-comprimidos/p', #polaramine
		'https://www.paguemenos.com.br/dramin-b6-com-30-comprimidos/p', #dramin
		'https://www.paguemenos.com.br/espironolactona-25mg-com-30-comprimidos-generico-geolab/p', #espironolactona
		'https://www.paguemenos.com.br/insulina-novolin-r-10ml/p' #insulina
	]
	paguemenos = []
	for i in links_paguemenos:
		coleta = coletar_preco_paguemenos(i)
		paguemenos.append(coleta)
	print(paguemenos)

	return paguemenos

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
		'https://www.drogaraia.com.br/advil-extra-alivio-400mg-analgesico-blister-com-8-capsulas-gelatinosas.html', #advil
		'https://www.drogaraia.com.br/engov-com-12-comprimidos.html', #engov
		'https://www.drogaraia.com.br/neosaldina-1-blister-com-10-drageas.html', #neosaldina
		'https://www.drogaraia.com.br/dorflex-analgesico-36-comprimidos.html', #dorflex
		'https://www.drogaraia.com.br/novalgina-1-grama-10-comprimidos.html', #novalgina
		'https://www.drogaraia.com.br/eno-sal-de-frutas-envelope-regular-5-g.html', #eno
		'https://www.drogaraia.com.br/neosoro-descongestionante-adulto-solucao-30-ml.html', #neosoro
		'https://www.drogaraia.com.br/antisseptico-topico-merthiolate-spray.html', #antisseptico
		'https://www.drogaraia.com.br/estomazil-anti-acido-po-efervescente-sem-sabor-6-envelopes-5g-cada.html', #estomazil
		'https://www.drogaraia.com.br/allegra-60-mg-10-capsulas.html', #allegra
		'https://www.drogaraia.com.br/vick-vaporub-descongestionante-30-g.html', #vick
		'https://www.drogaraia.com.br/polaramine-2-mg-20-comprimidos.html', #polaramine
		'https://www.drogaraia.com.br/dramin-b6-30-comprimidos.html', #dramin
		'https://www.drogaraia.com.br/espironolactona-25mg-eurofarma-generico-30-comprimidos.html', #espirolactona
		'https://www.drogaraia.com.br/novolin-insulina-humana-regular-100ui-10ml-frasco-ampola.html' #insulina
	]
	drogaraia = []
	for i in links_drogaraia:
		coleta = coletar_preco_drogaraia(i)
		drogaraia.append(coleta)
	print(drogaraia)

	return drogaraia

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
		'https://www.drogariasaopaulo.com.br/advil-400mg-8-capsulas/p', #advil
		'https://www.drogariasaopaulo.com.br/engov-15mg-150mg-150mg-50mg-cosmed-12-comprimidos/p', #engov
		'https://www.drogariasaopaulo.com.br/neosaldina-10-drageas/p', #neosaldina
		'https://www.drogariasaopaulo.com.br/analgesico-dorflex-36-comprimidos/p', #dorflex
		'https://www.drogariasaopaulo.com.br/analgesico-novalgina-1g-10-comprimidos/p', #novalgina
		'https://www.drogariasaopaulo.com.br/sal-de-fruta-eno-5g-2-envelopes/p', #eno
		'https://www.drogariasaopaulo.com.br/neosoro-adulto-solucao-nasal-30ml/p', #neosoro
		'https://www.drogariasaopaulo.com.br/antisseptico-topico-merthiolate-spray-30ml/p', #merthiolate
		'https://www.drogariasaopaulo.com.br/antiacido-estomazil-5g-sem-sabor-6-envelopes/p', #estomazil
		'https://www.drogariasaopaulo.com.br/antialergico-allegra-60mg-sanofi-10-comprimidos/p', #allegra
		'https://www.drogariasaopaulo.com.br/vick-vaporub-30g/p', #vick
		'https://www.drogariasaopaulo.com.br/polaramine-2mg-mantecorp-farmasa-20-comprimidos/p', #polaramine
		'https://www.drogariasaopaulo.com.br/dramin-b6-50mg10mg-takeda-30-comprimidos/p', #dramin
		'https://www.drogariasaopaulo.com.br/espironolactona-25mg-generico-eurofarma-30-comprimidos/p', #espirolactona
		'https://www.drogariasaopaulo.com.br/insulina-novolin-n-frasco-ampola-novo-nordisk-10ml/p' #insulina
	]
	drogariasp = []
	for i in links_drogariasp:
		coleta = coletar_preco_drogariasp(i)
		drogariasp.append(coleta)
	return drogariasp

#FUNÇÕES FORMATAÇÃO

def limpar_preco(preco = []):
	preco[1] = preco[1].replace('R$ ','')
	preco[1] = preco[1].replace(',','.')
	preco[1] = float(preco[1])
	return preco

if __name__ == '__main__':
	paguemenos = coletar_paguemenos()
	drogaraia = coletar_drogaraia()
	drogariasp = coletar_drogariasp()


	#print( list(map(lambda p: limpar_preco(p), drogariasp )) )	
	
	paguemenos = list(map(lambda p: limpar_preco(p), paguemenos )) 
	drogaraia = list(map(lambda p: limpar_preco(p), drogaraia )) 
	drogariasp = list(map(lambda p: limpar_preco(p), drogariasp )) 

	print(paguemenos)
	print(drogaraia)
	print(paguemenos)

	driver.close()