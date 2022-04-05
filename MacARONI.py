#!/usr/bin/evr python
print("""

███╗░░░███╗░█████╗░░█████╗░░█████╗░██████╗░░█████╗░███╗░░██╗██╗
████╗░████║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗░██║██║
██╔████╔██║███████║██║░░╚═╝███████║██████╔╝██║░░██║██╔██╗██║██║
██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██╔══██╗██║░░██║██║╚████║██║
██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚███║██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝


██████╗░██╗░░░██╗  ██╗░░██╗░░██╗██╗░██╗░░░░░░░██╗███╗░░██╗██████╗░
██╔══██╗╚██╗░██╔╝  ██║░██╔╝░██╔╝██║░██║░░██╗░░██║████╗░██║██╔══██╗
██████╦╝░╚████╔╝░  █████═╝░██╔╝░██║░╚██╗████╗██╔╝██╔██╗██║██████╔╝
██╔══██╗░░╚██╔╝░░  ██╔═██╗░███████║░░████╔═████║░██║╚████║██╔══██╗
██████╦╝░░░██║░░░  ██║░╚██╗╚════██║░░╚██╔╝░╚██╔╝░██║░╚███║██║░░██║
╚═════╝░░░░╚═╝░░░  ╚═╝░░╚═╝░░░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝╚═╝░░╚═╝
""")
import subprocess
import random
command_1 = "ifconfig"
object_1 = "wlan0"
list_1 = []
x = input("Do you want a randomised mac address? (y for yes) > ")
if x == "y":
    for i in range(6):
        a = random.randint(10, 99)
        a = str(a)
        list_1.append(a)
    new_mac_1 = str(":".join(list_1))
else:
    new_mac_1 = input("Please separate each pair with a : > ")
subprocess.call("%s %s down" % (command_1,object_1), shell=True)
subprocess.call("%s %s hw ether %s" % (command_1,object_1,new_mac_1), shell=True)
subprocess.call("%s %s up" % (command_1,object_1), shell=True)
print("[+] Your mac addres for "+ object_1 +" has been changed to "+ new_mac_1 +".")
