from customtkinter import * 
from tkinter import *
from lib.telaPrincipal import*
from CTkMenuBar import *
from lib.models.user_model import *

base = CTk() 
base.geometry("1000x600") 
base._set_appearance_mode("dark")
base.title("Motorola Device Manager") 
base.resizable(False, False)

root_path = f"{os.path.normpath(os.path.dirname(__file__))}"
assetsFolder = f'{root_path}\\assets'
buildFolder = ""
if os.path.exists (f"{root_path}\\docs\\default_build_folder.txt"):
    with open(f"{root_path}\\docs\\default_build_folder.txt", "r") as file:
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

currentUser = User.getUser(f'{root_path}\\docs')

multF_tela = MultF_Tela(base, currentUser, buildFolder, assetsFolder) 
scripts_tela = Scripts_Tela(base, currentUser.username, currentUser.password, assetsFolder) 


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


flash = CTkImage(Image.open(f"{assetsFolder}\\flash.png"), size=(90, 90))
tools = CTkImage(Image.open(f"{assetsFolder}\\Tools_2.png"), size=(85, 85))
eng_set = CTkImage(Image.open(f"{assetsFolder}\\engine.png"), size=(15, 15))
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
        with open(f"{root_path}\\docs\\default_build_folder.txt", "w") as file:
            file.write(dirname)
dropSettings.add_option("Set Build folder", command=setBuildFolder)



base.mainloop()