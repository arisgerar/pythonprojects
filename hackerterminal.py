import os
import time
from colorama import init

# Enable colors on Windows
init()

GREEN = "\033[92m"
RESET = "\033[0m"

# Clear terminal
os.system("cls" if os.name == "nt" else "clear")

logo = GREEN + r"""

██╗██████╗  ██████╗ ███╗   ██╗     ██████╗ ██████╗ ██████╗ ██████╗  █████╗
██║██╔══██╗██╔═══██╗████╗  ██║    ██╔════╝██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
██║██████╔╝██║   ██║██╔██╗ ██║    ██║     ██║   ██║██████╔╝██████╔╝███████║
██║██╔══██╗██║   ██║██║╚██╗██║    ██║     ██║   ██║██╔══██╗██╔══██╗██╔══██║
██║██║  ██║╚██████╔╝██║ ╚████║    ╚██████╗╚██████╔╝██████╔╝██║  ██║██║  ██║
╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

=====================================================================
                         IRON COBRA
                 ADVANCED NETWORKING INTERCEPTOR
                         Version 2.4
=====================================================================

""" + RESET

print(logo)

boot = [
    "Loading core modules...",
    "Initializing secure terminal...",
    "Loading network scanner...",
    "Loading system database...",
    "Loading encrypted modules...",
    "Verifying user ids...",
    "Establishing secure connection...",
    "System online."
]

for line in boot:
    print(GREEN + "[+]" + RESET, line)
    time.sleep(0.6)

print()
input(GREEN + "Press ENTER to continue..." + RESET)

# Clear screen before your game starts
os.system("cls" if os.name == "nt" else "clear")



import time
import random

wanted_chance = 5

print("Connecting to server...")

for i in range(11):
    bar = "█" * i
    print(f"[{bar:<10}] {i*10}%")
    
    wait_time = random.uniform(0.1, 1)
    time.sleep(wait_time)

    if random.randint(1, 10) == 1:
        print("Connection unstable...")
        time.sleep(2)

print("Connected!")
time.sleep(2)


while True:

    print("\nScanning IP addresses...\n")

    devices = ["DESKTOP", "PHONE", "ROUTER", "LAPTOP", "SERVER"]

    for i in range(5):
        ip = f"192.168.1.{random.randint(2, 254)}"
        device = random.choice(devices)
        ping = random.randint(5, 80)

        print(f"[FOUND] {ip} | {device} | {ping}ms")
        time.sleep(random.uniform(0.3, 1))
        
    time.sleep(1)
    print("\nScan complete.")

    if random.randint(1, 2) == 1:
        print("TARGET FOUND!")

        while True:
            choice = input("""
Choose an action:

1. Infect system
2. Launch DDoS attack
3. Start crypto mining
4. Demand bitcoin

> """)

            if choice == "1":
                print("\nDeploying virus...")
                time.sleep(2)

                if random.randint(1, 2) == 1:
                    print("SYSTEM COMPROMISED!")
                else:
                    print("Attack failed!")

            elif choice == "2":
                print("\nLaunching simulated traffic flood...")
                time.sleep(2)

                if random.randint(1, 3) == 1:
                    print("TARGET OVERLOADED!")
                else:
                    print("Target firewall blocked the attack!")

            elif choice == "3":
                print("\nStarting fictional crypto miner...")
                time.sleep(2)

                if random.randint(1, 2) == 1:
                    print("Mining complete!")
                    print("You earned 0.004 fake coins")
                else:
                    print("Mining detected and stopped!")

            elif choice == "4":
                print("\nSending fake ransom message...")
                time.sleep(2)

                if random.randint(1, 4) == 1:
                    print("Target paid the ransom!")
                    print("You earned 500 fake coins")
                else:
                    print("Target refused to pay!")

            else:
                print("Invalid choice")

            # Increase police chance after every action
            wanted_chance = min(wanted_chance * 2, 90)

            print(f"\nPolice detection chance: {wanted_chance}%")

            if random.randint(1, 100) <= wanted_chance:
                print("\n🚨 POLICE FOUND YOU!")
                print("Your terminal has been shut down.")
                exit()

            again_action = input("\nTry another action on this target? (y/n): ")

            if again_action.lower() != "y":
                break

    else:
        print("TARGET NOT FOUND.")

    again_scan = input("\nScan for another target? (y/n): ")

    if again_scan.lower() != "y":
        print("Closing terminal...")
        break