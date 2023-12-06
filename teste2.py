import requests
import base64
import tarfile
import os
from urllib import request
from getpass import getpass
from bs4 import BeautifulSoup
import sys

user_= sys.argv[1]
password_= sys.argv[2]

convert = base64.b64encode(f'{user_}:{password_}'.encode()).decode('ascii')

product = input('Insira o build name(sem o _g): ')
version = input('Insira a versao de sw: ')
url = ("https://artifacts.mot.com/artifactory/" + str(product) + "/" + str(version) + "/")
payload={}
headers = {
    'Authorization': f'Basic {convert}'
}
########################################################################################
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
element_list = soup.find_all('a')
for element in element_list:
    print(element.get_text())
########################################################################################
soft = input('Insira o sw: ')
url = ("https://artifacts.mot.com/artifactory/" + str(product) + "/" + str(version) + "/" + str(soft) + "/")
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
element_list = soup.find_all('a')
for element in element_list:
    print(element.get_text())
########################################################################################
targetp = input('Insira o target product: ')
url = ("https://artifacts.mot.com/artifactory/" + str(product) + "/" + str(version) + "/" + str(soft) + "/" + str(targetp) + "/")
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
element_list = soup.find_all('a')
for element in element_list:
    print(element.get_text())
########################################################################################
usertype = input('Insira o user type: ')
url = ("https://artifacts.mot.com/artifactory/" + str(product) + "/" + str(version) + "/" + str(soft) + "/" + str(targetp) + "/" + str(usertype) + "/")
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
element_list = soup.find_all('a')
for element in element_list:
    print(element.get_text())
########################################################################################
release = input('Insira o release type: ')
url = ("https://artifacts.mot.com/artifactory/" + str(product) + "/" + str(version) + "/" + str(soft) + "/" + str(targetp) + "/" + str(usertype) + "/" + str(release) + "/")
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
element_list = soup.select_one("a[href*=fastboot]")
for element in element_list:
    print(url+element_list.get_text())
    print(element_list.get_text())
########################################################################################
url2 = (url+element_list.get_text())
opener = request.build_opener()
opener.addheaders = [('Authorization', f'Basic {convert}')]
request.install_opener(opener)

file = 'build.gz'
request.urlretrieve(url2, file)
#########################################################################################

def obter_caminho_diretorio(arquivo):
    # Obtém o caminho absoluto do diretório atual
    diretorio_atual = os.getcwd()
 
    # Obtém o caminho completo do arquivo no diretório atual
    caminho_completo = os.path.join(diretorio_atual, arquivo)
 
    # Obtém apenas o diretório do caminho completo
    diretorio_do_arquivo = os.path.dirname(caminho_completo)
 
    return diretorio_do_arquivo
 
nome_do_arquivo = (file)
caminho_diretorio = obter_caminho_diretorio(nome_do_arquivo)
 
print(f'O arquivo {nome_do_arquivo} está no diretório: {caminho_diretorio}')

def extrair_arquivo(tar_gz_path, destino):
    try:
        with tarfile.open(tar_gz_path, 'r:gz') as tar:
            tar.extractall(destino)
        print(f"Arquivo {tar_gz_path} extraído com sucesso para {destino}.")
    except Exception as e:
        print(f"Erro ao extrair o arquivo {tar_gz_path}: {e}")
 
# Exemplo de uso
#caminho_arquivo = 'C:/Users/nickolas.costa/Desktop/Teste2/downloaded_file.tar.gz'
diretorio_destino = 'C:/Users/nickolas.costa/Desktop/Teste2'
 
extrair_arquivo(caminho_diretorio+"\\"+nome_do_arquivo, caminho_diretorio)

print("fim")