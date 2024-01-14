from customtkinter import *
from tkinter import *
import os
import subprocess

fastboot_path = f'"{os.path.dirname(__file__)}\\platform-tools\\fastboot.exe" '
adb_path = f'"{os.path.dirname(__file__)}\\platform-tools\\adb.exe" '

#SetCarrier
def set_carrier(checkedDevices):
    base = CTkToplevel() 
    base.geometry("300x200")
    base.title("Set Carrier")
    base.resizable(False, False) 
    label = CTkLabel (base, text = "Enter the ro.carrier:").place(x=95, y=3)
    ro_carrier = CTkEntry(base, width=100)
    ro_carrier.place(x=100, y=30)
    def click_carrier():
        skipDevices = []
        for device in checkedDevices:
            if device[0] == "FAST":
                subprocess.call(fastboot_path + f'oem config fsg-id "" -s {device[1]}')
                subprocess.call(fastboot_path + f"erase modemst1 -s {device[1]}")
                subprocess.call(fastboot_path + f"erase modemst2 -s {device[1]}")
                subprocess.call(fastboot_path + f'oem config carrier "{ro_carrier.get()}" -s {device[1]}')
                subprocess.call(fastboot_path + f"erase modemst1 -s {device[1]}")
                subprocess.call(fastboot_path + f"erase modemst2 -s {device[1]}")
                erase_mult(device[1])
                subprocess.call(fastboot_path + f"reboot -s {device[1]}")
            elif device[0] == "ADB":
                skipDevices.append(device[1])
        if len(skipDevices) > 0:
            deviceList = ""
            for device in skipDevices:
                deviceList += f"{device}\n"
            CTkLabel(base, text=f"The following devices are not in Fastboot Mode:\n{deviceList}").place(x=10, y=120)
        else:
            CTkLabel (base, text = "Finished", text_color="green").place(x=120, y=130)
    button = CTkButton(base, text="Set", width=100, command=click_carrier).place(x=100, y=60)
    base.after(100, base.lift)
    
#Setup Jump
def setup_jump(checkedDevices):
    skipDevices = []
    for device in checkedDevices:
        if device[0] == "ADB":
            subprocess.call(adb_path + f"-s {device[1]} shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1")
            subprocess.call(adb_path + f"-s {device[1]} reboot bootloader")
            subprocess.call(fastboot_path + f"reboot -s {device[1]}")
        elif device[0] == "FAST":
                skipDevices.append(device[1])
        if len(skipDevices) > 0:
            deviceList = ""
            for device in skipDevices:
                deviceList += f"{device}\n"
            CTkLabel(text=f"The following devices are not in Fastboot Mode:\n{deviceList}").place(x=90, y=120)

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
    def click_SKU():
        skipDevices = []
        for device in checkedDevices:
            if device[0] == "FAST":
                subprocess.call(fastboot_path + f"oem config sku {SKU.get()} -s {device[1]}")
                subprocess.call(fastboot_path + f"oem config carrier_sku {SKU.get()} -s {device[1]}")
                subprocess.call(fastboot_path + f"reboot bootloader -s {device[1]}")
            elif device[0] == "ADB":
                skipDevices.append(device[1])
        if len(skipDevices) > 0:
            deviceList = ""
            for device in skipDevices:
                deviceList += f"{device}\n"
            CTkLabel(base, text=f"The following devices are not in Fastboot Mode:\n{deviceList}").place(x=90, y=120)
        
        finished = CTkLabel (base, text = "Finished", text_color="green").place(x=120, y=130)

    button = CTkButton(base, text="Set", width=100, command=click_SKU).place(x=100, y=60)
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
    def change():
        for device in checkedDevices:
            skipDevices = []
            if device[0] == "FAST":
                if option.get() == 1:
                    subprocess.call(fastboot_path + f"oem hw dualsim false -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase frp -s {device[1]}")
                    subprocess.call(fastboot_path + f"-w -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase userdata -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase cache -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase modemst1 -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase modemst2 -s {device[1]}")
                    subprocess.call(fastboot_path + f"oem fb_mode_clear -s {device[1]}")
                    subprocess.call(fastboot_path + f'oem config bootmode "" -s {device[1]}')
                    finished = CTkLabel (base, text = "Finished", text_color="green").place(x=120, y=160)
                elif option.get() == 2:
                    subprocess.call(fastboot_path + f"oem hw dualsim true -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase frp -s {device[1]}")
                    subprocess.call(fastboot_path + f"-w -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase userdata -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase cache -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase modemst1 -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase modemst2 -s {device[1]}")
                    subprocess.call(fastboot_path + f"oem fb_mode_clear -s {device[1]}")
                    subprocess.call(fastboot_path + f'oem config bootmode "" -s {device[1]}')
                    finished = CTkLabel (base, text = "Finished", text_color="green").place(x=120, y=160)
            elif device[0] == "ADB":
                skipDevices.append(device[1])
        if len(skipDevices) > 0:
            deviceList = ""
            for device in skipDevices:
                deviceList += f"{device}\n"
            CTkLabel(base, text=f"The following devices are not in Fastboot Mode:\n{deviceList}").place(x=90, y=120)
    button = CTkButton(base, text="Set", width=100, command=change).place(x=95, y=110)
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

    def change():
        for device in checkedDevices:
            skipDevices = []
            if device[0] == "FAST":
                if option.get() == 1:
                    subprocess.call(fastboot_path + f"oem hw esim false -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase frp -s {device[1]}")
                    subprocess.call(fastboot_path + f"-w -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase userdata -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase cache -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase modemst1 -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase modemst2 -s {device[1]}")
                    subprocess.call(fastboot_path + f"oem fb_mode_clear -s {device[1]}")
                    subprocess.call(fastboot_path + f'oem config bootmode "" -s {device[1]}')
                    finished = CTkLabel (base, text = "Finished", text_color="green").place(x=120, y=160)
                elif option.get() == 2:
                    subprocess.call(fastboot_path + f"fastboot oem hw esim true -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase frp -s {device[1]}")
                    subprocess.call(fastboot_path + f"-w -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase userdata -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase cache -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase modemst1 -s {device[1]}")
                    subprocess.call(fastboot_path + f"erase modemst2 -s {device[1]}")
                    subprocess.call(fastboot_path + f"oem fb_mode_clear -s {device[1]}")
                    subprocess.call(fastboot_path + f'oem config bootmode "" -s {device[1]}')
                    finished = CTkLabel (base, text = "Finished", text_color="green").place(x=120, y=160)
            elif device[0] == "ADB":
                skipDevices.append(device[1])
        if len(skipDevices) > 0:
            deviceList = ""
            for device in skipDevices:
                deviceList += f"{device}\n"
            CTkLabel(base, text=f"The following devices are not in Fastboot Mode:\n{deviceList}").place(x=90, y=120)
    
    button = CTkButton(base, text="Set", width=100, command=change).place(x=95, y=110)
    base.after(100, base.lift)

#erases
def erase_mult(checkedDevices):
    for device in checkedDevices:
        skipDevices = []
        if device[0] == "FAST":
            subprocess.call(fastboot_path + f"erase frp -s {device[1]}")
            subprocess.call(fastboot_path + f"-w -s {device[1]}")
            subprocess.call(fastboot_path + f"erase userdata -s {device[1]}")
            subprocess.call(fastboot_path + f"erase cache -s {device[1]}")
            subprocess.call(fastboot_path + f"erase modemst1 -s {device[1]}")
            subprocess.call(fastboot_path + f"erase modemst2 -s {device[1]}")
            subprocess.call(fastboot_path + f"oem fb_mode_clear -s {device[1]}")
            subprocess.call(fastboot_path + f'oem config bootmode "" -s {device[1]}')
        elif device[0] == "ADB":
                skipDevices.append(device[1])
        if len(skipDevices) > 0:
            deviceList = ""
            for device in skipDevices:
                deviceList += f"{device}\n"
            CTkLabel(text=f"The following devices are not in Fastboot Mode:\n{deviceList}").place(x=90, y=120)

def erase(device):
    subprocess.call(fastboot_path + f"erase frp -s {device[1]}")
    subprocess.call(fastboot_path + f"-w -s {device[1]}")
    subprocess.call(fastboot_path + f"erase userdata -s {device[1]}")
    subprocess.call(fastboot_path + f"erase cache -s {device[1]}")
    subprocess.call(fastboot_path + f"erase modemst1 -s {device[1]}")
    subprocess.call(fastboot_path + f"erase modemst2 -s {device[1]}")
    subprocess.call(fastboot_path + f"oem fb_mode_clear -s {device[1]}")
    subprocess.call(fastboot_path + f'oem config bootmode "" -s {device[1]}')

#Change Radio
def change_radio(checkedDevices):
    base = CTkToplevel(fg_color="white") 
    base.geometry("300x200") 
    base.title("Set RADIO") 
    base.resizable(False, False) 
    label = CTkLabel (base, text = "Enter new RADIO:", text_color="black").place(x=95, y=3)
    radio = CTkEntry (base, fg_color="white", text_color="black", width=100)
    radio.place(x=100, y=30)
    def click_radio():
        for device in checkedDevices:
            skipDevices = []
            if device[0] == "FAST":
                subprocess.call(fastboot_path + f"erase modemst1 -s {device[1]}")
                subprocess.call(fastboot_path + f"erase modemst2 -s {device[1]}")
                subprocess.call(fastboot_path + f"oem hw radio {radio.get()} -s {device[1]}")
                subprocess.call(fastboot_path + f"reboot bootloader -s {device[1]}")
            elif device[0] == "ADB":
                skipDevices.append(device[1])
        if len(skipDevices) > 0:
            deviceList = ""
            for device in skipDevices:
                deviceList += f"{device}\n"
            CTkLabel(base, text=f"The following devices are not in Fastboot Mode:\n{deviceList}").place(x=90, y=120)
    button = CTkButton(base, text="Set", width=100, command=click_radio).place(x=100, y=60)
    base.after(100, base.lift)
        
#fastboot mode
def fast_mode(checkedDevices):
    for device in checkedDevices:
        skipDevices = []
        if device[0] == "ADB":
            subprocess.call(adb_path + f"-s {device[1]} reboot bootloader")
        elif device[0] == "ADB":
            skipDevices.append(device[1])
    if len(skipDevices) > 0:
            deviceList = ""
            for device in skipDevices:
                deviceList += f"{device}\n"
            CTkLabel(text=f"The following devices are not in Fastboot Mode:\n{deviceList}").place(x=90, y=120)


            





    
