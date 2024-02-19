from customtkinter import * 
from telaPrincipal import*
sys.path.append('lib\\models')
from user_model import User

base = CTk() 
base.geometry("1000x600") 
base._set_appearance_mode("dark") 
base.title("Motorola Device Manager") 
base.resizable(False, False)

currentUser = User.getUser()

multF_tela = MultF_Tela(base, currentUser) 
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
#Frames Principais
menuLateral = CTkFrame(base, width=150, height=600, fg_color="#3CB371", bg_color="#3CB371").place(x=0) 
multflash = CTkButton(menuLateral, text=None, image=flash, width=150, height=80, fg_color="#3CB371", bg_color="#3CB371", hover=None, command=show_multF).place(x=0) 
Scripts = CTkButton(menuLateral, text=None, image=tools, width=150, height=80, fg_color="#3CB371", bg_color="#3CB371", hover=None,command=show_scripts).place(x=0, y=80) 
multF_tela.place(x=150) 


base.mainloop()