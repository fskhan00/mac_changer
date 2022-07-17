#!/usr/bin/env python

import optparse
import subprocess

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="this shows interface help")
    parser.add_option("-m","--mac",dest="new_mac",help="this shows mac address help")
    (option,interface) = parser.parse_args()
    if not option.interface:
        parser.error("[+] Please enter the Interface name or --help for help")
    elif not option.new_mac:
        parser.error("[+] Please enter the new mac name or --help for help")
    return option

def change_mac(interface,mac):
    print("[+] Changin the interface "+ interface + "to new mac " + mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw","ether",mac])
    subprocess.call(["ifconfig", interface, "up"])


option = get_arguments()
ifconfig_result = subprocess.check_output(["ifconfig", option.interface])
print(ifconfig_result)



# change_mac(option.interface, option.new_mac)

