from customtkinter import * 
from telaPrincipal import*
#user = sys.argv[1]
#password = sys.argv[2]
user = ("nmoraes")
password = ("Punick@2024")


base = CTk() 
base.geometry("1000x600") 
base._set_appearance_mode("dark") 
base.title("Motorola Device Manager") 
base.resizable(False, False) 
        
multF_tela = MultF_Tela(base, user, password) 
scripts_tela = Scripts_Tela(base, user, password) 

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

#Frames Principais
menuLateral = CTkFrame(base, width=150, height=600, fg_color="#191970", bg_color="#191970").place(x=0) 
multflash = CTkButton(menuLateral, text="MultiFlash", width=150, height=80, fg_color="#191970", bg_color="#191970", command=show_multF).place(x=0) 
Scripts = CTkButton(menuLateral, text="Tools", width=150, height=80, fg_color="#191970", bg_color="#191970", command=show_scripts).place(x=0, y=80) 
multF_tela.place(x=150) 


base.mainloop()