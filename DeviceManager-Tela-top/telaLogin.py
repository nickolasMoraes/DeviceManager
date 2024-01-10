from customtkinter import *
import os
import requests
import base64
from tkinter import *
from PIL import Image
telaPrincipal = f'"{os.path.dirname(__file__)}\\DeviceManager-Tela-top\\telaPrincipal.py"'

Imagens = os.path.dirname(os.path.realpath(__file__))
img_log = CTkImage(Image.open(Imagens + "/login.png"), size=(500, 600))

winLog = CTk(fg_color="gray")
winLog.geometry("1000x600")
winLog.title("MDM - Login")
winLog.resizable(False, False)


img_Label = CTkLabel(winLog, image = img_log, text=None)
img_Label.place(x = 0, y = 0)

frameLog = CTkFrame(winLog, width=500, height=600, fg_color="black")
frameWel = CTkFrame(frameLog, width=290, height=300, fg_color="black")

wc = CTkLabel(frameWel, text="Welcome", text_color="white", font=("Roboto", 25))
wc.place(x=95, y=50)

user_ = CTkEntry(frameWel, placeholder_text="CoreID", width=250)
user_.place(x=20, y=100)

password_ = CTkEntry(frameWel, placeholder_text="Password", show="*", width=250)
password_.place(x=20, y=150)

def click():
        os.system(f'start \"DM\" cmd /c py "{os.path.dirname(__file__)}\\telaPrincipal.py"')
        quit()

button = CTkButton(frameWel, text="Login", command=click)
button.place(x=75, y=220)


frameLog.pack(side=RIGHT)
frameWel.place(x=100, y=130)
frameLog.pack_propagate(False)
frameWel.pack_propagate(False)
winLog.mainloop()