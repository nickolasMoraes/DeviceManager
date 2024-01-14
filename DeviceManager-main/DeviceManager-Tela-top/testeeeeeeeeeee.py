import tkinter as tk
from tkinter import ttk
import base64
from bs4 import BeautifulSoup
import requests
 
user = ('nmoraes')
password = ('Punick@2024')
convert = base64.b64encode(f'{user}:{password}'.encode()).decode('ascii')
product1 = ('bronco')
url = ("https://artifacts.mot.com/artifactory/" + str(product1) + "/")
payload={}
headers = {
    'Authorization': f'Basic {convert}'
}
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
element_list = soup.find_all('a')
 
resultados = [element.get_text() for element in element_list]

selected_value = ""

def on_combobox_select(event):
    global url
    selected_value = combobox.get()
    print(f"Valor selecionado: {selected_value}")
    url = url + selected_value
    print(url)
    update_combobox()
 
def update_combobox():
    global url

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    element_list = soup.find_all('a')
 
    resultados2 = [element.get_text() for element in element_list]
    combobox2['values'] = list(resultados2)
    
def on_combobox_select2(event):
    global url
    selected_value = combobox2.get()
    print(f"Valor selecionado: {selected_value}")
    url = url + selected_value
    print(url)
    update_combobox2()

resultados3 = ""

def update_combobox2():
    global url
    global resultados3

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    element_list = soup.find_all('a')
 
    resultados3 = [element.get_text() for element in element_list]
    combobox3['values'] = list(resultados3)

def on_combobox_select3(event):
    global url
    selected_value = combobox3.get()
    print(f"Valor selecionado: {selected_value}")
    url = url + selected_value
    print(url)
    update_combobox3()

resultados4 = ""

def update_combobox3():
    global url
    global resultados4

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    element_list = soup.find_all('a')
 
    resultados4 = [element.get_text() for element in element_list]
    combobox4['values'] = list(resultados4)

def on_combobox_select4(event):
    global url
    selected_value = combobox4.get()
    print(f"Valor selecionado: {selected_value}")
    url = url + selected_value
    print(url)
    update_combobox4()

resultados5 = ""

def update_combobox4():
    global url
    global resultados5

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    element_list = soup.find_all('a')
 
    resultados5 = [element.get_text() for element in element_list]
    combobox5['values'] = list(resultados5)

def on_combobox_select5(event):
    global url
    selected_value = combobox5.get()
    print(f"Valor selecionado: {selected_value}")
    url = url + selected_value
    print(url)
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    element_list = soup.select_one("a[href*=fastboot]")
    for element in element_list:
        print(url+element_list.get_text())
        print(element_list.get_text())

# Criar a janela principal
root = tk.Tk()
root.title("teste combobox")
 
# Criar a primeira combobox
combobox = ttk.Combobox(root, values=resultados)
combobox.pack()
 
# Criar a segunda combobox
combobox2 = ttk.Combobox(root)
combobox2.pack()

combobox3 = ttk.Combobox(root, values=resultados3)
combobox3.pack()

combobox4 = ttk.Combobox(root, values=resultados4)
combobox4.pack()

combobox5 = ttk.Combobox(root, values=resultados5)
combobox5.pack()

# Associar o evento de seleção à função on_combobox_select
combobox.bind("<<ComboboxSelected>>", on_combobox_select)

combobox2.bind("<<ComboboxSelected>>", on_combobox_select2)

combobox3.bind("<<ComboboxSelected>>", on_combobox_select3)

combobox4.bind("<<ComboboxSelected>>", on_combobox_select4)

combobox5.bind("<<ComboboxSelected>>", on_combobox_select5)
 
# Iniciar o loop principal da interface gráfica
root.mainloop()