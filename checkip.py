import requests
import argparse
from colorama import Fore, Style, init

init(autoreset=True)

def check_ip(ip):
    url = f'https://ipinfo.io/{ip}/json'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"Error checking IP: {e}"

def display_info(data):
    red_text = Fore.RED + Style.BRIGHT
    print(f"{red_text}IP Checker")
    print(f"{red_text}Developer: codejavascript")
    print(f"{red_text}Tool Version: v1.1")
    print(f"\n{red_text}[>] [Status]: success")
    print(f"{red_text}[>] [Victim]: {data.get('ip', 'N/A')}")
    print(f"{red_text}[>] [Type]: {data.get('type', 'N/A')}")
    print(f"{red_text}[>] [ISP]: {data.get('org', 'N/A')}")
    print(f"{red_text}[>] [Org]: {data.get('org', 'N/A')}")
    print(f"{red_text}[>] [City]: {data.get('city', 'N/A')}")
    print(f"{red_text}[>] [Region]: {data.get('region', 'N/A')}")
    print(f"{red_text}[>] [RegionName]: {data.get('region', 'N/A')}")
    print(f"{red_text}[>] [Country]: {data.get('country', 'N/A')}")
    print(f"{red_text}[>] [CountryCode]: {data.get('country', 'N/A')}")
    print(f"{red_text}[>] [Country Type]: {'N/A'}")
    print(f"{red_text}[>] [Latitude]: {data.get('loc', 'N/A').split(',')[0]}")
    print(f"{red_text}[>] [Longitude]: {data.get('loc', 'N/A').split(',')[1]}")
    print(f"{red_text}[>] [Time zone]: {data.get('timezone', 'N/A')}")
    print(f"{red_text}[>] [Zip code]: {data.get('postal', 'N/A')}")
    print(f"{red_text}[>] [Offset]: {'N/A'}")
    print(f"{red_text}[>] [Utc offset]: {'N/A'}")
    print(f"{red_text}[>] [Currency]: {'N/A'}")
    print(f"{red_text}[>] [Continent]: {'N/A'}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IP address checker using ipinfo.io")
    parser.add_argument('-t', '--target', type=str, required=True, help='IP address to check')
    args = parser.parse_args()

    ip_info = check_ip(args.target)
    if isinstance(ip_info, dict):
        display_info(ip_info)
    else:
        print(ip_info)
