import tkinter as tk
from tkinter import ttk
import threading
import time
import subprocess
import teste4
from getpass import getpass

 
user= sys.argv[1]
password= sys.argv[2]

def call_command(command, suppress_error_msg=False):
    def print_error_msg(e):
        if not suppress_error_msg:
            print(f"\n\t{e.__class__.__name__} running command <" + str(command) + '>:')
            # print(f'\t{e}\n')

    def sanitize_output(output_):
        head, _, _ = output_.partition('Finished')
        return head.replace("\\r\\n", "\n").replace("\\n", "\n").strip("b'\n")

    try:
        output = subprocess.check_output(command)
    except (FileNotFoundError, OSError, subprocess.CalledProcessError) as e:
        print_error_msg(e)
        # output = R.string.build_error_msg(str(e))
    # except Exception as e:
    #     print(f'-- Generic Exception<{e.__class__.__name__}>, should be explicitly added to known possible errors')
    #     print_error_msg(e)
        # output = R.string.build_error_msg(str(e))

    return sanitize_output(str(output))

class Celular:

    def __init__(self, barcode):
        self.barcode = barcode
 
def listar_celulares():
    # Listar celulares que estão conectados em fastboot
    barcode = call_command("fastboot devices")
    aux = barcode.replace("\\tfastboot", "").split("\n")
    lista_devices = []
    for device in aux:
        lista_devices.insert(0,Celular(device))
    return lista_devices
 
def transferir_arquivos(barcode):
    # Simula a transferência de arquivos
    cont = 1
    while True:
        if cont == 1:
            carrier = input("Insert ro.carrier: ")
            teste4.main(user_=user, password_=password, carrier_= carrier, barcode_= barcode)
            cont = cont + 1
        # product = call_command(f"fastboot -s {barcode} getvar product")
        print(f"BAIXANDO BUILD DO {barcode}")
        time.sleep(5)
 
def selecionar_celular():
    selected_barcode = combo_celulares.get()
    return selected_barcode
 
def transferir_arquivos_thread():
    barcode = selecionar_celular() 
    # Cria uma thread para a transferência de arquivos
    thread = threading.Thread(target=transferir_arquivos, args=({barcode}))
    thread.start()

 
# Interface gráfica usando Tkinter
app = tk.Tk()
app.title("Transferência de Arquivos")

# Lista inicial de celulares
celulares = listar_celulares()

# Combobox para selecionar celulares
combo_celulares = ttk.Combobox(app, values=[celular.barcode for celular in celulares])
combo_celulares.grid(row=0, column=0, padx=10, pady=10)

# Botão para iniciar a transferência de arquivos
btn_transferir = tk.Button(app, text="Transferir Arquivos", command=transferir_arquivos_thread)
btn_transferir.grid(row=1, column=0, padx=10, pady=10)

app.mainloop()