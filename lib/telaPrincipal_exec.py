from customtkinter import * 
from tkinter import *
from telaPrincipal import*
sys.path.append('lib\\models')
from user_model import User
from CTkMenuBar import *

base = CTk() 
base.geometry("1000x600") 
base._set_appearance_mode("dark")
base.title("Motorola Device Manager") 
base.resizable(False, False)

rootPath = f"{os.path.normpath(os.path.dirname(__file__))}"
buildFolder = ""
if os.path.exists (f"{rootPath}\\utilities\\default_build_folder.txt"):
    with open(f"{rootPath}\\utilities\\default_build_folder.txt", "r") as file:
        content = file.readline()
        if content != "":
            buildFolder = content
        else:
            if not os.path.exists(f"{os.environ['USERPROFILE']}\\Documents\\Builds"):
                os.mkdir(f"{os.environ['USERPROFILE']}\\Documents\\Builds")
            buildFolder = f"{os.environ['USERPROFILE']}\\Documents\\Builds"
else: 
    if not os.path.exists(f"{os.environ['USERPROFILE']}\\Documents\\Builds"):
        os.mkdir(f"{os.environ['USERPROFILE']}\\Documents\\Builds")
    buildFolder = f"{os.environ['USERPROFILE']}\\Documents\\Builds"

currentUser = User.getUser()

multF_tela = MultF_Tela(base, currentUser, buildFolder) 
scripts_tela = Scripts_Tela(base, currentUser.username, currentUser.password) 


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


flash = CTkImage(Image.open("assets/flash.png"), size=(90, 90))
tools = CTkImage(Image.open("assets/Tools_2.png"), size=(85, 85))
eng_set = CTkImage(Image.open("assets/engine.png"), size=(15, 15))
#Frames Principais
menuLateral = CTkFrame(base, width=150, height=620, fg_color="#6495ED", bg_color="#6495ED").place(x=0) 
multflash = CTkButton(menuLateral, text=None, image=flash, width=150, height=80, fg_color="#6495ED", bg_color="#6495ED", hover=None, command=show_multF).place(x=0, y=0) 
Scripts = CTkButton(menuLateral, text=None, image=tools, width=150, height=80, fg_color="#6495ED", bg_color="#6495ED", hover=None,command=show_scripts).place(x=0, y=80) 
multF_tela.place(x=150) 

menuBar = CTkTitleMenu(base, x_offset=280, y_offset=10)


settings = menuBar.add_cascade(text="", image=eng_set, fg_color= "transparent", hover_color="black", corner_radius=0)
dropSettings = CustomDropdownMenu(settings, fg_color="transparent", width=100)
def setBuildFolder():
    dirname = ""
    dirname = filedialog.askdirectory()
    if dirname != "":
        with open(f"{rootPath}\\utilities\\default_build_folder.txt", "w") as file:
            file.write(dirname)
dropSettings.add_option("Set Build folder", command=setBuildFolder)



base.mainloop()