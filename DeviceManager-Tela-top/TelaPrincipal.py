from customtkinter import *

class Scripts_Tela(CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=850, height=600, fg_color="pink", bg_color="pink")
        #widgets
        self.tools_bar = CTkFrame(self, width=850, height=100, fg_color="purple", bg_color="gray")
        self.setCarrier = CTkButton(self.tools_bar)

    def place(self, **kwargs):
        self.tools_bar.place(y=0)
        self.setCarrier.place(y=1)
        return super().place(**kwargs)
    
    def place_forget(self):
        for widget in self.place_slaves():
            widget.place_forget()
        return super().place_forget()
    
class MultF_Tela(CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=850, height=600, fg_color="gray", bg_color="gray")
        #widgets
        

    def place(self, **kwargs):
        
        return super().place(**kwargs)
    
    def place_forget(self):
        for widget in self.place_slaves():
            widget.place_forget()
        return super().place_forget()
    


base = CTk()
base.geometry("1000x600")
base._set_appearance_mode("dark")
base.title("Motorola Device Manager")
base.resizable(False, False)

multF_tela = MultF_Tela(base)
scripts_tela = Scripts_Tela(base)

def hide_tabs():
    for widget in multF_tela.place_slaves():
        widget.place_forget()
    multF_tela.place_forget()

    for widget in scripts_tela.place_slaves():
        widget.place_forget()
    scripts_tela.place_forget()

def show_multF():
    hide_tabs()
    multF_tela.place(x=150)

def show_scripts():
    hide_tabs()
    
    scripts_tela.place(x=150)

menuLateral = CTkFrame(base, width=150, height=600, fg_color="#1D5DEC", bg_color="#1D5DEC").place(x=0)

multflash = CTkButton(menuLateral, text="MultiFlash", width=150, height=80, fg_color="#1D5DEC", bg_color="#1D5DEC", command=show_multF).place(x=0)
Scripts = CTkButton(menuLateral, text="Tools", width=150, height=80, fg_color="#1D5DEC", bg_color="#1D5DEC", command=show_scripts).place(x=0, y=80)

multF_tela.place(x=150)



base.mainloop()