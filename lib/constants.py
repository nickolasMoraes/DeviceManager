import os

root_path = f"{os.path.normpath(os.path.dirname(__file__))}"
root_path = root_path.strip('\\lib')

adb_path = f"{root_path}\\lib\\utilities\\platform-tools\\adb.exe "
fastboot_path = f"{root_path}\\lib\\utilities\\platform-tools\\fastboot.exe "
refresh_button = f"{root_path}\\assets\\refresh.png "