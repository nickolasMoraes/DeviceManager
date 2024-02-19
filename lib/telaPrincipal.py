from CTkScrollableDropdown import *
from customtkinter import * 
from tkinter import *
import os
import subprocess
import base64
from bs4 import BeautifulSoup
import requests
import sys
import tarfile
import threading
from urllib import request
from constants import *
from PIL import Image
import time
from CTkTable import *


class ProcessLog(CTkFrame):
    def __init__(self, master, title, barcode, ro_carrier=None, option=None, SKU=None, radio=None):
        super().__init__(master, width=550, height=50, fg_color="#F5F5F5", bg_color="#F5F5F5")
        self.title = title
        self.barcode = barcode
        self.ro_carrier = ro_carrier
        self.option = option
        self.sku = SKU
        self.radio = radio
        self.log_Label = []

        if self.ro_carrier != None:
            self.barcode_Label = CTkLabel(self, width=137, height=30, text=self.barcode, justify=RIGHT)
            self.title_Label = CTkLabel(self, width=137, height=30, text=self.title)
            self.process_Label = CTkLabel(self, width=137, height=30, text="Running:", text_color="red")
            self.ro_carrier_label = CTkLabel(self, width=137, height=30, text=ro_carrier)

        elif self.option != None:
            if self.option == 1:
                self.barcode_Label = CTkLabel(self, width=137, height=30, text=self.barcode, justify=RIGHT)
                self.title_Label = CTkLabel(self, width=137, height=30, text=self.title)
                self.process_Label = CTkLabel(self, width=137, height=30, text="Running:", text_color="red")
                self.option_label = CTkLabel(self, width=137, height=30, text="Single SIM")

            elif self.option == 2:
                self.barcode_Label = CTkLabel(self, width=137, height=30, text=self.barcode, justify=RIGHT)
                self.title_Label = CTkLabel(self, width=137, height=30, text=self.title)
                self.process_Label = CTkLabel(self, width=137, height=30, text="Running:", text_color="red")
                self.option_label = CTkLabel(self, width=137, height=30, text="Dual SIM")

            elif self.option == 3:
                self.barcode_Label = CTkLabel(self, width=137, height=30, text=self.barcode, justify=RIGHT)
                self.title_Label = CTkLabel(self, width=137, height=30, text=self.title)
                self.process_Label = CTkLabel(self, width=137, height=30, text="Running:", text_color="red")
                self.option_label = CTkLabel(self, width=137, height=30, text="p-SIM")

            elif self.option == 4:
                self.barcode_Label = CTkLabel(self, width=137, height=30, text=self.barcode, justify=RIGHT)
                self.title_Label = CTkLabel(self, width=137, height=30, text=self.title)
                self.process_Label = CTkLabel(self, width=137, height=30, text="Running:", text_color="red")
                self.option_label = CTkLabel(self, width=137, height=30, text="e-SIM")

            elif self.sku != None:
                self.barcode_Label = CTkLabel(self, width=137, height=30, text=self.barcode, justify=RIGHT)
                self.title_Label = CTkLabel(self, width=137, height=30, text=self.title)
                self.process_Label = CTkLabel(self, width=137, height=30, text="Running:", text_color="red")
                self.sku_label = CTkLabel(self, width=137, height=30, text=self.sku)

        elif radio != None:
                self.barcode_Label = CTkLabel(self, width=137, height=30, text=self.barcode, justify=RIGHT)
                self.title_Label = CTkLabel(self, width=137, height=30, text=self.title)
                self.process_Label = CTkLabel(self, width=137, height=30, text="Running:", text_color="red")
                self.radio_label = CTkLabel(self, width=137, height=30, text=self.radio)

        else:
            self.barcode_Label = CTkLabel(self, width=137, height=30, text=self.barcode, justify=CENTER)
            self.title_Label = CTkLabel(self, width=137, height=30, text=self.title)
            self.process_Label = CTkLabel(self, width=137, height=30, text="Running:", text_color="red")
            self.empty_label = CTkLabel(self, width=137, height=30, text="-")


    def complete_Process(self):
        self.process_Label.configure(text="Complete:", text_color="green")
    
    def pack(self, **kwargs):
        if self.ro_carrier != None:
            self.barcode_Label.pack(side=LEFT)
            self.barcode_Label.pack_propagate(False)
            self.process_Label.pack(side=LEFT)
            self.process_Label.pack_propagate(False)
            self.title_Label.pack(side=LEFT)
            self.title_Label.pack_propagate(False)
            self.ro_carrier_label.pack(side=LEFT)
            self.ro_carrier_label.pack_propagate(False)
        elif self.option != None:
            self.barcode_Label.pack(side=LEFT)
            self.barcode_Label.pack_propagate(False)
            self.process_Label.pack(side=LEFT)
            self.process_Label.pack_propagate(False)
            self.title_Label.pack(side=LEFT)
            self.title_Label.pack_propagate(False)
            self.option_label.pack(side=LEFT)
            self.option_label.pack_propagate(False)
        elif self.sku != None:
            self.barcode_Label.pack(side=LEFT)
            self.barcode_Label.pack_propagate(False)
            self.process_Label.pack(side=LEFT)
            self.process_Label.pack_propagate(False)
            self.title_Label.pack(side=LEFT)
            self.title_Label.pack_propagate(False)
            self.sku_label.pack(side=LEFT)
            self.sku_label.pack_propagate(False)
        elif self.radio != None:
            self.barcode_Label.pack(side=LEFT)
            self.barcode_Label.pack_propagate(False)
            self.process_Label.pack(side=LEFT)
            self.process_Label.pack_propagate(False)
            self.title_Label.pack(side=LEFT)
            self.title_Label.pack_propagate(False)
            self.radio_label.pack(side=LEFT)
            self.radio_label.pack_propagate(False)
        else:
            self.barcode_Label.pack(side=LEFT)
            self.barcode_Label.pack_propagate(False)
            self.process_Label.pack(side=LEFT)
            self.process_Label.pack_propagate(False)
            self.title_Label.pack(side=LEFT)
            self.title_Label.pack_propagate(False)
            self.empty_label.pack(side=LEFT)
            self.empty_label.pack_propagate(False)
        print("processo criado")
        return super().pack(**kwargs) 

class ProcessLog_M(CTkFrame):
    def __init__(self, master, title, element_list, buildId):
        super().__init__(master, width=550, height=50, fg_color="#F5F5F5", bg_color="#F5F5F5")
        self.title = title
        self.buildId = element_list
        self.product = buildId
        
        self.product_label = CTkLabel(self, width=137, height=30, text=self.product, justify=RIGHT)
        self.process_label = CTkLabel(self, width=137, height=30, text="Downloading:", text_color="red")
        self.buildId_label = CTkLabel(self, width=137, height=30, text=self.buildId)
        self.empty_label = CTkLabel(self, width=137, height=30, text="-")
        
    def flash_device(self):
        self.process_label.configure(text="Flashing:", text_color="purple")
    
    def process_complete(self):
        self.process_label.configure(text="complete:", text_color="green")
    
    def process_extract(self):
        self.process_label.configure(text="Extract:", text_color="yellow")

        
    def pack(self, **kwargs):
        self.product_label.pack(side=LEFT)
        self.product_label.pack_propagate()
        self.process_label.pack(side=LEFT)
        self.process_label.pack_propagate()
        self.buildId_label.pack(side=LEFT)
        self.buildId_label.pack_propagate()
        self.empty_label.pack(side=LEFT)
        self.empty_label.pack_propagate()
        return super().pack(**kwargs)
    
class Scripts_Tela(CTkFrame):
    def __init__(self, master, user, password, ): 
        super().__init__(master, width=850, height=600, fg_color="#D3D3D3", bg_color="#D3D3D3")
        self.user = user
        self.password = password
        value = [["Barcode", "Status", "Process", "input" ]]
        #widgets 
        self.tools_bar = CTkFrame(self, width=850, height=100, fg_color="#228B22", bg_color="#228B22")
        self.deviceStatus = CTkFrame(self, width=270, height=500, fg_color="#DCDCDC", bg_color="#DCDCDC")
        self.logFrame = CTkFrame(self, width=580, height=500, fg_color="#DCDCDC", bg_color="#DCDCDC")
        self.logFrame_scroll = CTkScrollableFrame(self.logFrame, width=550, height=500, fg_color="#D3D3D3", bg_color="#D3D3D3")
        self.deviceList = CTkScrollableFrame(self.deviceStatus, width=270, height=450, fg_color="#DCDCDC", bg_color="#DCDCDC")
        self.summary_label = CTkTable(self, row=1, column=4, width=135, values=value)
        self.deviceList_buttons = []
        self.log_Label = []
    
        #Botão refresh
        refresh = CTkImage(Image.open("assets/refresh.png"), size=(45, 45))
        self.refreshButton = CTkButton(self.deviceStatus, width=30, image = refresh, fg_color= "transparent", hover_color = "#DCDCDC", text = None, command=self.refresh_device)

        #botão clear
        clear = CTkImage(Image.open("assets/trash.png"), size=(20, 20))
        self.trashButton = CTkButton(self, width=30, image = clear, bg_color="transparent", fg_color= "transparent", hover_color = "#DCDCDC", text = None, command=self.clear_log)

        #Botões tools Bar
        self.setCarrier = CTkButton(self.tools_bar, width=150, text="Set Carrier", command=lambda:self.set_carrier(self.getcheckedDevice()))
        self.changeSKU = CTkButton(self.tools_bar, width=150, text="Change SKU", command=lambda:self.change_sku(self.getcheckedDevice()))
        self.singleSim = CTkButton(self.tools_bar, width=150, text="SS/DS SIM", command=lambda:self.sim_type(self.getcheckedDevice()))
        self.eSim = CTkButton(self.tools_bar, width=150, text="eSIM / pSIM", command=lambda:self.sim_type2(self.getcheckedDevice()))
        self.changeRadio = CTkButton(self.tools_bar, width=150, text="Change RADIO", command=lambda:self.change_radio(self.getcheckedDevice()))
        self.setupJump = CTkButton(self.tools_bar, width=150, text="Setup Jump", command=lambda: self.setup_jump_threading(self.getcheckedDevice()))
        self.erase_button = CTkButton(self.tools_bar, width=150, text="Erase", command=lambda:self.erase_threading(self.getcheckedDevice()))
        self.fastboot_mode = CTkButton(self.tools_bar, width=150, text="Fastboot Mode", command=lambda:self.fastboot_mode_threading(self.getcheckedDevice()))
        
    
    def place(self, **kwargs): 
        self.tools_bar.place(y=0)
        self.deviceStatus.place(y=100, x=580)
        self.setCarrier.place(y=10, x=10) 
        self.changeSKU.place(y=60, x=10)
        self.singleSim.place(y=10, x=180)
        self.eSim.place(y=60, x=180)
        self.changeRadio.place(y=10, x=350)
        self.setupJump.place(y=60, x=350)
        self.erase_button.place(y=10, x=520)
        self.refreshButton.place(y=4, x=210)
        self.fastboot_mode.place(y=60, x=520)
        self.logFrame.place(y=130, x=0)
        self.logFrame_scroll.place(y=0, x=0)
        self.trashButton.place(y=100, x=530)
        self.summary_label.place(y=100)
        self.deviceList.place(y=80)
        return super().place(**kwargs) 
    
    def clear_log(self):
        for log in self.logFrame_scroll.pack_slaves():
            log.pack_forget()
            log.destroy()

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
                    if secure.find("no") != -1:
                        fastDevice.append("No")
                    elif secure.find("yes") != -1:
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
                checkedDevices.append(device)                
        return(checkedDevices)

    def set_carrier(self, checkedDevices):
        base = CTkToplevel() 
        base.geometry("300x200")
        base.title("Set Carrier")
        base.resizable(False, False) 
        label = CTkLabel (base, text = "Enter the ro.carrier:").place(x=95, y=3)
        ro_carrier = CTkEntry(base, width=100)
        ro_carrier.place(x=100, y=30)
        def click_carrier(device, ro_carrier):
            log = self.start_Process("Set Carrier", device.barcode, ro_carrier)
            device.switch_working()
            if device.usbType == "FAST":
                subprocess.call(fastboot_path + f'oem config fsg-id "" -s {device.barcode}')
                subprocess.call(fastboot_path + f"erase modemst1 -s {device.barcode}")
                subprocess.call(fastboot_path + f"erase modemst2 -s {device.barcode}")
                subprocess.call(fastboot_path + f'oem config carrier "{ro_carrier}" -s {device.barcode}')
                subprocess.call(fastboot_path + f"erase modemst1 -s {device.barcode}")
                subprocess.call(fastboot_path + f"erase modemst2 -s {device.barcode}")
                self.erase(device)
                subprocess.call(fastboot_path + f"reboot -s {device.barcode}")
            elif device.usbType == "ADB":
                print(f"The following device is not in Fastboot Mode: {device.barcode}")
            time.sleep(75)
            device.switch_working()
            log.complete_Process()
            
        #threading set_carrier
        def set_carrier_threading(checkedDevices, ro_carrier):
            for device in checkedDevices:
                if device.isWorking == False:
                    global set_carrier_thread
                    set_carrier_thread = threading.Thread(target=lambda:click_carrier(device, ro_carrier))
                    set_carrier_thread.start()
                else:
                    print(f"Device is busy: {device.barcode}")
            base.destroy()     
        button = CTkButton(base, text="Set", width=100, command=lambda:set_carrier_threading(checkedDevices, ro_carrier.get()))
        button.place(x=100, y=60)
        base.after(100, base.lift)
        
    #Setup Jump
    def setup_jump(self, device):
        log = self.start_Process("Setup Jump", device.barcode)
        device.switch_working()
        if device.usbType == "ADB":
            subprocess.call(adb_path + f"-s {device.barcode} shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1")
            subprocess.call(adb_path + f"-s {device.barcode} reboot bootloader")
            subprocess.call(fastboot_path + f"reboot -s {device.barcode}")
        elif device.usbType == "FAST":
            print(f"The following device is not in ADB Mode: {device}")
        device.switch_working()
        log.complete_Process()

    def setup_jump_threading(self, checkedDevices):
        for device in checkedDevices:
            if device.isWorking == False:
                thread = threading.Thread(target=lambda:self.setup_jump(device))
                thread.start()
            else:
                print(f"Device is busy: {device.barcode}")
        
    def setup_jump_1(self, device):
        subprocess.call(adb_path + f"-s {device} shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1")
        subprocess.call(adb_path + f"-s {device} reboot bootloader")
        subprocess.call(fastboot_path + f"reboot -s {device}")

    #change SKU
    def change_sku(self, checkedDevices):
        base = CTkToplevel(fg_color="white") 
        base.geometry("300x200") 
        base.title("Set SKU") 
        base.resizable(False, False) 
        label = CTkLabel (base, text = "Enter the SKU:", text_color="black").place(x=95, y=3)
        SKU = CTkEntry (base, fg_color="white", text_color="black", width=100)
        SKU.place(x=100, y=30)
        def click_SKU(device, SKU):
            log = self.start_Process("Change SKU", device.barcode, SKU)
            device.switch_working()
            if device.usbType == "FAST":
                subprocess.call(fastboot_path + f"oem config sku {SKU} -s {device.barcode}")
                subprocess.call(fastboot_path + f"oem config carrier_sku {SKU} -s {device.barcode}")
                subprocess.call(fastboot_path + f"reboot bootloader -s {device.barcode}")
            elif device.usbType == "ADB":
                print(f"The following device is not in Fastboot Mode: {device}")
            device.switch_working()
            log.complete_Process()
        def change_SKU_threading(checkedDevices, SKU):
            for device in checkedDevices:
                if device.isWorking == False:
                    thread = threading.Thread(target=lambda:click_SKU(device, SKU))
                    thread.start()
                else:
                    print(f"Device is busy: {device.barcode}")  
            base.destroy()       

        button = CTkButton(base, text="Set", width=100, command=lambda:change_SKU_threading(checkedDevices, SKU.get())).place(x=100, y=60)
        base.after(100, base.lift)
        
    #Dual/Single SIM
    def sim_type(self, checkedDevices):
        base = CTkToplevel(fg_color="white") 
        base.geometry("300x200")  
        base.title("Set SIM Type")
        base.resizable(False, False) 
        option = IntVar(value=0)
        ss = CTkRadioButton (base, text="Single SIM", text_color="black", variable=option, value=1)
        ss.place(x=95, y=30)
        ds = CTkRadioButton (base, text="Dual SIM", text_color="black", variable=option, value=2)
        ds.place(x=95, y=80)
        def change(device, option):
            log = self.start_Process("SS/DS SIM", device.barcode, option=option)
            device.switch_working()
            if device.usbType == "FAST":
                if option == 1:
                    subprocess.call(fastboot_path + f"oem hw dualsim false -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase frp -s {device.barcode}")
                    subprocess.call(fastboot_path + f"-w -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase userdata -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase cache -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase modemst1 -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase modemst2 -s {device.barcode}")
                    subprocess.call(fastboot_path + f"oem fb_mode_clear -s {device.barcode}")
                    subprocess.call(fastboot_path + f'oem config bootmode "" -s {device.barcode}')
                elif option == 2:
                    subprocess.call(fastboot_path + f"oem hw dualsim true -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase frp -s {device.barcode}")
                    subprocess.call(fastboot_path + f"-w -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase userdata -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase cache -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase modemst1 -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase modemst2 -s {device.barcode}")
                    subprocess.call(fastboot_path + f"oem fb_mode_clear -s {device.barcode}")
                    subprocess.call(fastboot_path + f'oem config bootmode "" -s {device.barcode}')
            elif device.usbType == "ADB":
                print(base, text=f"The following device is not in Fastboot Mode: {device}")
            device.switch_working()
            log.complete_Process()
        
        def sim_type_threading(checkedDevices, option):
            for device in checkedDevices:
                if device.isWorking == False:
                    thread = threading.Thread(target=lambda:change(device, option))
                    thread.start()
                else:
                    print(f"Device is busy: {device.barcode}")
            base.destroy()
        button = CTkButton(base, text="Set", width=100, command=lambda:sim_type_threading(checkedDevices, option.get())).place(x=95, y=110)
        base.after(100, base.lift)
        
    #E/P-SIM
    def sim_type2(self, checkedDevices):
        base = CTkToplevel(fg_color="white") 
        base.geometry("300x200")  
        base.title("Set SIM Type")
        base.resizable(False, False) 
        option = IntVar(value=0)
        ps = CTkRadioButton (base, text="p-SIM", text_color="black", variable=option, value=3)
        ps.place(x=95, y=30)
        es = CTkRadioButton (base, text="e-SIM", text_color="black", variable=option, value=4)
        es.place(x=95, y=80)
        def change(device, option):
            log = self.start_Process("Set Carrier", device.barcode, option=option)
            device.switch_working()
            if device.usbType == "FAST":
                if option == 3:
                    subprocess.call(fastboot_path + f"oem hw esim false -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase frp -s {device.barcode}")
                    subprocess.call(fastboot_path + f"-w -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase userdata -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase cache -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase modemst1 -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase modemst2 -s {device.barcode}")
                    subprocess.call(fastboot_path + f"oem fb_mode_clear -s {device.barcode}")
                    subprocess.call(fastboot_path + f'oem config bootmode "" -s {device.barcode}')

                elif option == 4:
                    subprocess.call(fastboot_path + f"fastboot oem hw esim true -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase frp -s {device.barcode}")
                    subprocess.call(fastboot_path + f"-w -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase userdata -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase cache -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase modemst1 -s {device.barcode}")
                    subprocess.call(fastboot_path + f"erase modemst2 -s {device.barcode}")
                    subprocess.call(fastboot_path + f"oem fb_mode_clear -s {device.barcode}")
                    subprocess.call(fastboot_path + f'oem config bootmode "" -s {device.barcode}')
                    
            elif device.usbType == "ADB":
                print(base, text=f"The following device is not in Fastboot Mode:\n{device}")
            device.switch_working()
            log.complete_Process()
        def esim_threading(checkedDevices, option):
            for device in checkedDevices:
                if device.isWorking == False:
                    thread = threading.Thread(target=lambda:change(device, option))
                    thread.start()
                else:
                    print(f"Device is busy: {device.barcode}")
            base.destroy()
        
        button = CTkButton(base, text="Set", width=100, command=lambda:esim_threading(checkedDevices, option.get())).place(x=95, y=110)
        base.after(100, base.lift)

    #erases
    def erase_mult(self, device):
            log = self.start_Process("Erase Device", device.barcode)
            device.switch_working()
            if device.usbType == "FAST":
                subprocess.call(fastboot_path + f"erase frp -s {device.barcode}")
                subprocess.call(fastboot_path + f"-w -s {device.barcode}")
                subprocess.call(fastboot_path + f"erase userdata -s {device.barcode}")
                subprocess.call(fastboot_path + f"erase cache -s {device.barcode}")
                subprocess.call(fastboot_path + f"erase modemst1 -s {device.barcode}")
                subprocess.call(fastboot_path + f"erase modemst2 -s {device.barcode}")
                subprocess.call(fastboot_path + f"oem fb_mode_clear -s {device.barcode}")
                subprocess.call(fastboot_path + f'oem config bootmode "" -s {device.barcode}')
            elif device.usbType == "ADB":
                print(f"The following devices are not in Fastboot Mode:\n{device}")
            device.switch_working()
            log.complete_Process()
    def erase_threading(self, checkedDevices):
        for device in checkedDevices:
            if device.isWorking == False:
                thread = threading.Thread(target=lambda:self.erase_mult(device))
                thread.start()
            else:
                print(f"Device is busy: {device.barcode}")

    def erase(self, device):
        subprocess.call(fastboot_path + f"erase frp -s {device.barcode}")
        subprocess.call(fastboot_path + f"-w -s {device.barcode}")
        subprocess.call(fastboot_path + f"erase userdata -s {device.barcode}")
        subprocess.call(fastboot_path + f"erase cache -s {device.barcode}")
        subprocess.call(fastboot_path + f"erase modemst1 -s {device.barcode}")
        subprocess.call(fastboot_path + f"erase modemst2 -s {device.barcode}")
        subprocess.call(fastboot_path + f"oem fb_mode_clear -s {device.barcode}")
        subprocess.call(fastboot_path + f'oem config bootmode "" -s {device.barcode}')

    #Change Radio
    def change_radio(self, checkedDevices):
        base = CTkToplevel(fg_color="white") 
        base.geometry("300x200") 
        base.title("Set RADIO") 
        base.resizable(False, False) 
        label = CTkLabel (base, text = "Enter new RADIO:", text_color="black").place(x=95, y=3)
        radio = CTkEntry (base, fg_color="white", text_color="black", width=100)
        radio.place(x=100, y=30)
        def click_radio(device, radio):
            log = self.start_Process("Change Radio", device.barcode, radio)
            device.switch_working()
            if device.usbType == "FAST":
                subprocess.call(fastboot_path + f"erase modemst1 -s {device.barcode}")
                subprocess.call(fastboot_path + f"erase modemst2 -s {device.barcode}")
                subprocess.call(fastboot_path + f"oem hw radio {radio} -s {device.barcode}")
                subprocess.call(fastboot_path + f"reboot bootloader -s {device.barcode}")
            elif device.usbType == "ADB":
                print(f"The following devices are not in Fastboot Mode:\n{device}")
                device.switch_working()
                log.complete_Process()
        def change_radio_threading(checkedDevices, radio):
            for device in checkedDevices:
                if device.isWorking == False:
                    thread = threading.Thread(target=lambda:click_radio(device, radio))
                    thread.start()
                else:
                    print(f"Device is busy: {device.barcode}")
            base.destroy()
        button = CTkButton(base, text="Set", width=100, command=change_radio_threading(checkedDevices, radio.get())).place(x=100, y=60)
        base.after(100, base.lift)
                   
    #fastboot mode
    def fast_mode(self, device):
        log = self.start_Process("Fastboot Mode", device.barcode)
        device.switch_working()
        if device.usbType == "ADB":
            subprocess.call(adb_path + f"-s {device.barcode} reboot bootloader")
        elif device.usbType == "FAST":
            print(f"The following devices are not in Fastboot Mode:\n{device}")
        device.switch_working()
        log.complete_Process()

    def fastboot_mode_threading(self, checkedDevices):
        for device in checkedDevices:
            if device.isWorking == False:
                thread = threading.Thread(target=lambda:self.fast_mode(device))
                thread.start()
            else:
                print(f"Device is busy: {device.barcode}")

    def start_Process(self, title, barcode, ro_carrier=None, option=None, SKU=None, radio=None):
        log = ProcessLog(self.logFrame_scroll, title, barcode, ro_carrier, option, SKU, radio)
        self.log_Label.append(log)
        log.pack()
        return log

resultados = ""

class MultF_Tela(CTkFrame): 
    def __init__(self, master, currentUser): 
        super().__init__(master, width=850, height=600, fg_color="#D3D3D3", bg_color="#D3D3D3")
        self.token = currentUser.token
        value = [["Product", "Status", "Build", "progress" ]]

        self.tools_bar = CTkFrame(self, width=850, height=100, fg_color="#228B22", bg_color="#228B22")
        self.deviceStatus = CTkFrame(self, width=300, height=500, fg_color="#DCDCDC", bg_color="#DCDCDC")
        self.deviceList = CTkScrollableFrame(self.deviceStatus, width=300, height=450, fg_color="#DCDCDC", bg_color="#DCDCDC")
        self.summary_label = CTkTable(self, row=1, column=4, width=135, values=value)
        self.logFrame = CTkFrame(self, width=580, height=500, fg_color="#DCDCDC", bg_color="#DCDCDC")
        self.logFrame_scroll = CTkScrollableFrame(self.logFrame, width=545, height=500, fg_color="#D3D3D3", bg_color="#D3D3D3")
        self.deviceList_buttons_mf = []
        self.log_Label = []
        self.commonProduct = ""
        self.checkedDevices = 0
        self.url = "https://artifacts.mot.com/artifactory/"
        self.productId_url = ""

        clear = CTkImage(Image.open("assets/trash.png"), size=(20, 20))
        self.trashButton = CTkButton(self, width=35, image = clear, bg_color="transparent", fg_color="#DCDCDC", hover_color = "#DCDCDC", text = None, command=self.clear_log)

        #Botão refresh
        refresh = CTkImage(Image.open("assets/refresh.png"), size=(45, 45))
        self.refreshButton = CTkButton(self.deviceStatus, width=30, image = refresh, fg_color= "transparent", hover_color = "#DCDCDC", text = None, command=self.refresh_device)

        #labels
        self.product =  CTkEntry(self.tools_bar, width=150, fg_color="white", corner_radius=5)
        fastbootName = CTkImage(Image.open("assets/send.png"), size=(30, 30))
        uplabelimg = CTkImage(Image.open("assets/Update_Label.png"), size=(20, 20))
        self.upLabel = CTkButton(self.product, width=10, height=0, text=None, image=uplabelimg, fg_color=None, hover = None, border_color="gray",corner_radius=4 ,command=lambda:self.upLabel_button(self.product.get()))

        self.fastbootName =  CTkButton(self.tools_bar, width=30, text=None,image=fastbootName , fg_color= "transparent", hover_color = "#191970", command=self.thread_fast)
        
        #Combobox
        self.androidVer_url = ""
        def androidV_callback(value):
            self.androidVer_.set(value=value)
            if self.androidVer_url == "":
                self.url = f'{self.url}{value}'
            else:
                self.url = f'{self.productId_url}{value}'
            self.androidVer_url = self.url
            self.updateBuildId(self.return_url_list())
        self.androidVer_ = CTkComboBox(self.tools_bar, width=150,  button_color="#3CB371")
        self.androidVer_.set("Os Version")
        self.osVer_= CTkScrollableDropdown(self.androidVer_, values = ["Os Version"], justify="left", button_color="transparent",command=androidV_callback, autocomplete=True)

        self.buildId_url = ""
        def buildId_callback(value):
            self.buildId.set(value=value)
            if self.buildId_url == "":
                self.url = f'{self.url}{value}'
            else:
                self.url = f'{self.androidVer_url}{value}'
            self.buildId_url = self.url
            print(self.url)
            self.updateProductName(self.return_url_list())
        self.buildId = CTkComboBox(self.tools_bar, width=150, button_color="#3CB371")
        self.buildId_= CTkScrollableDropdown(self.buildId, width=300, values = ["Build ID"], justify="left", button_color="transparent", command=buildId_callback, autocomplete=True)
        self.buildId.set("Build ID")

        self.productName_url = ""
        def productName_callback(value):
            self.productName.set(value=value)
            if self.productName_url == "":
                self.url = f'{self.url}{value}'
            else:
                self.url = f'{self.buildId_url}{value}'
            self.productName_url = self.url
            print(self.url)
            self.updateuserType(self.return_url_list())
        self.productName = CTkComboBox(self.tools_bar, width=150, button_color="#3CB371")
        self.productName_= CTkScrollableDropdown(self.productName, values = ["Product Name"], justify="left", button_color="transparent", command=productName_callback, autocomplete=True)
        self.productName.set("Product Name")
        

        self.userType_url = ""
        def userType_callback(value):
            self.userType.set(value=value)
            if self.userType_url == "":
                self.url = f'{self.url}{value}'
            else:
                self.url = f'{self.productName_url}{value}'
            self.userType_url = self.url
            print(self.url)
            self.updateCid(self.return_url_list())
        self.userType = CTkComboBox(self.tools_bar, width=150, button_color="#3CB371")
        self.userType_= CTkScrollableDropdown(self.userType, values = ["User Type"], justify="left", button_color="transparent", command= userType_callback, autocomplete=True)
        self.userType.set("User Type")

        self.cidType_url = ""
        def cidType_callback(value):
            self.cidType.set(value=value)
            if self.cidType_url == "":
                self.url = f'{self.url}{value}'
            else:
                self.url = f'{self.userType_url}{value}'
            self.cidType_url = self.url
            print(self.url)
        self.cidType = CTkComboBox(self.tools_bar, width=150, button_color="#3CB371")
        self.cidType_= CTkScrollableDropdown(self.cidType, values = ["CID"], justify="left", button_color="transparent", command= cidType_callback, autocomplete=True)
        self.cidType.set("CID")

        self.roCarrier = CTkEntry(self.tools_bar, width=150, placeholder_text="ro.carrier")

    def fastboot_download(self, checkedDevices, token):
        buildId = self.buildId.get()
        productlabel = self.product.get()
        log = self.start_Process("Build Download", buildId, productlabel)

        headers = {
            'Authorization': f'Basic {token}'
        }
        site = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        self.element_list = soup.select_one("a[href*=fastboot]")
        print(self.element_list)
        if self.element_list == None:
            print("Fastboot build not found")
            return
        for element in self.element_list:
            print(element.get_text())
            print(self.url+self.element_list.get_text())
            print(self.element_list.get_text())
            file_gz= self.element_list.get_text()
            print(file_gz)

        self.nome = self.element_list.get_text()
        self.nome = self.nome.replace(".tar.gz", "")
        self.nome = self.nome.replace("fastboot_", "")

        if(os.path.exists(self.nome)) :
            caminho_final = os.getcwd() + "\\" + self.nome
            print("Arquivo já existe")
        else :
            print("build nao existe")
            #BAIXA A BUILD SELECIONADA
            url2 = (self.url+self.element_list.get_text())
            opener = request.build_opener()
            opener.addheaders = [('Authorization', f'Basic {token}')]
            request.install_opener(opener)

            request.urlretrieve(url2, file_gz)

            diretorio_arquivo = os.getcwd()

            caminho_arquivo = (f'{diretorio_arquivo}\\{file_gz}')
            log.process_extract()
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
                log.process_complete()
        for device in checkedDevices :
            self.flash_mode(caminho_final, self.roCarrier, device)
            log.flash_device()
            log.process_complete()

    def flash_mode(self, caminho_pasta, carrier, fastDevice):
        # print(f"BAIXANDO BUILD DO {fastDevice[1]}")
            try:
                # Mude para a pasta desejada                                       '
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
        
    def thread_fast(self):
        thread = threading.Thread(target=lambda:self.fastboot_download(self.getcheckedDevice(), self.token))
        thread.start()
    
    def getcheckedDevice(self):
        checkedDevices = []
        for device in self.deviceList_buttons_mf:
            if device.isChecked:
                deviceInfo = []
                deviceInfo.append(device.usbType)
                deviceInfo.append(device.barcode)
                deviceInfo.append(device.product)
                deviceInfo.append(device.isWorking)
                
                checkedDevices.append(deviceInfo)                
        return(checkedDevices)
    
    def return_url_list(self):
        print(self.token)
        headers = {
            'Authorization': f'Basic {self.token}'
        }
        site = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        element_list = soup.find_all('a')
        resultados = [element.get_text() for element in element_list]
        print(resultados)
        return resultados
    
    def upLabel_button(self, product):
        self.product_ = product
        print(product)
        self.updateProductLabel(self.product_)
        if self.url.find(self.product_) == -1:

            self.url = f'https://artifacts.mot.com/artifactory/{self.product_}/' 
        print(self.url)
        self.productId_url = self.url
        self.updateAndroidVer(self.return_url_list())
        
    def updateProductLabel(self, product):
        self.commonProduct=product
        self.product.configure(textvariable=product, placeholder_text=product)
        self.updateAndroidVer([])
        self.updateBuildId([])
        self.updateProductName([])
        self.updateuserType([])
        self.updateCid([])

    def updateAndroidVer(self, resultados):
        self.osVer_.configure(values=resultados)
        self.updateBuildId([])
        self.updateProductName([])
        self.updateuserType([])
        self.updateCid([])

    def updateBuildId(self, resultados):
        self.buildId_.configure(values=resultados)
        self.updateProductName([])
        self.updateuserType([])
        self.updateCid([])

    def updateProductName(self, resultados):
        self.productName_.configure(values=resultados)
        self.updateuserType([])
        self.updateCid([])

    def updateuserType(self, resultados):
        self.userType_.configure(values=resultados)
        self.updateCid([])
    
    def updateCid(self, resultados):
        self.cidType_.configure(values=resultados)

    def update_combobox(self):
        global url
        headers = {
        'Authorization': f'Basic {self.token}'
        }

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        element_list = soup.find_all('a')

        resultados2 = [element.get_text() for element in element_list]
        self.buildId['values'] = list(resultados2)

    def on_androidVer_select(self, event):
        global url
        selected_value = self.androidVer_
        url = url + selected_value
        print(url)
        self.update_combobox()
    
    #widgets 
    def clear_log(self):
        for log in self.logFrame_scroll.pack_slaves():
            log.pack_forget()
            log.destroy()

    def place(self, **kwargs):
        self.tools_bar.place(y=0)
        self.deviceStatus.place(y=100, x=550)
        self.refreshButton.place(y=4, x=240)
        self.deviceList.place(y=50)
        self.product.place(y=10, x=10)
        self.androidVer_.place(y=60, x=10)
        self.buildId.place(y=10, x=180)
        self.productName.place(y=60, x=180)
        self.userType.place(y=10, x=350)
        self.cidType.place(y=60, x=350)
        self.roCarrier.place(y=10, x=520)
        self.fastbootName.place(y=55, x=520)
        self.logFrame.place(y=130, x=0)
        self.logFrame_scroll.place(y=0, x=0)
        self.summary_label.place(y=100)
        self.trashButton.place(y=100, x=533)
        self.upLabel.place(y=0, x=122)
        return super().place(**kwargs)

    def place_forget(self): 
        for widget in self.place_slaves(): 
            widget.place_forget() 
            return super().place_forget()
    
    def refresh_device(self):
        # Atualiza a lista de devices
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
                    if secure.find("no") != -1:
                        fastDevice.append("No")
                    elif secure.find("yes") != -1:
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

        for device in adbList:
            self.deviceList_buttons_mf.append(DeviceButton(self.deviceList, device, self))

        for device in fastList:
            self.deviceList_buttons_mf.append(DeviceButton(self.deviceList, device, self))

        for device in self.deviceList_buttons_mf:
            device.pack()
        self.url = "https://artifacts.mot.com/artifactory/"

    def start_Process(self, title, buildId, product):
        log = ProcessLog_M(self.logFrame_scroll, title, buildId, product)
        self.log_Label.append(log)
        log.pack()
        return log

class DeviceButton(CTkButton): 
    def __init__(self, master, deviceInfo, tela: MultF_Tela):
        super() .__init__(master, width=250, height=100, fg_color="#191970", command=self.click_device)
        self.isChecked = False
        self.tela = tela
        
        self.usbType = deviceInfo[0]
        self.barcode = deviceInfo[1]
        self.secure = deviceInfo[2]
        self.sku = deviceInfo[3]
        self.hw_rev = deviceInfo[4]
        self.carrier = deviceInfo[5]
        self.productid = deviceInfo[6]
        self.isWorking = False

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
        device_refresh = CTkImage(Image.open("assets/device_refresh.png"), size = (50, 100))    
        self.configure(image = device_refresh, text=f"Barcode: {self.barcode.strip()}\nSecure: {self.secure}\nSKU: {self.sku}\nHardware rev: {self.hw_rev}\nCarrier: {self.carrier}\nProduct: {self.productid}")
        self._text_label.configure(justify=LEFT, anchor='e', pady=5, padx=10)

    def click_device(self):
        if not self.isWorking:
            if not self.isChecked:
                if type(self.tela) == MultF_Tela:
                    if self.tela.checkedDevices == 0:
                        self.tela.updateProductLabel(self.productid)
                        self.tela.url = f'{self.tela.url}{self.productid}/' 
                        self.tela.productId_url = self.tela.url
                        self.tela.updateAndroidVer(self.tela.return_url_list())
                        self.configure(fg_color="green")
                        self.isChecked = True
                        self.tela.checkedDevices += 1
                    else:
                        if self.tela.commonProduct == self.productid:
                            self.configure(fg_color="green")
                            self.isChecked = True
                            self.tela.checkedDevices += 1
                else:
                    self.configure(fg_color="green")
                    self.isChecked = True
            else:
                if type(self.tela) == MultF_Tela:
                    if self.tela.checkedDevices == 1:
                        self.tela.updateProductLabel("")
                        self.configure(fg_color="#191970")
                        self.isChecked = False
                        self.tela.checkedDevices -= 1
                    elif self.tela.checkedDevices > 1:
                        self.configure(fg_color="#191970")
                        self.isChecked = False
                        self.tela.checkedDevices -= 1
                    self.tela.url = "https://artifacts.mot.com/artifactory/"
                else:
                    self.configure(fg_color="#191970")
                    self.isChecked = False
        else:
            print(f"Device is busy: {self.barcode}")
    
    def switch_working(self):
        if not self.isWorking:
            self.configure(fg_color="yellow")
            self.isWorking = True
        else:
            if self.isChecked:
                self.configure(fg_color="green")
            else:
                self.configure(fg_color="gray")
            self.isWorking = False




      