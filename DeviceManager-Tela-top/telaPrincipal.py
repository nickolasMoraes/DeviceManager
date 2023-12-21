from customtkinter import * 
import os
import subprocess

adb_path = f'"{os.path.dirname(__file__)}\\platform-tools\\fastboot.exe" '

class Scripts_Tela(CTkFrame):
    class DeviceButton(CTkButton):
        def __init__(self, master, label):
            super() .__init__(master, width=270, height=100, fg_color="gray", text=label, command=self.click_device)
            self.isChecked = False
        
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
        self.deviceList_buttons = []
        
        #Botão refresh
        self.refreshButton = CTkButton(self.deviceStatus, width=30, text="Refresh Devices", command=self.refresh_device)

        #Botões tools Bar
        self.setCarrier = CTkButton(self.tools_bar, width=150, text="Set Carrier", command=self.getcheckedDevice)
        self.changeSKU = CTkButton(self.tools_bar, width=150, text="Change SKU")
        self.singleSim = CTkButton(self.tools_bar, width=150, text="SS/DS SIM")
        self.eSim = CTkButton(self.tools_bar, width=150, text="eSIM / pSIM")
        self.changeRadio = CTkButton(self.tools_bar, width=150, text="Change RADIO")
        self.setupJump = CTkButton(self.tools_bar, width=150, text="Setup Jump")
        self.setupJump = CTkButton(self.tools_bar, width=150, text="Setup Jump")
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

        output = subprocess.getoutput(adb_path + "devices") 
        _serialNumber = output.split("\n")
        print(_serialNumber)

        serialNumber = []
        for item in _serialNumber:
            if item.find("List of") == -1 and item != "" and item.find("daemon") == -1:
                if item.find("unauthorized") == -1:
                    serialNumber.append(item.strip("\tdevice"))

        for device in serialNumber:
            self.deviceList_buttons.append(Scripts_Tela.DeviceButton(self.deviceList, device))

        for device in self.deviceList_buttons:
            device.pack()

    def getcheckedDevice(self):
        checkedDevices = []
        for device in self.deviceList_buttons:
            if device.isChecked:
                checkedDevices.append(device)
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