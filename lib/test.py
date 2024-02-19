from CTkScrollableDropdown import *
import customtkinter

root = customtkinter.CTk()

customtkinter.CTkLabel(root, text="Different Dropdown Styles").pack(pady=5)

# Some option list
values = ['../', 'msi_only/', 'T1TGN33.1/', 'T1TGN33.10/', 'T1TGN33.11/', 'T1TGN33.12/', 'T1TGN33.13/', 'T1TGN33.14/', 'T1TGN33.15/', 'T1TGN33.16/', 'T1TGN33.17/', 'T1TGN33.18/', 'T1TGN33.19/', 'T1TGN33.2/', 'T1TGN33.20/', 'T1TGN33.21/', 'T1TGN33.22/', 'T1TGN33.23/', 'T1TGN33.24/', 'T1TGN33.25/', 'T1TGN33.26/', 'T1TGN33.29/', 'T1TGN33.29-1/', 'T1TGN33.29-2/', 'T1TGN33.29-3/', 'T1TGN33.3/', 'T1TGN33.30/', 'T1TGN33.31/', 'T1TGN33.31-F.1/', 'T1TGN33.31-F.2/', 'T1TGN33.32/', 'T1TGN33.33/', 'T1TGN33.34/', 'T1TGN33.35/', 'T1TGN33.36/', 'T1TGN33.37/', 'T1TGN33.37-1/', 'T1TGN33.37-2/', 'T1TGN33.38/', 'T1TGN33.39/', 'T1TGN33.4/', 'T1TGN33.40/', 'T1TGN33.41/', 'T1TGN33.42/', 'T1TGN33.43/', 'T1TGN33.44/', 'T1TGN33.45/', 'T1TGN33.46/', 'T1TGN33.47/', 'T1TGN33.48/', 'T1TGN33.49/', 'T1TGN33.5/', 'T1TGN33.50/', 'T1TGN33.51/', 'T1TGN33.52/', 'T1TGN33.53/', 'T1TGN33.54/', 'T1TGN33.55/', 'T1TGN33.56/', 'T1TGN33.57/', 'T1TGN33.58/', 'T1TGN33.59/', 'T1TGN33.6/', 'T1TGN33.60/', 'T1TGN33.60-1/', 'T1TGN33.60-10/', 'T1TGN33.60-100/', 'T1TGN33.60-101/', 'T1TGN33.60-102/', 'T1TGN33.60-103/', 'T1TGN33.60-104/', 'T1TGN33.60-105/', 'T1TGN33.60-106/', 'T1TGN33.60-107/', 'T1TGN33.60-108/', 'T1TGN33.60-109/', 'T1TGN33.60-11/', 'T1TGN33.60-110/', 'T1TGN33.60-111/', 'T1TGN33.60-112/', 'T1TGN33.60-113/', 'T1TGN33.60-114/', 'T1TGN33.60-114R1/', 'T1TGN33.60-114R2/', 'T1TGN33.60-114R3/', 'T1TGN33.60-115/', 'T1TGN33.60-116/', 'T1TGN33.60-12/', 'T1TGN33.60-13/', 'T1TGN33.60-14/', 'T1TGN33.60-15/', 'T1TGN33.60-16/', 'T1TGN33.60-17/', 'T1TGN33.60-18/', 'T1TGN33.60-19/', 'T1TGN33.60-2/', 'T1TGN33.60-20/', 'T1TGN33.60-22/', 'T1TGN33.60-23/', 'T1TGN33.60-23R1/', 'T1TGN33.60-23R2/', 'T1TGN33.60-23R3/', 'T1TGN33.60-24/', 'T1TGN33.60-25/', 'T1TGN33.60-26/', 'T1TGN33.60-27/', 'T1TGN33.60-28/', 'T1TGN33.60-29/', 'T1TGN33.60-3/', 'T1TGN33.60-3-F.1/', 'T1TGN33.60-3-F.2/', 'T1TGN33.60-3-F.3/', 'T1TGN33.60-3-F.4/', 'T1TGN33.60-3-F.5/', 'T1TGN33.60-3-F.6/', 'T1TGN33.60-30/', 'T1TGN33.60-31/', 'T1TGN33.60-32/', 'T1TGN33.60-33/', 'T1TGN33.60-34/', 'T1TGN33.60-35/', 'T1TGN33.60-36/', 'T1TGN33.60-37/', 'T1TGN33.60-37R1/', 'T1TGN33.60-38/', 'T1TGN33.60-39/', 'T1TGN33.60-4/', 'T1TGN33.60-40/', 'T1TGN33.60-41/', 'T1TGN33.60-41-1/', 'T1TGN33.60-41-2/', 'T1TGN33.60-41-2R1/', 'T1TGN33.60-41-2R2/', 'T1TGN33.60-41R1/', 'T1TGN33.60-41R2/', 'T1TGN33.60-41R3/', 'T1TGN33.60-41R4/', 'T1TGN33.60-42/', 'T1TGN33.60-43/', 'T1TGN33.60-44/', 'T1TGN33.60-45/', 'T1TGN33.60-46/', 'T1TGN33.60-47/', 'T1TGN33.60-48/', 'T1TGN33.60-49/', 'T1TGN33.60-5/', 'T1TGN33.60-50/', 'T1TGN33.60-51/', 'T1TGN33.60-52/', 'T1TGN33.60-53/', 'T1TGN33.60-54/', 'T1TGN33.60-55/', 'T1TGN33.60-55R1/', 'T1TGN33.60-55R2/', 'T1TGN33.60-55R3/', 'T1TGN33.60-56/', 'T1TGN33.60-57/', 'T1TGN33.60-58/', 'T1TGN33.60-59/', 'T1TGN33.60-5R1/', 'T1TGN33.60-6/', 'T1TGN33.60-60/', 'T1TGN33.60-61/', 'T1TGN33.60-62/', 'T1TGN33.60-63/', 'T1TGN33.60-64/', 'T1TGN33.60-65/', 'T1TGN33.60-66/', 'T1TGN33.60-67/', 'T1TGN33.60-67-1/', 'T1TGN33.60-67-1-1/', 'T1TGN33.60-67-1-1R1/', 'T1TGN33.60-67-1-1R2/', 'T1TGN33.60-67-1-1R3/', 'T1TGN33.60-67-1-2/', 'T1TGN33.60-67-2/', 'T1TGN33.60-67-3/', 'T1TGN33.60-67-3R1/', 'T1TGN33.60-67-3R2/', 'T1TGN33.60-67-4/', 'T1TGN33.60-67-5/', 'T1TGN33.60-67-6/', 'T1TGN33.60-67-6-1-1/', 'T1TGN33.60-67-7/', 'T1TGN33.60-67R1/', 'T1TGN33.60-68/', 'T1TGN33.60-69/', 'T1TGN33.60-7/', 'T1TGN33.60-70/', 'T1TGN33.60-71/', 'T1TGN33.60-72/', 'T1TGN33.60-73/', 'T1TGN33.60-74/', 'T1TGN33.60-75/', 'T1TGN33.60-76/', 'T1TGN33.60-77/', 'T1TGN33.60-78/', 'T1TGN33.60-79/', 'T1TGN33.60-8/', 'T1TGN33.60-80/', 'T1TGN33.60-81/', 'T1TGN33.60-82/', 'T1TGN33.60-83/', 'T1TGN33.60-84/', 'T1TGN33.60-85/', 'T1TGN33.60-86/', 'T1TGN33.60-87/', 'T1TGN33.60-88/', 'T1TGN33.60-89/', 'T1TGN33.60-9/', 'T1TGN33.60-90/', 'T1TGN33.60-91/', 'T1TGN33.60-92/', 'T1TGN33.60-93/', 'T1TGN33.60-94/', 'T1TGN33.60-95/', 'T1TGN33.60-96/', 'T1TGN33.60-97/', 'T1TGN33.60-98/', 'T1TGN33.60-99/', 'T1TGN33.60-99-1/', 'T1TGN33.60-99-2/', 'T1TGN33.60-99-3/', 'T1TGN33.60-9R1/', 'T1TGN33.60-9R2/', 'T1TGN33.60-9R3/', 'T1TGN33.7/', 'T1TGN33.8/', 'T1TGN33.9/', 'T1TGNS33.60-114-1/', 'T1TGNS33.60-114-2/', 'T1TGNS33.60-114-3/', 'T1TGNS33.60-114-4/', 'T1TGNS33.60-41-1/', 'T1TGNS33.60-41-2/', 'T1TGNS33.60-41-2-1/', 'T1TGNS33.60-41-2-10/', 'T1TGNS33.60-41-2-11/', 'T1TGNS33.60-41-2-12/', 'T1TGNS33.60-41-2-13/', 'T1TGNS33.60-41-2-14/', 
'T1TGNS33.60-41-2-2/', 'T1TGNS33.60-41-2-3/', 'T1TGNS33.60-41-2-4/', 'T1TGNS33.60-41-2-5/', 'T1TGNS33.60-41-2-6/', 'T1TGNS33.60-41-2-7/', 'T1TGNS33.60-41-2-8/', 'T1TGNS33.60-41-2-9/', 'T1TGNS33.60-55-1/', 'T1TGNS33.60-55-2/', 'T1TGNS33.60-55-3-1/', 'T1TGNS33.60-55-3-10/', 'T1TGNS33.60-55-3-11/', 'T1TGNS33.60-55-3-12/', 'T1TGNS33.60-55-3-2/', 'T1TGNS33.60-55-3-3/', 'T1TGNS33.60-55-3-4/', 'T1TGNS33.60-55-3-5/', 'T1TGNS33.60-55-3-6/', 'T1TGNS33.60-55-3-7/', 'T1TGNS33.60-55-3-8/', 'T1TGNS33.60-55-3-9/', 'T1TGNS33.60-67-1/', 'T1TGNS33.60-67-1-2-1/', 'T1TGNS33.60-67-1-2-2/', 'T1TGNS33.60-67-1-2-3/', 'T1TGNS33.60-67-1-2-4/', 'T1TGNS33.60-67-1-2-5/', 'T1TGNS33.60-67-2/', 'T1TGNS33.60-67-3/', 'T1TGNS33.60-67-4/', 'T1TGNS33.60-67-5/', 'T1TGNS33.60-67-6-1/', 'T1TGNS33.60-67-6-1-1-1/', 'T1TGNS33.60-67-6-1-1-2/', 'T1TGNS33.60-67-6-1-1-3/', 'TTGN33.10/', 'TTGN33.11/', 'TTGN33.12/', 'TTGN33.13/', 'TTGN33.14/', 'TTGN33.15/', 'TTGN33.16/', 'TTGN33.17/', 'TTGN33.18/', 'TTGN33.19/', 'TTGN33.2/', 'TTGN33.20/', 'TTGN33.21/', 'TTGN33.22/', 'TTGN33.23/', 'TTGN33.24/', 'TTGN33.25/', 'TTGN33.26/', 'TTGN33.27/', 'TTGN33.28/', 'TTGN33.29/', 'TTGN33.3/', 'TTGN33.30/', 'TTGN33.31/', 'TTGN33.32/', 'TTGN33.33/', 'TTGN33.34/', 'TTGN33.35/', 'TTGN33.36/', 'TTGN33.37/', 'TTGN33.38/', 'TTGN33.39/', 'TTGN33.4/', 'TTGN33.40/', 'TTGN33.41/', 'TTGN33.42/', 'TTGN33.43/', 'TTGN33.44/', 'TTGN33.45/', 'TTGN33.46/', 'TTGN33.47/', 'TTGN33.48/', 'TTGN33.49/', 'TTGN33.5/', 'TTGN33.50/', 'TTGN33.51/', 'TTGN33.52/', 'TTGN33.53/', 'TTGN33.54/', 'TTGN33.55/', 'TTGN33.56/', 'TTGN33.57/', 'TTGN33.58/', 'TTGN33.59/', 'TTGN33.6/', 'TTGN33.60/', 'TTGN33.61/', 'TTGN33.62/', 'TTGN33.63/', 'TTGN33.64/', 'TTGN33.65/', 'TTGN33.66/', 'TTGN33.67/', 'TTGN33.68/', 'TTGN33.69/', 'TTGN33.7/', 'TTGN33.70/', 'TTGN33.71/', 'TTGN33.72/', 'TTGN33.73/', 'TTGN33.74/', 'TTGN33.75/', 'TTGN33.76/', 'TTGN33.77/', 'TTGN33.78/', 'TTGN33.79/', 'TTGN33.8/', 'TTGN33.80/', 'TTGN33.81/', 'TTGN33.82/', 'TTGN33.83/', 'TTGN33.84/', 'TTGN33.85/', 'TTGN33.86/', 'TTGN33.87/', 'TTGN33.88/', 'TTGN33.89/', 'TTGN33.90/', 'TTGN33.91/', 'TTGN33.92/', 'TTGN33.93/']

# Attach to OptionMenu 
optionmenu = customtkinter.CTkOptionMenu(root, width=240)
optionmenu.pack(fill="x", padx=10, pady=10)

CTkScrollableDropdown(optionmenu, values=values)

# Attach to Combobox
combobox = customtkinter.CTkComboBox(root, width=240)
combobox.pack(fill="x", padx=10, pady=10)

CTkScrollableDropdown(combobox, values=values, justify="left", button_color="transparent")

# Attach to Entry
customtkinter.CTkLabel(root, text="Live Search Values").pack()

entry = customtkinter.CTkEntry(root, width=240)
entry.pack(fill="x", padx=10, pady=10)

_values=[]
for item in values:
    _values.append(item.strip('/'))

CTkScrollableDropdown(entry, values=_values, command=lambda e: entry.insert(1, e),
                      autocomplete=True) # Using autocomplete

# Attach to Button 
button = customtkinter.CTkButton(root, text="choose options", width=240)
button.pack(fill="x", padx=10, pady=10)

CTkScrollableDropdown(button, values=values, height=270, resize=False, button_height=30,
                      scrollbar=False, command=lambda e: button.configure(text=e))

root.mainloop()