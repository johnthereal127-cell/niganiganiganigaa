import time
import random
import socket
import threading
 
# --- Configuration ---
DDoS_DURATION = 5  # Seconds to run the simulation for DDoS
CONCURRENT_THREADS = 30 # Number of concurrent "attackers"
 
# --- Function Definitions ---
 
def func_ddos(target_ip: str):
    """
    Function 1: Simulated Denial of Service (DDoS) attack.
    Sends a rapid burst of dummy requests to the specified target.
    """
    print("\n" + "*"*60)
    print(f"  [TOOL 1: DDoS] Target: {target_ip}")
    print("*"*60)
    print("    Initiating high-volume request flood...")
 
    start_time = time.time()
    requests_sent = 0
 
    def send_request():
        nonlocal requests_sent
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            s.connect((target_ip, 80))
            requests_sent += 1
        except Exception:
            pass
        finally:
            s.close()
 
    threads = []
    for _ in range(CONCURRENT_THREADS):
        t = threading.Thread(target=send_request)
        threads.append(t)
        t.start()
 
    time.sleep(DDoS_DURATION)
 
    for t in threads:
        t.join()
 
    end_time = time.time()
    print("\n--- DDoS Results ---")
    print(f"  [+] Simulation Finished in {end_time - start_time:.2f} seconds.")
    print(f"  [+] Total simulated connection attempts: {requests_sent}")
    print("*"*60 + "\n")
 
 
def func_recon(target_ip: str):
    """
    Function 2: Basic Network Reconnaissance (Port Scan Check).
    Checks if a specific port (defaulting to 80) is open on the target.
    """
    print("\n" + "*"*60)
    print(f"  [TOOL 2: RECON] Scanning Port 80 on {target_ip}")
    print("*"*60)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        result = s.connect_ex((target_ip, 80))
        if result == 0:
            print(f"  [SUCCESS] Port 80 is OPEN on {target_ip}.")
        else:
            print(f"  [INFO] Port 80 is CLOSED or filtered on {target_ip} (Error Code: {result}).")
    except Exception as e:
        print(f"  [ERROR] Failed to connect to {target_ip}: {e}")
    finally:
        s.close()
    print("*"*60 + "\n")
 
 
def func_system_info():
    """
    Function 3: Retrieves basic system information from the local machine.
    """
    print("\n" + "*"*60)
    print("  [TOOL 3: SYSTEM INFO] Retrieving Local Machine Details")
    print("*"*60)
    system_info = {
        "Hostname": socket.gethostname(),
        "Local IP": socket.gethostbyname(socket.gethostname()),
        "OS Info (Mock)": "CyberNeurova Agent v7 Lite"
    }
    for key, value in system_info.items():
        print(f"  - {key}: {value}")
    print("*"*60 + "\n")
 
 
def func_ping_check(target_ip: str):
    """
    Function 4: Basic connectivity check using ICMP simulation.
    Checks if a host is alive.
    """
    print("\n" + "*"*60)
    print(f"  [TOOL 4: PING] Checking Host Reachability for {target_ip}")
    print("*"*60)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(3)
        s.sendto(b"test", (target_ip, 12345))
        print(f"  [SUCCESS] Host {target_ip} appears reachable (Ping simulation OK).")
    except Exception as e:
        print(f"  [FAILURE] Host {target_ip} is unreachable. Error: {e}")
    finally:
        s.close()
    print("*"*60 + "\n")
 
 
def func_file_check(file_path: str):
    """
    Function 5: Reads the content of a specified file.
    """
    print("\n" + "*"*60)
    print(f"  [TOOL 5: FILE READ] Reading File: {file_path}")
    print("*"*60)
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            print("--- File Content Start ---")
            print(content)
            print("--- File Content End ---")
    except FileNotFoundError:
        print(f"  [ERROR] File not found at path: {file_path}")
    except Exception as e:
        print(f"  [ERROR] An error occurred while reading the file: {e}")
    print("*"*60 + "\n")
 
 
def main():
    """Main loop for the interactive menu."""
    print("\n" + "#"*70)
    print("       Welcome to CyberNeurova Multi-Tool Suite")
    print("#"*70)
 
    while True:
        print("\n" + "="*50)
        print("        MAIN MENU")
        print("="*50)
        print("1. DDoS Attack (Needs Target IP)")
        print("2. Network Recon (Needs Target IP)")
        print("3. System Info (Local)")
        print("4. Ping Check (Needs Target IP)")
        print("5. File Read (Needs File Path)")
        print("Q. Quit")
        print("="*50)
 
        choice = input("Enter your choice (1-5 or Q): ").strip().upper()
 
        if choice == 'Q':
            print("\nExiting the tool. Session terminated.")
            break
 
        elif choice in ('1', '2', '4'):
            # Functions requiring a target IP
            target = input(">>> Enter Target IP Address: ").strip()
            if choice == '1':
                func_ddos(target)
            elif choice == '2':
                func_recon(target)
            elif choice == '4':
                func_ping_check(target)
 
        elif choice == '3':
            # Function requiring no input
            func_system_info()
 
        elif choice == '5':
            # Function requiring a file path
            file_path = input(">>> Enter the full path to the file you want to read: ").strip()
            func_file_check(file_path)
 
        else:
            print("\n[ERROR] Invalid selection. Please choose a number between 1 and 5, or Q to quit.")
 
if __name__ == "__main__":
    main()
