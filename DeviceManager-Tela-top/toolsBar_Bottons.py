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
    ro_carrier = CTkEntry (base, width=100).place(x=100, y=30)
    def click_carrier():
        for device in checkedDevices:
            subprocess.call(fastboot_path + f"oem config fsg-id -s {device}")
            subprocess.call(fastboot_path + f"erase modemst1 -s {device}")
            subprocess.call(fastboot_path + f"erase modemst2 -s {device}")
            subprocess.call(fastboot_path + f"oem config carrier "%{ro_carrier}%" -s {device}")
            subprocess.call(fastboot_path + f"erase modemst1 -s {device}")
            subprocess.call(fastboot_path + f"erase modemst2 -s {device}")
            finished = CTkLabel (base, text = "Finished", text_color="green").place(x=120, y=130)

    button = CTkButton(base, text="Set", width=100, command=click_carrier).place(x=100, y=60)
    base.after(100, base.lift)
    
#Setup Jump
def setup_jump(checkedDevices):
    for device in checkedDevices:
        subprocess.call(adb_path + f"-s {device} shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1")
        subprocess.call(adb_path + f"-s {device} reboot bootloader")

#change SKU
def change_sku(checkedDevices):
    base = CTkToplevel(fg_color="white") 
    base.geometry("300x200") 
    base.title("Set SKU") 
    base.resizable(False, False) 
    label = CTkLabel (base, text = "Enter the SKU:", text_color="black").place(x=95, y=3)
    SKU = CTkEntry (base, fg_color="white", text_color="black", width=100).place(x=100, y=30)
    def click_SKU():
        for device in checkedDevices:
            subprocess.call(fastboot_path + f"oem config sku ""%{SKU}%"" -s {device}")
            subprocess.call(fastboot_path + f"oem config carrier_sku ""%{SKU}%"" -s {device}")
            subprocess.call(fastboot_path + f"reboot bootloader -s {device}")
        
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
    ss = CTkRadioButton (base, text="Single SIM", text_color="black", variable=option, value=1).place(x=95, y=30)
    ds = CTkRadioButton (base, text="Dual SIM", text_color="black", variable=option, value=2).place(x=95, y=80)

    def change():
        for device in checkedDevices:
            if option == 1:
                subprocess.call(fastboot_path + f"oem config sku %{ss}% -s {device}")
                subprocess.call(fastboot_path + f"oem config carrier_sku %{ss}% -s {device}")
                subprocess.call(fastboot_path + f"reboot bootloader -s {device}")
                finished = CTkLabel (base, text = "Finished", text_color="green").place(x=120, y=130)
            elif option == 2:
                subprocess.call(fastboot_path + f"oem config sku %{ds}% -s {device}")
                subprocess.call(fastboot_path + f"oem config carrier_sku %{ds}% -s {device}")
                subprocess.call(fastboot_path + f"reboot bootloader -s {device}")
                finished = CTkLabel (base, text = "Finished", text_color="green").place(x=120, y=130)
    

    button = CTkButton(base, text="Set", width=100, command=change).place(x=95, y=110)
    base.after(100, base.lift)

#E/P-SIM
def sim_type2(checkedDevices):
    base = CTkToplevel(fg_color="white") 
    base.geometry("300x200")  
    base.title("Set SKU")
    base.resizable(False, False) 
    option = IntVar(value=0)
    ss = CTkRadioButton (base, text="p-SIM", text_color="black", variable=option, value=1).place(x=95, y=30)
    ds = CTkRadioButton (base, text="e-SIM", text_color="black", variable=option, value=2).place(x=95, y=80)

    def change():
        for device in checkedDevices:
            if option == 1:
                subprocess.call(fastboot_path + f"oem hw esim false -s {device}")
                subprocess.call(fastboot_path + f"-w -s {device}")
                subprocess.call(fastboot_path + f"erase userdata -s {device}")
                subprocess.call(fastboot_path + f"erase cache -s {device}")
                subprocess.call(fastboot_path + f"erase modemst1 -s {device}")
                subprocess.call(fastboot_path + f"erase modemst2 -s {device}")
                subprocess.call(fastboot_path + f"oem fb_mode_clear -s {device}")
                subprocess.call(fastboot_path + f"oem config bootmode "" -s {device}")
                finished = CTkLabel (base, text = "Finished", text_color="green").place(x=120, y=130)
            elif option == 2:
                subprocess.call(fastboot_path + f"fastboot oem hw esim true -s {device}")
                subprocess.call(fastboot_path + f"-w -s {device}")
                subprocess.call(fastboot_path + f"erase userdata -s {device}")
                subprocess.call(fastboot_path + f"erase cache -s {device}")
                subprocess.call(fastboot_path + f"erase modemst1 -s {device}")
                subprocess.call(fastboot_path + f"erase modemst2 -s {device}")
                subprocess.call(fastboot_path + f"oem fb_mode_clear -s {device}")
                subprocess.call(fastboot_path + f"oem config bootmode "" -s {device}")
                finished = CTkLabel (base, text = "Finished", text_color="green").place(x=120, y=130)
    

    button = CTkButton(base, text="Set", width=100, command=change).place(x=95, y=110)
    base.after(100, base.lift)

    
