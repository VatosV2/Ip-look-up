import requests                                                                                                                                                                                                                    
import colorama
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def write_all_infos(a, b, c, d, ip_address):
    with open("output/ipinfo_" + ip_address + "_.txt", "w") as file:
            file.write(a + "\n")
            file.write(b + "\n")
            file.write(c + "\n")
            file.write(d + "\n")

def get_ip_info(ip):
    url = f"https://tex-api.com/ipApi.php?ip={ip}"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    clear()
    print(colorama.Fore.LIGHTMAGENTA_EX + '''
                    ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗   ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                    ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                    ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗█████╗██║   ██║   ██║██║   ██║██║     ███████╗
                    ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║
                    ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║      ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                    ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                discord.gg/nexus-tools
    ''')

    lc = (colorama.Fore.RESET + "[" + colorama.Fore.LIGHTMAGENTA_EX + ">" + colorama.Fore.RESET + "]")
    ip_address = input(lc + "Enter IP to look up: ")

    print(colorama.Fore.GREEN + "Looking up infos to " + ip_address)
    print(colorama.Fore.RESET)
    ip_info = get_ip_info(ip_address)

    if "city" in ip_info:
        city = ip_info["city"]
    if "ip_start" in ip_info:
        ip_start = ip_info["ip_start"]
    if "country" in ip_info:
        country = ip_info["country"]
    if "region" in ip_info:
        region = ip_info["region"]

    a = "IP: " + ip_start
    b = "City: " + city
    c = "Country: " + country
    d = "Region: " + region

    print(a)
    print(b)
    print(c)
    print(d)
    print()
    print()
    print(colorama.Fore.GREEN + "Writng infos into ipinfo_" + ip_address + ".txt")
    write_all_infos(a, b, c, d, ip_address)
    input()


main()
