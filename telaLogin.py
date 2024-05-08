from customtkinter import *
import os
import requests
import base64
from tkinter import *
from PIL import Image
from lib.models.user_model import *
import sys

root_path = f"{os.path.normpath(os.path.dirname(__file__))}"
exec_path = sys.argv[0].replace('\\MDM.exe', '')

def checkLogin(user: User.UserModel) :
        url = ("https://artifacts.mot.com/artifactory/genevn")
        headers = {
        'Authorization': f'Basic {user.token}'
        }
        req = requests.get(url, headers=headers)
        print(f'{req.status_code}')
        if(req.status_code == 200) :
                return True
        else :
                return False

if exec_path.find('telaLogin.py') == -1:
        userSaved = User.getUser(f'{exec_path}\\docs')
else:        
        userSaved = User.getUser(f'{root_path}\\docs')
if checkLogin(userSaved) :
        print("usuário já está logado")
        # os.system(f'start \"DM\" cmd /c pyw {os.path.dirname(__file__)}\\telaPrincipal_exec.py {userSaved.username} {userSaved.password}')        
        if exec_path.find('telaLogin.py') == -1:
                os.system(f'start "DM" cmd /c start {exec_path}\\tools\\functions.exe {userSaved.username} {userSaved.password}')
        else:
                os.system(f'start "DM" cmd /c start python3 {root_path}\\telaPrincipal_exec.py {userSaved.username} {userSaved.password}')
        sys.exit()

winLog = CTk(fg_color="gray")
winLog.geometry("1000x600")
winLog.title("MDM - Login")
winLog.resizable(False, False)

img_log = CTkImage(Image.open(f"{root_path}\\assets\\login.png"), size=(500, 600))
img_Label = CTkLabel(winLog, image = img_log, text=None)
img_Label.place(x = 0, y = 0)

frameLog = CTkFrame(winLog, width=500, height=600, fg_color="black")
frameWel = CTkFrame(frameLog, width=290, height=300, fg_color="black")

wc = CTkLabel(frameWel, text="Welcome", text_color="white", font=("Roboto", 25))
wc.place(x=95, y=50)

labelLogin = CTkLabel(frameWel, text="", text_color="white", font=("Roboto", 12))
labelLogin.place(x=105, y=250)

def click():
        user = User.UserModel(user_.get(), password_.get())
        loginValidate = checkLogin(user)
        if(loginValidate) :
                # os.system(f'start \"DM\" cmd /c py {os.path.dirname(__file__)}\\telaPrincipal_exec.py {user_.get()} {password_.get()}')
                if exec_path.find('telaLogin.py') == -1:
                        os.system(f'start "DM" cmd /c start {exec_path}\\tools\\functions.exe {user.username} {user.password}')                        
                        User.storeUser(user, f'{exec_path}\\docs')
                        print(f'{exec_path}\\docs')
                else:
                        os.system(f'start "DM" cmd /c start python3 {root_path}\\telaPrincipal_exec.py {user.username} {user.password}')
                        User.storeUser(user, f'{root_path}\\docs')
                sys.exit()
                
        else : 
                labelLogin.configure(text="Login inválido")

user_ = CTkEntry(frameWel, placeholder_text="CoreID", width=250)
user_.place(x=20, y=100)

password_ = CTkEntry(frameWel, placeholder_text="Password", show="*", width=250)
password_.place(x=20, y=150)

button = CTkButton(frameWel, text="Login", command=click)
button.place(x=75, y=220)

frameLog.pack(side=RIGHT)
frameWel.place(x=100, y=130)
frameLog.pack_propagate(False)
frameWel.pack_propagate(False)
winLog.mainloop()