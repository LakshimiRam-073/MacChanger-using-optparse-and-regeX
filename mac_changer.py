#!usr/bin/env python

import subprocess
import optparse
import  re

def get_info ():
    parse = optparse.OptionParser()
    parse.add_option("-i", "--interface", dest="interface", help="THIS IS USED TO CHANGE MAC ADDRESS")
    parse.add_option("-m", "--macaddress", dest="new_mac", help="INPUT A NEW MAC ADDRESS")
    (options , arguments)=parse.parse_args()
    if not options.interface:
        parse.error("[-] specify the interface , or type --help for  he lp  menu")
    elif not  options.new_mac:
        parse.error("[-] specify the  new mac , or type --help for  he lp  menu")
    return options


def change_mac (interface, new_mac):
    print('[+]changing mac address...')
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)

def geting_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_search:
        return mac_search.group(0)
    else:
        print("[-]could not find mac address")



options =get_info()
current_mac=geting_mac(options.interface)
print("current mac ="+str(current_mac))
change_mac(options.interface,options.new_mac)

new_macadd=geting_mac(options.interface)
if new_macadd == geting_mac(options.interface):
    print("[+}MAC ADDRESS CHANGED")
    print("NEW MAC ="+str(new_macadd))
else:
    print("[-]MAC ADDRESS NOT CHANGED")


