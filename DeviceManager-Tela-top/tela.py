import re
import subprocess
import requests

from tkinter import *

def verbose_call(func):
    def print_func(*func_args, **func_kwargs):
        if get_args().verbose:
            print(f'Calling <{func.__name__}>')
        return func(*func_args, **func_kwargs)
    return print_func
 

def call_command(command, suppress_error_msg=False):
    def print_error_msg(e):
        if not suppress_error_msg:
            print(f"\n\t{e.__class__.__name__} running command <" + str(command) + '>:')
            print(f'\t{e}\n')

    def sanitize_output(output_):
        head, _, _ = output_.partition('Finished')
        return head.replace("\\r\\n", "\n").replace("\\n", "\n").strip("b'\n")

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
    except (FileNotFoundError, OSError, subprocess.CalledProcessError) as e:
        print_error_msg(e)
        output = R.string.build_error_msg(str(e))
    except Exception as e:
        print(f'-- Generic Exception<{e.__class__.__name__}>, should be explicitly added to known possible errors')
        print_error_msg(e)
        output = R.string.build_error_msg(str(e))

    return sanitize_output(str(output))


def input_tail(input, sep=': '):
    _, _, tail = input.partition(sep)
    return tail


def is_secure(input):
    return "Secure" if input_tail(input) == "yes" else "Non secure"


def get_build(i):
    input = i.replace('(bootloader) ro.build.fingerprint',"")
    head = input.splitlines()[0][5:]   
    tail = input.splitlines()[1][5:]    
    result = head+tail
    return result.split('/')[3]

    
def get_fastboot_info():
    barcode = input_tail(call_command("fastboot getvar serialno"))
    hw_type = is_secure(call_command("fastboot getvar secure"))
    sku = input_tail(call_command("fastboot getvar sku"))
    hw_rev = input_tail(call_command("fastboot getvar hwrev"))
    version = get_build(call_command("fastboot getvar ro.build.fingerprint"))
    cid = input_tail(call_command("fastboot getvar cid"))
    channelid = input_tail(call_command("fastboot getvar channelid"))
    radio = input_tail(call_command("fastboot getvar radio"))
    carrier = input_tail(call_command("fastboot getvar ro.carrier"))

    texto = f'''
    DEVICE INFORMATIONS:
    Barcode: {barcode}
    HW Type: {hw_type}
    SKU: {sku}
    HW Rev: {hw_rev}
    Version: {version}
    CID: {cid}
    Channel ID: {channelid}
    Radio: {radio}
    Carrier: {carrier}'''
    
    texto_resultado["text"] = texto

def fastboot_erases():
    call_command("fastboot erase frp")
    call_command("fastboot -w")
    call_command("fastboot erase userdata")
    call_command("fastboot erase cache")
    call_command("fastboot erase modemst1")
    call_command("fastboot erase modemst2")
    call_command("fastboot oem fb_mode_clear")
    call_command("fastboot oem config bootmode """)

    texto2 = f'''
    Erase Completed'''

    texto_resultado["text"] = texto2

def fastboot_mode():
    call_command("adb reboot bootloader")


def setup_jump():
    call_command("adb shell content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1")
    call_command("adb reboot-bootloader")

def set_carrier():
    #janela2 = Tk()
    janela2 = Toplevel()
    janela2.title ("Comando")
    janela2.geometry('270x250')
    label = Label (janela2, text = "Enter the value")
    label.grid (column = 0, row = 0, padx=15, pady=15)
    entrada = Entry(janela2,width=10)
    entrada.grid(column=1, row=0, padx=5, pady=15)
    resultado = entrada.get()
    #label.configure(text= resultado)
    saida = f'''
    call_command("fastboot oem config fsg-id """)
    call_command("fastboot erase modemst1")
    call_command("fastboot erase modemst2")
    call_command("fastboot oem config carrier " + resultado)
    call_command("fastboot erase modemst1")
    call_command("fastboot erase modemst2")'''
    botao = Button(janela2, text="OK",command = saida)
    botao.grid(column=1, row=1, padx=5, pady=15)
    botaoX = Button(janela2, text="Fechar",command = janela2.destroy)
    botaoX.grid(column=2, row=1, padx=5, pady=15)


#########################################################################################################################################################################################

root = Tk()  # create root window
root.title("Device Manager")
root.iconbitmap("icon.ico")
root.config(bg="skyblue")

# Create Frame widget
left_frame = Frame(root, width=200, height=400, bg="green")
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root, width=650, height=400, bg='green')
right_frame.grid(row=0, column=1, padx=10, pady=5)

image = PhotoImage(file="cell.png")
original_image = image.subsample(3,3)  # resize image using subsample
Label(left_frame, image=original_image).grid(row=0, column=0, padx=5, pady=5)

# Create tool bar frame
tool_bar = Frame(left_frame, width=180, height=185, bg='green')
tool_bar.grid(row=4, column=0, padx=5, pady=5)

botaoInfo = Button(left_frame, text="Exibir informações dos devices", command=get_fastboot_info)
botaoInfo.grid(row=3, column=0, padx=5, pady=5)

botaoErase = Button(tool_bar, text="Erases", command=fastboot_erases)
botaoErase.grid(row=0, column=0, padx=5, pady=3, ipadx=10)


botaoADB = Button(tool_bar, text="Fastboot", command=fastboot_mode)
botaoADB.grid(row=0, column=1, padx=5, pady=3, ipadx=10)

botaoJump = Button(tool_bar, text="Setup Jump", command=setup_jump)
botaoJump.grid(row=5, column=0, padx=5, pady=5)

botaoFlash = Button(tool_bar, text="Flash")
botaoFlash.grid(row=5, column=1, padx=5, pady=5)

botaoRADIO = Button(tool_bar, text="Change RADIO")
botaoRADIO.grid(row=6, column=0, padx=5, pady=5)

botaoSKU = Button(tool_bar, text="Change SKU")
botaoSKU.grid(row=6, column=1, padx=5, pady=5)

botaoCarrier = Button(tool_bar, text="Carrier", command=set_carrier)
botaoCarrier.grid(row=7, column=0, padx=5, pady=5)

botaoRB = Button(tool_bar, text="Reboot")
botaoRB.grid(row=7, column=1, padx=5, pady=5)

botaoSIM = Button(tool_bar, text="Dual/Single")
botaoSIM.grid(row=8, column=0, padx=5, pady=5)

botaoESIM = Button(tool_bar, text="Esim/Psim")
botaoESIM.grid(row=8, column=1, padx=5, pady=5)

texto_resultado = Label(right_frame, text="", width=100, height=30, bg='green', fg="white")
texto_resultado.grid(row=2, column=0, padx=5, pady=5)

root.mainloop()