from customtkinter import * 
import os
import subprocess
from toolsBar_Bottons import *

adb_path = f'"{os.path.dirname(__file__)}\\platform-tools\\adb.exe" '
fastboot_path = f'"{os.path.dirname(__file__)}\\platform-tools\\fastboot.exe" '

class Scripts_Tela(CTkFrame):
    class DeviceButton(CTkButton):
        
        def __init__(self, master, deviceInfo):
            super() .__init__(master, width=270, height=100, fg_color="gray", command=self.click_device)
            self.isChecked = False
            
            self.usbType = deviceInfo[0]
            self.barcode = deviceInfo[1]
            self.secure = deviceInfo[2]
            self.sku = deviceInfo[3]
            self.hw_rev = deviceInfo[4]
            self.carrier = deviceInfo[5]

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
             
            self.configure(text=f'''
Barcode: {self.barcode}
Secure: {self.secure}
SKU: {self.sku}
Hardware rev: {self.hw_rev}
Carrier: {self.carrier}
''')
            
        def click_device(self):
            if not self.isChecked:
                self.configure(fg_color="green")
                self.isChecked = True
            else:
                self.configure(fg_color="gray")
                self.isChecked = False

    def __init__(self, master): 
        super().__init__(master, width=850, height=600, fg_color="#D3D3D3", bg_color="#D3D3D3")
        #widgets 
        self.tools_bar = CTkFrame(self, width=850, height=100, fg_color="#191970", bg_color="#191970")
        self.deviceStatus = CTkFrame(self, width=300, height=500, fg_color="#DCDCDC", bg_color="#DCDCDC")
        self.deviceList = CTkScrollableFrame(self.deviceStatus, width=300, height=450, fg_color="#DCDCDC", bg_color="#DCDCDC")
        self.infoList = CTkFrame(self, width=550, height=100, fg_color="#DCDCDC", bg_color="#DCDCDC")
        self.deviceList_buttons = []
        self.statusFrame = []
    
        #Botão refresh
        self.refreshButton = CTkButton(self.deviceStatus, width=30, text="Refresh Devices", command=self.refresh_device)

        #Botões tools Bar

        self.setCarrier = CTkButton(self.tools_bar, width=150, text="Set Carrier", command=lambda:set_carrier(self.getcheckedDevice()))
        self.changeSKU = CTkButton(self.tools_bar, width=150, text="Change SKU", command=change_sku)
        self.singleSim = CTkButton(self.tools_bar, width=150, text="SS/DS SIM", command=sim_type)
        self.eSim = CTkButton(self.tools_bar, width=150, text="eSIM / pSIM")
        self.changeRadio = CTkButton(self.tools_bar, width=150, text="Change RADIO")
        self.setupJump = CTkButton(self.tools_bar, width=150, text="Setup Jump", command=lambda: setup_jump(self.getcheckedDevice()))
        
        self.erase = CTkButton(self.tools_bar, width=150, text="Erase")
    
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
                adbDevice.append(item.strip("\tdevice"))
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

                adbList.append(adbDevice)
       
        for item in serialFast:
            if item != "":
                fastDevice = []
                fastDevice.append("FAST")
                fastDevice.append(item.strip("\tfastboot"))
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

                fastList.append(fastDevice)
                print(fastList)

        for device in adbList:
            self.deviceList_buttons.append(Scripts_Tela.DeviceButton(self.deviceList, device))

        for device in fastList:
            self.deviceList_buttons.append(Scripts_Tela.DeviceButton(self.deviceList, device))

        for device in self.deviceList_buttons:
            device.pack()
        
        for device in self.statusFrame:
            device.pack()
  
    def getcheckedDevice(self):
        checkedDevices = []
        for device in self.deviceList_buttons:
            if device.isChecked:
                checkedDevices.append(device.barcode)
        return(checkedDevices)
        
class MultF_Tela(CTkFrame): 
    def __init__(self, master): 
        super().__init__(master, width=850, height=600, fg_color="gray", bg_color="gray") 
    #widgets 
    def place(self, **kwargs): 
        return super().place(**kwargs) 
    
    def place_forget(self): 
        for widget in self.place_slaves(): 
            widget.place_forget() 
            return super().place_forget() 

#Funções gerais

        
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