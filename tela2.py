from tkinter import*

#Construção da janela------------
janela = Tk()
janela.title("Device Manager")
janela.geometry('1200x700')

#Caixa de texto-----------------

email_label = Label(janela, text="Email Address:")
email_label.pack()

email_entry = Entry(janela)
email_entry.pack()
email_entry.focus()

#Caixa de saída-----------------


botao = Button(janela, text="Clica aqui")
botao.pack()

janela.mainloop()