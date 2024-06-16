import requests
from colorama import Fore, Style, init
import time
import threading
import speedtest

init(autoreset=True)

message = 'IP Checking...'

def loading_animation(stop_event):
    animation = "|/-\\"
    idx = 0
    while not stop_event.is_set():
        print(f"\r{Fore.RED}{message} {animation[idx % len(animation)]}", end="")
        idx += 1
        time.sleep(0.2)

def results():
    global message
    stop_event = threading.Event()
    thread = threading.Thread(target=loading_animation, args=(stop_event,))
    thread.start()

    try:
        response = requests.get("https://ipleak.net/json/")
        if response.status_code == 200:
            data = response.json()
            ip = data['ip']
            country_name = data['country_name']
            region_name = data['region_name']
            isp_name = data['isp_name']
            city_name = data['city_name']
            message = "Internet Speed checking..."
            print(f"\n\n{Fore.GREEN}       IP INFORMATION\n{Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f" ━{Fore.BLUE} Your IP:  {Fore.RED}{ip}")
            print(f" ━{Fore.BLUE} ISP Name: {Fore.GREEN}{isp_name}")
            print(f" ━{Fore.BLUE} Country:  {Fore.YELLOW}{country_name}")
            print(f" ━{Fore.BLUE} Region:   {Fore.CYAN}{region_name}")
            print(f" ━{Fore.BLUE} City:     {Fore.LIGHTRED_EX}{city_name}")
        else:
            print(f"\n{Fore.YELLOW}No internet{Style.RESET_ALL}")
            return

        st = speedtest.Speedtest()
        download_speed = st.download()
        upload_speed = st.upload()
        res = st.results.dict()

        print(f"\n ━{Fore.BLUE} Download speed: {res['download'] / 1_000_000:.2f} Mbps")
        print(f" ━{Fore.BLUE} Upload speed: {res['upload'] / 1_000_000:.2f} Mbps")
        print(f" ━{Fore.BLUE} Ping: {res['ping']} ms")
        print(f"{Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Style.RESET_ALL}\n")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}ERROR: No Internet: {e}{Style.RESET_ALL}")
    finally:
        stop_event.set()
        thread.join()
        # Clear the loading animation line
        print("\r" + " " * 40, end="\r")

results()
