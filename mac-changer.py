#!/usr/bin/env python
import subprocess
import optparse
from pyfiglet import Figlet
from colorama import Fore, Style

def change_mac(interface, new_mac):
    print("[+] Changing MAC for interface " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Specify interface to change MAC for,  use --help for usage")
    parser.add_option("-m", "--mac", dest="new_mac", help="Specify the new MAC , use --help for usage")
    (options, agruments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify interface, use --help for usage")
    elif not options.new_mac:
        parser.error("[-] Please specify MAC , use --help for usage")
    return options

def print_banner():
    f = Figlet(font='slant')
    colored_banner = Fore.GREEN + f.renderText('MAC Changer') + Style.RESET_ALL
    creator_text = Fore.CYAN + "Script Creator: Sami Khatatba" + Style.RESET_ALL
    print(colored_banner)
    print(creator_text)

def show_menu():
    print(Fore.YELLOW + "\n===== MAC Changer Menu =====" + Style.RESET_ALL)
    print("1. Change MAC Address")
    print("2. Show Current MAC Address")
    print("3. Exit")

def get_current_mac(interface):
    try:
        output = subprocess.check_output(["ifconfig", interface])
        return output.decode('utf-8')
    except subprocess.CalledProcessError:
        return None

def main():
    while True:
        show_menu()
        choice = input(Fore.CYAN + "\nEnter your choice (1-3): " + Style.RESET_ALL)
        
        if choice == '1':
            interface = input("Enter interface name: ")
            new_mac = input("Enter new MAC address: ")
            change_mac(interface, new_mac)
        elif choice == '2':
            interface = input("Enter interface name: ")
            mac_info = get_current_mac(interface)
            if mac_info:
                print(Fore.GREEN + "\nCurrent MAC Info:\n" + Style.RESET_ALL)
                print(mac_info)
            else:
                print(Fore.RED + "[-] Could not retrieve MAC info for interface" + Style.RESET_ALL)
        elif choice == '3':
            print(Fore.YELLOW + "\nExiting..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "[-] Invalid choice, please try again" + Style.RESET_ALL)

if __name__ == "__main__":
    print_banner()
    main()
