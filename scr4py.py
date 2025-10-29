import os
import requests
import colorama
from colorama import Fore, Style

username = os.getlogin()

colorama.init(autoreset=True)

ocean_gradient = [
    Fore.BLUE,         
    Fore.LIGHTBLUE_EX,  
    Fore.CYAN,            
    Fore.LIGHTBLUE_EX,
    Fore.BLUE,
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTBLACK_EX
]

while True:

    os.system("cls" if os.name == "nt" else "clear")

    banner = [       
"\n  ███████╗ ██████╗██████╗ ██╗  ██╗██████╗ ██╗   ██╗",
"  ██╔════╝██╔════╝██╔══██╗██║  ██║██╔══██╗╚██╗ ██╔╝",
"  ███████╗██║     ██████╔╝███████║██████╔╝ ╚████╔╝ ",
"  ╚════██║██║     ██╔══██╗╚════██║██╔═══╝   ╚██╔╝  ",
"  ███████║╚██████╗██║  ██║     ██║██║        ██║   ",
"  ╚══════╝ ╚═════╝╚═╝  ╚═╝     ╚═╝╚═╝        ╚═╝   ",
"                              v1.0 by Nuhphyron <3"
    ]

    for i, line in enumerate(banner):
        print(ocean_gradient[i % len(ocean_gradient)] + line)

    print(f"\n Welcome, {Fore.LIGHTRED_EX}{username}{Style.RESET_ALL}, to the Scr4py CLI!")
    print('''
 You can use this tool to fetch a list of HTTP proxies.
 Made with <3 by Nuhphyron.

 > How would you like to fetch the proxies?

 - 1) Direct Connection
 - 2) Local VPN Proxy
 - 3) Exit
 ''')

    choice = input(f"{Fore.LIGHTGREEN_EX} {username}@scr4per:~$ {Style.RESET_ALL}")

    if choice == "1":
        try:
            response = requests.get("https://www.proxy-list.download/api/v1/get?type=http")
            print("\n Status Code:", response.status_code)
            if response.status_code == 200:
                with open("proxies.txt", "w") as f:
                    f.write(response.text)
                print(" Proxies saved to proxies.txt!")
        except ConnectionResetError as e:
            print(f"\n Connection Reset Error: {e}")
            print(f"\n{Fore.LIGHTYELLOW_EX} Possible Fixes:{Style.RESET_ALL}")
            print(f"   {Fore.LIGHTYELLOW_EX}- Try using the VPN option; your ISP may have blocked the API.{Style.RESET_ALL}")
            print(f"   {Fore.LIGHTYELLOW_EX}- Check your network connectivity.{Style.RESET_ALL}")
        except Exception as e:
            print(f"\n An Error Occurred: {e}")
            print(f"\n {Fore.LIGHTYELLOW_EX}Possible Fixes:{Style.RESET_ALL}")
            print(f"   {Fore.LIGHTYELLOW_EX}- Try using the second option with a local VPN proxy.{Style.RESET_ALL}")
            print(f"   {Fore.LIGHTYELLOW_EX}- Verify network access and retry.{Style.RESET_ALL}")
        input("\n Press Enter to continue...")

    elif choice == "2":
        try:
            proxies = {
                "http": "http://127.0.0.1:8080",
                "https": "http://127.0.0.1:8080"
            }
            response = requests.get("https://www.proxy-list.download/api/v1/get?type=http", proxies=proxies)
            print("\n Status Code:", response.status_code)
            if response.status_code == 200:
                with open("proxies.txt", "w") as f:
                    f.write(response.text)
                print(" Proxies saved to proxies.txt!")
        except ConnectionResetError as e:
            print(f"\n Connection Reset Error: {e}")
            print(f"\n {Fore.LIGHTYELLOW_EX}Possible Fixes:{Style.RESET_ALL}")
            print(f"   {Fore.LIGHTYELLOW_EX}- Verify that the VPN connection is active.{Style.RESET_ALL}")
            print(f"   {Fore.LIGHTYELLOW_EX}- Confirm proxy settings are valid.{Style.RESET_ALL}")
        except Exception as e:
            print(f"\n An Error Occurred: {e}")
            print(f"\n {Fore.LIGHTYELLOW_EX}Possible Fixes:{Style.RESET_ALL}")
            print(f"   {Fore.LIGHTYELLOW_EX}- Verify VPN connectivity.{Style.RESET_ALL}")
            print(f"   {Fore.LIGHTYELLOW_EX}- Recheck proxy configuration.{Style.RESET_ALL}")
        input("\n Press Enter to continue...")

    elif choice == "3":
        break

    else:
        print("\n Please enter 1, 2, or 3!")
        input("\n Press Enter to continue...")
