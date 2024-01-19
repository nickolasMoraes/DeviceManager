from customtkinter import *
from tkinter import *
import os
import subprocess
import threading
import time
from constants import *


#SetCarrier
def set_carrier(checkedDevices):
    base = CTkToplevel() 
    base.geometry("300x200")
    base.title("Set Carrier")
    base.resizable(False, False) 
    label = CTkLabel (base, text = "Enter the ro.carrier:").place(x=95, y=3)
    ro_carrier = CTkEntry(base, width=100)
    ro_carrier.place(x=100, y=30)
    def click_carrier(device, ro_carrier):
        device.switch_working()
        if device.usbType == "FAST":
            subprocess.call(fastboot_path + f'oem config fsg-id "" -s {device.barcode}')
            subprocess.call(fastboot_path + f"erase modemst1 -s {device.barcode}")
            subprocess.call(fastboot_path + f"erase modemst2 -s {device.barcode}")
            subprocess.call(fastboot_path + f'oem config carrier "{ro_carrier}" -s {device.barcode}')
            subprocess.call(fastboot_path + f"erase modemst1 -s {device.barcode}")
            subprocess.call(fastboot_path + f"erase modemst2 -s {device.barcode}")
            erase(device)
            subprocess.call(fastboot_path + f"reboot -s {device.barcode}")
        elif device.usbType == "ADB":
            print(f"The following device is not in Fastboot Mode: {device.barcode}")
        time.sleep(75)
        device.switch_working()
        
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
            
    button = CTkButton(base, text="Set", width=100, command=lambda:set_carrier_threading(checkedDevices, ro_carrier.get())).place(x=100, y=60)
    base.after(100, base.lift)
     
#Setup Jump
def setup_jump(device):
    device.switch_working()
    if device.usbType == "ADB":
        subprocess.call(adb_path + f"-s {device.barcode} shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1")
        subprocess.call(adb_path + f"-s {device.barcode} reboot bootloader")
        subprocess.call(fastboot_path + f"reboot -s {device.barcode}")
    elif device.usbType == "FAST":
        print(f"The following device is not in ADB Mode: {device}")
    device.switch_working()

def setup_jump_threading(checkedDevices):
    for device in checkedDevices:
        if device.isWorking == False:
            thread = threading.Thread(target=lambda:setup_jump(device))
            thread.start()
        else:
            print(f"Device is busy: {device.barcode}")

    
def setup_jump_1(device):
    subprocess.call(adb_path + f"-s {device} shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1")
    subprocess.call(adb_path + f"-s {device} reboot bootloader")
    subprocess.call(fastboot_path + f"reboot -s {device}")

#change SKU
def change_sku(checkedDevices):
    base = CTkToplevel(fg_color="white") 
    base.geometry("300x200") 
    base.title("Set SKU") 
    base.resizable(False, False) 
    label = CTkLabel (base, text = "Enter the SKU:", text_color="black").place(x=95, y=3)
    SKU = CTkEntry (base, fg_color="white", text_color="black", width=100)
    SKU.place(x=100, y=30)
    def click_SKU(device, SKU):
        device.switch_working()
        if device.usbType == "FAST":
            subprocess.call(fastboot_path + f"oem config sku {SKU} -s {device.barcode}")
            subprocess.call(fastboot_path + f"oem config carrier_sku {SKU} -s {device.barcode}")
            subprocess.call(fastboot_path + f"reboot bootloader -s {device.barcode}")
        elif device.usbType == "ADB":
            print(f"The following device is not in Fastboot Mode: {device}")
        device.switch_working()
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
def sim_type(checkedDevices):
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
def sim_type2(checkedDevices):
    base = CTkToplevel(fg_color="white") 
    base.geometry("300x200")  
    base.title("Set SIM Type")
    base.resizable(False, False) 
    option = IntVar(value=0)
    ps = CTkRadioButton (base, text="p-SIM", text_color="black", variable=option, value=1)
    ps.place(x=95, y=30)
    es = CTkRadioButton (base, text="e-SIM", text_color="black", variable=option, value=2)
    es.place(x=95, y=80)

    def change(device, option):
        device.switch_working()
        if device.usbType == "FAST":
            if option == 1:
                subprocess.call(fastboot_path + f"oem hw esim false -s {device.barcode}")
                subprocess.call(fastboot_path + f"erase frp -s {device.barcode}")
                subprocess.call(fastboot_path + f"-w -s {device.barcode}")
                subprocess.call(fastboot_path + f"erase userdata -s {device.barcode}")
                subprocess.call(fastboot_path + f"erase cache -s {device.barcode}")
                subprocess.call(fastboot_path + f"erase modemst1 -s {device.barcode}")
                subprocess.call(fastboot_path + f"erase modemst2 -s {device.barcode}")
                subprocess.call(fastboot_path + f"oem fb_mode_clear -s {device.barcode}")
                subprocess.call(fastboot_path + f'oem config bootmode "" -s {device.barcode}')

            elif option == 2:
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
def erase_mult(device):
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
def erase_threading(checkedDevices):
    for device in checkedDevices:
        if device.isWorking == False:
            thread = threading.Thread(target=lambda:erase_mult(device))
            thread.start()
        else:
            print(f"Device is busy: {device.barcode}")

def erase(device):
    subprocess.call(fastboot_path + f"erase frp -s {device.barcode}")
    subprocess.call(fastboot_path + f"-w -s {device.barcode}")
    subprocess.call(fastboot_path + f"erase userdata -s {device.barcode}")
    subprocess.call(fastboot_path + f"erase cache -s {device.barcode}")
    subprocess.call(fastboot_path + f"erase modemst1 -s {device.barcode}")
    subprocess.call(fastboot_path + f"erase modemst2 -s {device.barcode}")
    subprocess.call(fastboot_path + f"oem fb_mode_clear -s {device.barcode}")
    subprocess.call(fastboot_path + f'oem config bootmode "" -s {device.barcode}')

#Change Radio
def change_radio(checkedDevices):
    base = CTkToplevel(fg_color="white") 
    base.geometry("300x200") 
    base.title("Set RADIO") 
    base.resizable(False, False) 
    label = CTkLabel (base, text = "Enter new RADIO:", text_color="black").place(x=95, y=3)
    radio = CTkEntry (base, fg_color="white", text_color="black", width=100)
    radio.place(x=100, y=30)
    def click_radio(device, radio):
        device.switch_working()
        if device.usbType == "FAST":
            subprocess.call(fastboot_path + f"erase modemst1 -s {device.barcode}")
            subprocess.call(fastboot_path + f"erase modemst2 -s {device.barcode}")
            subprocess.call(fastboot_path + f"oem hw radio {radio} -s {device.barcode}")
            subprocess.call(fastboot_path + f"reboot bootloader -s {device.barcode}")
        elif device.usbType == "ADB":
            print(f"The following devices are not in Fastboot Mode:\n{device}")
            device.switch_working()
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
def fast_mode(device):
    device.switch_working()
    if device.usbType == "ADB":
        subprocess.call(adb_path + f"-s {device.barcode} reboot bootloader")
    elif device.usbType == "FAST":
        print(f"The following devices are not in Fastboot Mode:\n{device}")
    device.switch_working()

def fastboot_mode_threading(checkedDevices):
    for device in checkedDevices:
        if device.isWorking == False:
            thread = threading.Thread(target=lambda:fast_mode(device))
            thread.start()
        else:
            print(f"Device is busy: {device.barcode}")


            





    
