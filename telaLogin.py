from customtkinter import *
import os

winLog = CTk()
winLog.geometry("1000x600")
winLog.title("MDM - Login")
winLog.resizable(False, False)

frameLog = CTkFrame(winLog, width=500, height=600, fg_color="black")
frameWel = CTkFrame(frameLog, width=290, height=300, fg_color="black")

wc = CTkLabel(frameWel, text="Welcome", font=("Roboto", 25))
wc.place(x=95, y=50)

user_ = CTkEntry(frameWel, placeholder_text="CoreID", width=250)
user_.place(x=20, y=100)

password_ = CTkEntry(frameWel, placeholder_text="Password", show="*", width=250)
password_.place(x=20, y=150)

def click():
    os.system(f'start \"DM\" cmd /c py teste2.py {user_.get()} {password_.get()}')
    quit()

button = CTkButton(frameWel, text="Login", command=click)
button.place(x=75, y=220)


frameLog.pack(side=RIGHT)
frameWel.place(x=100, y=130)
frameLog.pack_propagate(False)
frameWel.pack_propagate(False)
winLog.mainloop()