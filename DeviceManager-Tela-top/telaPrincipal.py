from customtkinter import * 
import os
import subprocess
from toolsBar_Bottons import *
import base64
from bs4 import BeautifulSoup
import requests
import sys
import tarfile
import threading
from urllib import request

adb_path = f'"{os.path.dirname(__file__)}\\platform-tools\\adb.exe" '
fastboot_path = f'"{os.path.dirname(__file__)}\\platform-tools\\fastboot.exe" '
#user = sys.argv[1]
#password = sys.argv[2]
user = ("nmoraes")
password = ("Punick@2024")


class Scripts_Tela(CTkFrame):
    def __init__(self, master): 
        super().__init__(master, width=850, height=600, fg_color="#D3D3D3", bg_color="#D3D3D3")
        #widgets 
        self.tools_bar = CTkFrame(self, width=850, height=100, fg_color="#191970", bg_color="#191970")
        self.deviceStatus = CTkFrame(self, width=300, height=500, fg_color="#DCDCDC", bg_color="#DCDCDC")
        self.deviceList = CTkScrollableFrame(self.deviceStatus, width=300, height=450, fg_color="#DCDCDC", bg_color="#DCDCDC")
        self.infoList = CTkFrame(self, width=550, height=100, fg_color="#DCDCDC", bg_color="#DCDCDC")
        self.deviceList_buttons = []
    
        #Botão refresh
        self.refreshButton = CTkButton(self.deviceStatus, width=30, text="Refresh Devices", command=self.refresh_device)

        #Botões tools Bar

        self.setCarrier = CTkButton(self.tools_bar, width=150, text="Set Carrier", command=lambda:set_carrier(self.getcheckedDevice()))
        self.changeSKU = CTkButton(self.tools_bar, width=150, text="Change SKU", command=lambda:change_sku(self.getcheckedDevice()))
        self.singleSim = CTkButton(self.tools_bar, width=150, text="SS/DS SIM", command=lambda:sim_type(self.getcheckedDevice()))
        self.eSim = CTkButton(self.tools_bar, width=150, text="eSIM / pSIM", command=lambda:sim_type2(self.getcheckedDevice()))
        self.changeRadio = CTkButton(self.tools_bar, width=150, text="Change RADIO", command=lambda:change_radio(self.getcheckedDevice()))
        self.setupJump = CTkButton(self.tools_bar, width=150, text="Setup Jump", command=lambda: setup_jump(self.getcheckedDevice()))
        self.erase = CTkButton(self.tools_bar, width=150, text="Erase", command=lambda:erase_mult(self.getcheckedDevice()))
        self.fastboot_mode = CTkButton(self.tools_bar, width=150, text="Fastboot Mode", command=lambda:fast_mode(self.getcheckedDevice()))
    
    def place(self, **kwargs): 
        self.tools_bar.place(y=0)
        self.deviceStatus.place(y=100, x=550)
        self.setCarrier.place(y=10, x=10) 
        self.changeSKU.place(y=60, x=10)
        self.singleSim.place(y=10, x=180)
        self.eSim.place(y=60, x=180)
        self.changeRadio.place(y=10, x=350)
        self.setupJump.place(y=60, x=350)
        self.erase.place(y=10, x=520)
        self.refreshButton.place(y=10, x=100)
        self.deviceList.place(y=50)
        self.infoList.place(y=500)
        self.fastboot_mode.place(y=60, x=520)
        

        return super().place(**kwargs) 
    
    def place_forget(self): 
        '''Esquema de transição de telas'''
        for widget in self.place_slaves(): 
            widget.place_forget() 
            return super().place_forget() 

    def refresh_device(self):
        '''Atualiza a lista de devices'''
        while len(self.deviceList_buttons) > 0:
            self.deviceList_buttons[0].destroy()
            self.deviceList_buttons.pop(0)

        output = subprocess.getoutput(adb_path + "devices") # Barcode do Device em ADB
        serialADB = output.split("\n")
       
        _output = subprocess.getoutput(fastboot_path + "devices") # Barcode do Device em Fastboot
        serialFast = _output.split("\n")
      
        adbList = []
        fastList = []
   
        for item in serialADB:
            if item.find("List of") == -1 and item != "" and item.find("daemon") == -1 and item.find("unauthorized") == -1:
                adbDevice = []
                adbDevice.append("ADB")
                adbDevice.append(item.strip("device").strip("\\t"))
                secure = subprocess.getoutput(adb_path + f"-s {adbDevice[1]} shell getprop ro.boot.secure_hardware") # Verifica se o device é seguro/ monta a lista com a infos de un unico device
                if secure.find("no devices") != -1:
                    return
                else:
                    if secure.find("0") != -1:
                        adbDevice.append("No")
                    elif secure.find("1") != -1:
                        adbDevice.append("Yes")
                
                sku = subprocess.getoutput(adb_path + f"-s {adbDevice[1]} shell getprop ro.boot.hardware.sku")
                adbDevice.append(sku)

                hw_rev = subprocess.getoutput(adb_path + f"-s {adbDevice[1]} shell getprop ro.boot.hardware.revision")
                adbDevice.append(hw_rev)

                carrier = subprocess.getoutput(adb_path + f"-s {adbDevice[1]} shell getprop ro.carrier")
                adbDevice.append(carrier)

                product = subprocess.getoutput(adb_path + f"-s {adbDevice[1]} shell getprop ro.build.product")
                adbDevice.append(product)

                adbList.append(adbDevice)
       
        for item in serialFast:
            if item != "":
                fastDevice = []
                fastDevice.append("FAST")
                
                fastDevice.append(item.strip("fastboot").strip("\t"))
                secure = subprocess.getoutput(fastboot_path + f"getvar secure -s {fastDevice[1]}") # Verifica se o device é seguro/ monta a lista com a infos de un unico device
                
                if secure.find("no devices") != -1:
                    return
                else:
                    if secure.find("0") != -1:
                        fastDevice.append("No")
                    elif secure.find("1") != -1:
                        fastDevice.append("Yes")
                
                sku = subprocess.getoutput(fastboot_path + f"getvar sku -s {fastDevice[1]}")
                fastDevice.append(sku[5:sku.find("\n")])

                hw_rev = subprocess.getoutput(fastboot_path + f"getvar hwrev -s {fastDevice[1]}")
                fastDevice.append(hw_rev[6:hw_rev.find("\n")])

                carrier = subprocess.getoutput(fastboot_path + f"getvar ro.carrier -s {fastDevice[1]}")
                fastDevice.append(carrier[12:carrier.find("\n")])

                product = subprocess.getoutput(fastboot_path + f"getvar product -s {fastDevice[1]}")
                fastDevice.append(product[8:product.find("\n")])

                fastList.append(fastDevice)

        for device in adbList:
            self.deviceList_buttons.append(DeviceButton(self.deviceList, device, self))

        for device in fastList:
            self.deviceList_buttons.append(DeviceButton(self.deviceList, device, self))

        for device in self.deviceList_buttons:
            device.pack()
  
    def getcheckedDevice(self):
        checkedDevices = []
        for device in self.deviceList_buttons:
            if device.isChecked:
                deviceInfo = []
                deviceInfo.append(device.usbType)
                deviceInfo.append(device.barcode)
                checkedDevices.append(deviceInfo)                
        return(checkedDevices)

resultados = ""

class MultF_Tela(CTkFrame): 
    def __init__(self, master): 
        super().__init__(master, width=850, height=600, fg_color="gray", bg_color="gray")
        self.tools_bar = CTkFrame(self, width=850, height=100, fg_color="#191970", bg_color="#191970")
        self.deviceStatus = CTkFrame(self, width=300, height=500, fg_color="#DCDCDC", bg_color="#DCDCDC")
        self.deviceList = CTkScrollableFrame(self.deviceStatus, width=300, height=450, fg_color="#DCDCDC", bg_color="#DCDCDC")
        self.infoList = CTkFrame(self, width=550, height=100, fg_color="#DCDCDC", bg_color="#DCDCDC")
        self.deviceList_buttons_mf = []
        self.commonProduct = ""
        self.checkedDevices = 0
        self.url = "https://artifacts.mot.com/artifactory/"
        self.productId_url = ""


        #Botão refresh
        self.refreshButton = CTkButton(self.deviceStatus, width=30, text="Refresh Devices", command=self.refresh_device)

        #labels
        self.product =  CTkLabel(self.tools_bar, width=150, fg_color="white", text="")
        self.fastbootName =  CTkLabel(self.tools_bar, width=200, fg_color="white", text="")
        
        #Combobox
        self.androidVer_url = ""
        def androidV_callback(value):
            if self.androidVer_url == "":
                self.url = f'{self.url}{value}'
            else:
                self.url = f'{self.productId_url}{value}'
            self.androidVer_url = self.url
            print(self.url)
            self.updateBuildId(self.return_url_list())
        self.androidVer_ = CTkComboBox(self.tools_bar, width=150, values=[], command=androidV_callback)
        self.androidVer_.set("OS Version")
        

        self.buildId_url = ""
        def buildId_callback(value):
            if self.buildId_url == "":
                self.url = f'{self.url}{value}'
            else:
                self.url = f'{self.androidVer_url}{value}'
            self.buildId_url = self.url
            print(self.url)
            self.updateProductName(self.return_url_list())
        self.buildId = CTkComboBox(self.tools_bar, width=150, command= buildId_callback)
        self.buildId.set("Build ID")
        

        self.productName_url = ""
        def productName_callback(value):
            if self.productName_url == "":
                self.url = f'{self.url}{value}'
            else:
                self.url = f'{self.buildId_url}{value}'
            self.productName_url = self.url
            print(self.url)
            self.updateuserType(self.return_url_list())
        self.productName = CTkComboBox(self.tools_bar, width=150, command= productName_callback)
        self.productName.set("Product Name")
        

        self.userType_url = ""
        def userType_callback(value):
            if self.userType_url == "":
                self.url = f'{self.url}{value}'
            else:
                self.url = f'{self.productName_url}{value}'
            self.userType_url = self.url
            print(self.url)
            self.updateCid(self.return_url_list())
        self.userType = CTkComboBox(self.tools_bar, width=150, command= userType_callback)
        self.userType.set("User Type")

        self.cidType_url = ""
        def cidType_callback(value):
            if self.cidType_url == "":
                self.url = f'{self.url}{value}'
            else:
                self.url = f'{self.userType_url}{value}'
            self.cidType_url = self.url
            print(self.url)
            fastboot_download()
        self.cidType = CTkComboBox(self.tools_bar, width=150, command= cidType_callback)
        self.cidType.set("CID")

        self.roCarrier = CTkEntry(self.tools_bar, width=150)

        self.element_list = ""
        def fastboot_download():
            convert = base64.b64encode(f'{user}:{password}'.encode()).decode('ascii')
            headers = {
                'Authorization': f'Basic {convert}'
            }
            site = requests.get(self.url, headers=headers)
            soup = BeautifulSoup(site.content, 'html.parser')
            self.element_list = soup.select_one("a[href*=fastboot]")
            for element in self.element_list:
                print(self.url+self.element_list.get_text())
                print(self.element_list.get_text())
                file_gz= self.element_list.get_text()
                print(file_gz)

            nome = self.element_list.get_text()
            nome = nome.replace(".tar.gz", "")
            nome = nome.replace("fastboot_", "")

            if(os.path.exists(nome)) :
                caminho_final = os.getcwd() + "\\" + nome
                print("Arquivo já existe")
            else :
                #BAIXA A BUILD SELECIONADA
                url2 = (self.url+self.element_list.get_text())
                opener = request.build_opener()
                opener.addheaders = [('Authorization', f'Basic {convert}')]
                request.install_opener(opener)

                request.urlretrieve(url2, file_gz)

                diretorio_arquivo = os.getcwd()

                caminho_arquivo = (f'{diretorio_arquivo}\\{file_gz}')
 
                # Extraindo o conteúdo do arquivo .tar.gz
                with tarfile.open(caminho_arquivo, 'r:gz') as tar:
                    tar.extractall(diretorio_arquivo)
                    request.urlretrieve(url2, file_gz)

                    diretorio_arquivo = os.getcwd()

                    caminho_arquivo = (f'{diretorio_arquivo}\\{file_gz}')

                    # Entrando na pasta extraída
                    pasta_extraida = os.path.splitext(caminho_arquivo)[0]  
                    # Remove a extensão .tar.gz
                    os.chdir(pasta_extraida.replace(".tar", "").replace("fastboot_", ""))
            
                    # Armazenando o caminho na variável
                    caminho_final = os.getcwd()
                    os.remove(caminho_arquivo)
                    caminho_arquivo = 0

            print("Caminho final:", caminho_final)

            def flash_mode(caminho_pasta, carrier):
                try:
                    # Mude para a pasta desejada
                    os.chdir(caminho_pasta)
                    subprocess.getoutput(fastboot_path + f" -s {fastDevice[1]} -w")
                    subprocess.getoutput(fastboot_path + f" -s {fastDevice[1]} erase cache")
                    subprocess.getoutput(fastboot_path + f" -s {fastDevice[1]} erase userdata")
                    subprocess.getoutput(fastboot_path + f" -s {fastDevice[1]} erase modemst1")
                    subprocess.getoutput(fastboot_path + f" -s {fastDevice[1]} erase modemst2")
                    subprocess.getoutput(fastboot_path + f" -s {fastDevice[1]} oem fb_mode_clear")
                    subprocess.getoutput(fastboot_path + f" -s {fastDevice[1]} oem config bootmode """)
                    subprocess.getoutput(fastboot_path + f" -s {fastDevice[1]} erase frp")
                    subprocess.getoutput(fastboot_path + f" -s {fastDevice[1]} oem config carrier {carrier}")

                    os.system(f'flashall.bat /d {fastDevice[1]}')
    
                except Exception as e:
                    print(f"Ocorreu um erro: {e}")

            flash_mode(caminho_final, self.roCarrier)
        

    def getcheckedDevice(self):
        checkedDevices = []
        for device in self.deviceList_buttons_mf:
            if device.isChecked:
                deviceInfo = []
                deviceInfo.append(device.usbType)
                deviceInfo.append(device.barcode)
                deviceInfo.append(device.product)
                checkedDevices.append(deviceInfo)                
        return(checkedDevices)
    
    def return_url_list(self):
        convert = base64.b64encode(f'{user}:{password}'.encode()).decode('ascii')
        headers = {
            'Authorization': f'Basic {convert}'
        }
        site = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        element_list = soup.find_all('a')
        resultados = [element.get_text() for element in element_list]
        return resultados

   

    def updateProductLabel(self, product):
        self.commonProduct=product
        self.product.configure(text=product)
        self.updateAndroidVer([])
        self.updateBuildId([])
        self.updateProductName([])
        self.updateuserType([])
        self.updateCid([])

    def updateAndroidVer(self, resultados):
        self.androidVer_.configure(values=resultados)
        self.updateBuildId([])
        self.updateProductName([])
        self.updateuserType([])
        self.updateCid([])

    def updateBuildId(self, resultados):
        self.buildId.configure(values=resultados)
        self.updateProductName([])
        self.updateuserType([])
        self.updateCid([])

    def updateProductName(self, resultados):
        self.productName.configure(values=resultados)
        self.updateuserType([])
        self.updateCid([])

    def updateuserType(self, resultados):
        self.userType.configure(values=resultados)
        self.updateCid([])
    
    def updateCid(self, resultados):
        self.cidType.configure(values=resultados)
        

    def update_combobox(self):
        global url
        convert = base64.b64encode(f'{user}:{password}'.encode()).decode('ascii')
        headers = {
        'Authorization': f'Basic {convert}'
        }

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        element_list = soup.find_all('a')

        resultados2 = [element.get_text() for element in element_list]
        self.buildId['values'] = list(resultados2)

    def on_androidVer_select(self, event):
        global url
        selected_value = self.androidVer
        url = url + selected_value
        print(url)
        self.update_combobox()
    
    #widgets 
    def place(self, **kwargs):
        self.tools_bar.place(y=0)
        self.deviceStatus.place(y=100, x=550)
        self.refreshButton.place(y=10, x=100)
        self.deviceList.place(y=50)
        self.infoList.place(y=500)
        self.product.place(y=10, x=10)
        self.androidVer_.place(y=60, x=10)
        self.buildId.place(y=10, x=180)
        self.productName.place(y=60, x=180)
        self.userType.place(y=10, x=350)
        self.cidType.place(y=60, x=350)
        self.roCarrier.place(y=10, x=520)
        self.fastbootName.place(y=60, x=520)
        return super().place(**kwargs)

    def place_forget(self): 
        for widget in self.place_slaves(): 
            widget.place_forget() 
            return super().place_forget()
    
    def refresh_device(self):
        '''Atualiza a lista de devices'''
        while len(self.deviceList_buttons_mf) > 0:
            self.deviceList_buttons_mf[0].destroy()
            self.deviceList_buttons_mf.pop(0)
        self.updateProductLabel("")
        self.checkedDevices = 0

        output = subprocess.getoutput(adb_path + "devices") # Barcode do Device em ADB
        serialADB = output.split("\n")
       
        _output = subprocess.getoutput(fastboot_path + "devices") # Barcode do Device em Fastboot
        serialFast = _output.split("\n")
      
        adbList = []
        fastList = []
   
        for item in serialADB:
            if item.find("List of") == -1 and item != "" and item.find("daemon") == -1 and item.find("unauthorized") == -1:
                adbDevice = []
                adbDevice.append("ADB")
                adbDevice.append(item.strip("device").strip("\\t"))
                secure = subprocess.getoutput(adb_path + f"-s {adbDevice[1]} shell getprop ro.boot.secure_hardware") # Verifica se o device é seguro/ monta a lista com a infos de un unico device
                if secure.find("no devices") != -1:
                    return
                else:
                    if secure.find("0") != -1:
                        adbDevice.append("No")
                    elif secure.find("1") != -1:
                        adbDevice.append("Yes")
                
                sku = subprocess.getoutput(adb_path + f"-s {adbDevice[1]} shell getprop ro.boot.hardware.sku")
                adbDevice.append(sku)

                hw_rev = subprocess.getoutput(adb_path + f"-s {adbDevice[1]} shell getprop ro.boot.hardware.revision")
                adbDevice.append(hw_rev)

                carrier = subprocess.getoutput(adb_path + f"-s {adbDevice[1]} shell getprop ro.carrier")
                adbDevice.append(carrier)

                product = subprocess.getoutput(adb_path + f"-s {adbDevice[1]} shell getprop ro.build.product")
                adbDevice.append(product)

                adbList.append(adbDevice)
       
        for item in serialFast:
            if item != "":
                fastDevice = []
                fastDevice.append("FAST")
                
                fastDevice.append(item.strip("fastboot").strip("\t"))
                secure = subprocess.getoutput(fastboot_path + f"getvar secure -s {fastDevice[1]}") # Verifica se o device é seguro/ monta a lista com a infos de un unico device
                
                if secure.find("no devices") != -1:
                    return
                else:
                    if secure.find("0") != -1:
                        fastDevice.append("No")
                    elif secure.find("1") != -1:
                        fastDevice.append("Yes")
                
                sku = subprocess.getoutput(fastboot_path + f"getvar sku -s {fastDevice[1]}")
                fastDevice.append(sku[5:sku.find("\n")])

                hw_rev = subprocess.getoutput(fastboot_path + f"getvar hwrev -s {fastDevice[1]}")
                fastDevice.append(hw_rev[6:hw_rev.find("\n")])

                carrier = subprocess.getoutput(fastboot_path + f"getvar ro.carrier -s {fastDevice[1]}")
                fastDevice.append(carrier[12:carrier.find("\n")])

                product = subprocess.getoutput(fastboot_path + f"getvar product -s {fastDevice[1]}")
                fastDevice.append(product[9:product.find("\n")])

                fastList.append(fastDevice)
        print(fastList)
        print(adbList)

        for device in adbList:
            self.deviceList_buttons_mf.append(DeviceButton(self.deviceList, device, self))

        for device in fastList:
            self.deviceList_buttons_mf.append(DeviceButton(self.deviceList, device, self))

        for device in self.deviceList_buttons_mf:
            device.pack()
        self.url = "https://artifacts.mot.com/artifactory/"

class DeviceButton(CTkButton):
    
    def __init__(self, master, deviceInfo, tela: MultF_Tela):
        super() .__init__(master, width=270, height=100, fg_color="gray", command=self.click_device)
        self.isChecked = False

        self.tela = tela

        
        self.usbType = deviceInfo[0]
        self.barcode = deviceInfo[1]
        self.secure = deviceInfo[2]
        self.sku = deviceInfo[3]
        self.hw_rev = deviceInfo[4]
        self.carrier = deviceInfo[5]
        self.product = deviceInfo[6]


        #Informações adicionais
        
        if self.usbType == "ADB": #Fingerprint de ADB/ if para coletar os dados em cada modo de usb
            self.fingerP = subprocess.getoutput(adb_path + f"-s {self.barcode} shell getprop ro.build.fingerprint")
        
##########################################################################################################################################
        #Fingerprint de Fastboot/ if para coletar os dados em cada modo de usb
        elif self.usbType == "FAST": 
            _fingerP = subprocess.getoutput(fastboot_path + f"getvar ro.build.fingerprint -s {self.barcode}").split("\n")

            self.fingerP = ""
            for line in _fingerP:
                if line.find("Done") != -1:
                    break
                self.fingerP += line[line.find(":")+2:]
##########################################################################################################################################
        #cid
            self.cid = ""
            cid_= subprocess.getoutput(fastboot_path + f"getvar cid -s {self.barcode}")
            self.cid = cid_[5:cid_.find("\n")]
            
##########################################################################################################################################
        #Channel ID
            self.channelid = ""
            channelid_= subprocess.getoutput(fastboot_path + f"getvar channelid -s {self.barcode}")
            self.channelid = channelid_[11:channelid_.find("\n")]
            
##########################################################################################################################################
        #Radio
            self.radio = ""
            radio_ = subprocess.getoutput(fastboot_path + f"getvar radio -s {self.barcode}")
            self.radio = radio_[7:radio_.find("\n")]

##########################################################################################################################################
            
        self.configure(text=f'Barcode: {self.barcode}\nSecure: {self.secure}\nSKU: {self.sku}\nHardware rev: {self.hw_rev}\nCarrier: {self.carrier}\nProduct: {self.product}')
        
    def click_device(self):
            if not self.isChecked:
                if type(self.tela) == MultF_Tela:
                    if multF_tela.checkedDevices == 0:
                        multF_tela.updateProductLabel(self.product)
                        self.tela.url = f'{self.tela.url}{self.product}/' 
                        self.tela.productId_url = self.tela.url
                        multF_tela.updateAndroidVer(self.tela.return_url_list())
                        self.configure(fg_color="green")
                        self.isChecked = True
                        multF_tela.checkedDevices += 1
                    else:
                        if multF_tela.commonProduct == self.product:
                            self.configure(fg_color="green")
                            self.isChecked = True
                            multF_tela.checkedDevices += 1
                else:
                    self.configure(fg_color="green")
                    self.isChecked = True
            else:
                if type(self.tela) == MultF_Tela:
                    if multF_tela.checkedDevices == 1:
                        multF_tela.updateProductLabel("")
                        self.configure(fg_color="gray")
                        self.isChecked = False
                        multF_tela.checkedDevices -= 1
                    elif multF_tela.checkedDevices > 1:
                        self.configure(fg_color="gray")
                        self.isChecked = False
                        multF_tela.checkedDevices -= 1
                    self.tela.url = "https://artifacts.mot.com/artifactory/"
                else:
                    self.configure(fg_color="gray")
                    self.isChecked = False
    
base = CTk() 
base.geometry("1000x600") 
base._set_appearance_mode("dark") 
base.title("Motorola Device Manager") 
base.resizable(False, False) 
        
multF_tela = MultF_Tela(base) 
scripts_tela = Scripts_Tela(base) 

#Transição de Telas
def hide_tabs(): 
    multF_tela.place_forget() 
    scripts_tela.place_forget() 

def show_multF(): 
    hide_tabs() 
    multF_tela.place(x=150) 

def show_scripts(): 
    hide_tabs() 
    scripts_tela.place(x=150) 

#Frames Principais
menuLateral = CTkFrame(base, width=150, height=600, fg_color="#191970", bg_color="#191970").place(x=0) 
multflash = CTkButton(menuLateral, text="MultiFlash", width=150, height=80, fg_color="#191970", bg_color="#191970", command=show_multF).place(x=0) 
Scripts = CTkButton(menuLateral, text="Tools", width=150, height=80, fg_color="#191970", bg_color="#191970", command=show_scripts).place(x=0, y=80) 
multF_tela.place(x=150) 


base.mainloop()