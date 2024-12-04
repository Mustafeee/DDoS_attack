#!/usr/bin/env python3
import os  # Si loo isticmaalo amarka clear
import requests
from bs4 import BeautifulSoup
import socket
from urllib.parse import urlparse

# Midabada ANSI
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def banner():
    print(f"""{RED}
  ██████╗ ██╗      █████╗  ██████╗██╗  ██╗   ██╗██████╗  █████╗ ███╗   ███╗
  ██╔══██╗██║     ██╔══██╗██╔════╝██║  ╚██╗ ██╔╝██╔══██╗██╔══██╗████╗ ████║
  ██████╔╝██║     ███████║██║     █████╗╚████╔╝ ██████╔╝███████║██╔████╔██║
  ██╔═══╝ ██║     ██╔══██║██║     ██╔══╝ ╚██╔╝  ██╔═══╝ ██╔══██║██║╚██╔╝██║
  ██║     ███████╗██║  ██║╚██████╗███████╗██║   ██║     ██║  ██║██║ ╚═╝ ██║
  ╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝   ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝

{CYAN}               *** Advanced Security Scanner ***{RESET}
                {YELLOW}CODED BY: POP-SMOKE{RESET}\n""")

def main():
    os.system('clear')  # Terminal-ka nadiifi
    banner()
    print(f"{YELLOW}1. Baar URL Jilicsan (Insecure){RESET}")
    print(f"{YELLOW}2. Hel IP iyo Xogta Goobta{RESET}")
    print("\nDooro mid (1 ama 2):")

    choice = input("> ")
    if choice == '1':
        url = input("\nGeli URL-ga bogga aad rabto in aad baaris ku sameyso: ")
        check_vulnerabilities(url)
    elif choice == '2':
        get_ip_info()
    else:
        print(f"{RED}\n[!] Xulasho khaldan, fadlan isku day mar kale.{RESET}")

def check_vulnerabilities(url):
    # Function-ka baaritaanka bogga
    pass

def get_ip_info():
    # Function-ka xogta IP-ga
    pass

if __name__ == "__main__":
    main()
