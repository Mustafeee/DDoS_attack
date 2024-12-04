#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
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

def check_vulnerabilities(url):
    try:
        print(f"{CYAN}[INFO]{RESET} Baaritaanka URL-ka: {url}")
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"{RED}[!] Qalad: Bogga ma furmo. Status-ka: {response.status_code}{RESET}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"{GREEN}[+] Falanqeyn lagu sameeyay URL-ka!{RESET}\n")

        # Baaritaanka Links aan HTTPS lahayn
        links = soup.find_all('a', href=True)
        print(f"{CYAN}[INFO]{RESET} Links aan HTTPS lahayn:")
        insecure_links = 0
        for link in links:
            href = link['href']
            if not href.startswith('https://') and not href.startswith('#') and not href.startswith('mailto:'):
                print(f"  {RED}- {href}{RESET}")
                insecure_links += 1
        if insecure_links == 0:
            print(f"{GREEN}  Dhammaan links-yada waa HTTPS.{RESET}")

        # Baaritaanka foomamka
        forms = soup.find_all('form')
        print(f"\n{CYAN}[INFO]{RESET} Foomamka la helay: {len(forms)}")
        for form in forms:
            action = form.get('action', 'Aan la cayimin')
            if not action.startswith('https://') and not action.startswith('/'):
                print(f"  {RED}- Foom aan HTTPS lahayn: {action}{RESET}")
        if not forms:
            print(f"{GREEN}  Foommo lama helin.{RESET}")

        # Baaritaanka JavaScript iyo XSS
        print(f"\n{CYAN}[INFO]{RESET} Baaritaanka XSS Jilicsan:")
        scripts = soup.find_all('script')
        for script in scripts:
            if script.string and re.search(r'<script>', script.string, re.IGNORECASE):
                print(f"  {RED}- Waxaa laga yaabaa in XSS laga helo!{RESET}")

        # Whois iyo IP xogta
        domain = urlparse(url).netloc
        ip_address = socket.gethostbyname(domain)
        print(f"\n{CYAN}[INFO]{RESET} IP Address ee {domain}: {YELLOW}{ip_address}{RESET}")

    except requests.RequestException as e:
        print(f"{RED}[!] Qalad: {e}{RESET}")
    except socket.gaierror:
        print(f"{RED}[!] Qalad: Lama heli karo IP-ga domain-ka {domain}.{RESET}")

def get_ip_info():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        ip = data.get('ip', 'Lama helin')
        location = f"{data.get('city', 'Lama helin')}, {data.get('region', 'Lama helin')}, {data.get('country', 'Lama helin')}"
        loc_details = data.get('loc', 'Lama helin')

        print(f"{GREEN}\n=== Xogta IP Address ==={RESET}")
        print(f"{CYAN}[+] IP Address: {ip}{RESET}")
        print(f"{CYAN}[+] Goobta: {location}{RESET}")
        print(f"{CYAN}[+] Faahfaahinta Goobta (Latitude, Longitude): {loc_details}{RESET}")

    except requests.RequestException as e:
        print(f"{RED}[!] Qalad: {e}{RESET}")

if __name__ == "__main__":
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
