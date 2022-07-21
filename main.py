import subprocess
import re

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

wifi_list = []

for name in profile_names:
    profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
    type = re.search("Type                   : (.*)\r", profile_info_pass)
    password = re.search("Key Content            : (.*)\r", profile_info_pass)
    type = type[1] if type is not None else None
    password = password[1] if password is not None else None
    wifi_list.append({"name": name, "type": type, "password": password}) 

size = 50

print("\n")
for wifi in wifi_list:
    print(f'{"".ljust(size//2-(len(wifi["name"])//2))}{wifi["name"]}')
    print("\u250C"+"\u2500"*size+"\u2510")
    print(f'\u2502 Type: {wifi["type"]}'.ljust(size+1)+"\u2502")
    print(f'\u2502 Password: {wifi["password"]}'.ljust(size+1)+"\u2502")
    print("\u2514"+"\u2500"*size+"\u2518\n")


