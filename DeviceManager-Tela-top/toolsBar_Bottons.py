from customtkinter import *
from tkinter import *
import os
import subprocess
fastboot_path = f'"{os.path.dirname(__file__)}\\platform-tools\\fastboot.exe" '

#SetCarrier
def set_carrier():
    base = CTk(fg_color="white") 
    base.geometry("300x200") 
    base._set_appearance_mode("dark") 
    base.title("Set Carrier") 
    base.resizable(False, False) 
    label = CTkLabel (base, text = "Enter the ro.carrier:").place(x=95, y=3)
    ro_carrier = CTkEntry (base, width=100).place(x=100, y=30)
    def click_carrier():
        subprocess.call(fastboot_path + f"oem config fsg-id")
        subprocess.call(fastboot_path + f"erase modemst1")
        subprocess.call(fastboot_path + f"erase modemst2")
        subprocess.call(fastboot_path + f"oem config carrier ""%{ro_carrier}%""")
        subprocess.call(fastboot_path + f"erase modemst1")
        subprocess.call(fastboot_path + f"erase modemst2")
        finished = CTkLabel (base, text = "Finished", text_color="green").place(x=120, y=130)

    button = CTkButton(base, text="Set", width=100, command=click_carrier).place(x=100, y=60)
    base.mainloop()