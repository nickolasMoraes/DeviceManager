import subprocess
import requests
import base64
import tarfile
import os
import threading
from urllib import request
from getpass import getpass
from bs4 import BeautifulSoup

# celulares_conectados = []

def call_command(command, suppress_error_msg=False):
    def print_error_msg(e):
        if not suppress_error_msg:
            print(f"\n\t{e.__class__.__name__} running command <" + str(command) + '>:')
            print(f'\t{e}\n')

    def sanitize_output(output_):
        head, _, _ = output_.partition('Finished')
        return head.replace("\\r\\n", "\n").replace("\\n", "\n").strip("b'\n")

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
    except (FileNotFoundError, OSError, subprocess.CalledProcessError) as e:
        print_error_msg(e)
        # output = R.string.build_error_msg(str(e))
    except Exception as e:
        print(f'-- Generic Exception<{e.__class__.__name__}>, should be explicitly added to known possible errors')
        print_error_msg(e)
        # output = R.string.build_error_msg(str(e))

    # return sanitize_output(str(output))
    return True

# user= input("User: ")
# password= getpass("Password: ")

# class Celular:
#     def __init__(self, barcode):
#         self.barcode = barcode

# def listar_celulares_conectados():
#     global celulares_conectados
#     try:
#         # Executar o comando fastboot devices
#         barcode = call_command("fastboot devices")
#         # Dividir a saída em linhas e armazenar em um array
#         celulares_conectados = barcode.replace("\\tfastboot", "").strip().split('\n')[0:]
 
#         if not celulares_conectados:
#             print("Nenhum celular conectado via fastboot.")
#         else:
#             print("Celulares conectados:")
#             for i, celular in enumerate(celulares_conectados, start=1):
#                 print(f"{i}. {celular}")
#                 selecionar_celular()        
#     except subprocess.CalledProcessError as e:
#         print(f"Erro ao executar fastboot devices: {e}")

# def selecionar_celular():
#             # Pedir ao usuário para escolher um celular
#     escolha = int(input("Escolha o número do celular desejado: "))
#     if 1 <= escolha <= len(celulares_conectados):
#         celular_escolhido = celulares_conectados[escolha - 1]
#         print(f"Você escolheu: {celular_escolhido}")
#     else:
#         print("Escolha inválida.")
#     return celular_escolhido

# def transferir_arquivos_thread(celular_escolhido):
#     celular_escolhido = selecionar_celular()
#     # Cria uma thread para a transferência de arquivos
#     thread = threading.Thread(target=main, args=(celular_escolhido,))
#     thread.start()

def main(user_, password_, carrier_, barcode_):
    convert = base64.b64encode(f'{user_}:{password_}'.encode()).decode('ascii')

    product = input('Insira o build name(sem o _g): ')
    version = input('Insira a versao de sw: ')
    url = ("https://artifacts.mot.com/artifactory/" + str(product) + "/" + str(version) + "/")
    payload={}
    headers = {
        'Authorization': f'Basic {convert}'
    }
    ########################################################################################
    #ACESSO E REQUISIÇÃO AO ARTIFACTORY
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
        file_gz= element_list.get_text()
    ########################################################################################
    #BAIXA A BUILD SELECIONADA
    url2 = (url+element_list.get_text())
    opener = request.build_opener()
    opener.addheaders = [('Authorization', f'Basic {convert}')]
    request.install_opener(opener)

    request.urlretrieve(url2, file_gz)
    #########################################################################################
    # carrier_ = input("Insert ro.carrier: ")
    ##############################################################################################
    #extrair build
    # Obtendo o diretório do arquivo
    diretorio_arquivo = os.getcwd()

    caminho_arquivo = (f'{diretorio_arquivo}\\{file_gz}')
 
    # Extraindo o conteúdo do arquivo .tar.gz
    with tarfile.open(caminho_arquivo, 'r:gz') as tar:
        tar.extractall(diretorio_arquivo)

    # Entrando na pasta extraída
    pasta_extraida = os.path.splitext(caminho_arquivo)[0]  # Remove a extensão .tar.gz
    os.chdir(pasta_extraida.replace(".tar", "").replace("fastboot_", ""))
    # Armazenando o caminho na variável
    caminho_final = os.getcwd()
    os.remove(caminho_arquivo)
    caminho_arquivo = 0
    # Exibindo o caminho
    print("Caminho final:", caminho_final)

    def flash_mode(caminho_pasta, carrier):
        try:
            # Mude para a pasta desejada
            os.chdir(caminho_pasta)
            call_command(f"fastboot -s {barcode_} -w")
            call_command(f"fastboot -s {barcode_} erase cache")
            call_command(f"fastboot -s {barcode_} erase userdata")
            call_command(f"fastboot -s {barcode_} erase modemst1")
            call_command(f"fastboot -s {barcode_} erase modemst2 ")
            call_command(f"fastboot -s {barcode_} oem fb_mode_clear")
            call_command(f"fastboot -s {barcode_} oem config bootmode """)
            call_command(f"fastboot -s {barcode_} erase frp")
            call_command(f"fastboot -s {barcode_} oem config carrier {carrier}")

            # Substitua 'seuarquivo.bat' pelo nome do seu arquivo .bat
            os.system(f'flashall.bat /d {barcode_}')
 
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
 
    flash_mode(caminho_final, carrier_)
 
# Chamar a função 
# listar_celulares_conectados()
# celular_escolhido = selecionar_celular()
# transferir_arquivos_thread(celular_escolhido)