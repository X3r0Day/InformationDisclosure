import subprocess
import time
import os
import json
from colorama import Fore, Style

f_check = False
f_type = []

def show_intro():
    os.system("clear" if os.name != "nt" else "cls")
    print(Fore.CYAN + Style.BRIGHT)
    print('''
.___          _____        ________   .__                 
|   |  ____ _/ ____\____   \______ \  |__|  ______  ____  
|   | /    \\   __\/  _ \   |    |  \ |  | /  ___/_/ ___\ 
|   ||   |  \|  | (  <_> )  |    `   \|  | \___ \ \  \___ 
|___||___|  /|__|  \____/  /_______  /|__|/____  > \___  >
          \/                       \/          \/      \/      <33                                                  
    ''')
    print(Fore.GREEN + Style.BRIGHT + "Version: dev-alpha-1.0\n" + Style.RESET_ALL)
    print("Created by: " + Fore.RED, Style.BRIGHT + "X3r0Day" + Style.RESET_ALL)
    print(Fore.YELLOW + "\nA tool to query and analyze archived data from the Wayback Machine.\n" + Style.RESET_ALL)
    time.sleep(2)

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

def basic_query(url):
    command = f"""
    curl -G "https://web.archive.org/cdx/search/cdx" \
    --data-urlencode "url={url}/*" \
    --data-urlencode "collapse=urlkey" \
    --data-urlencode "output=text" \
    --data-urlencode "fl=original"
    """
    return execute_command(command)

def load_extensions(filename='file_extensions.json'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data.get("extensions", [])
    except Exception as e:
        print(Fore.RED + f"Error reading JSON file: {e}")
        return []

def filter_files(query_result, extensions):
    filtered_lines = []
    for line in query_result.splitlines():
        if any(ext in line for ext in extensions):
            filtered_lines.append(line)
    return "\n".join(filtered_lines)

def save_to_file(content, filename='output.txt'):
    with open(filename, 'w') as f:
        f.write(content)
    print(Fore.GREEN + f"Results saved to {filename}.")

def menu():
    show_intro()  # Show the intro when the program starts
    extensions = []
    
    while True:
        os.system('clear')  # For Linux and macOS, 'cls' for Windows
        print(Fore.CYAN + Style.BRIGHT + "===== Menu =====")
        print("1. Execute Basic Query")
        print("2. Load Filter Extensions from JSON")
        print("3. Exit")
        
        choice = input(Fore.YELLOW + "Choose an option: ")

        if choice == '1':
            url = input(Fore.GREEN + "Enter URL to query: ")
            result = basic_query(url)
            
            if extensions:
                result = filter_files(result, extensions)
                print(Fore.GREEN + f"Filtered Result (extensions: {', '.join(extensions)}):\n")
            else:
                print(Fore.GREEN + "Result:\n")
            
            print(result)
            save_to_file(result)  # Save the filtered result to output.txt
            input(Fore.MAGENTA + "Press Enter to continue...")

        elif choice == '2':
            # Load file extensions from JSON file
            extensions = load_extensions()
            if extensions:
                print(Fore.GREEN + f"Loaded extensions: {', '.join(extensions)}")
            else:
                print(Fore.RED + "Failed to load extensions.")
            input(Fore.MAGENTA + "Press Enter to continue...")

        elif choice == '3':
            print(Fore.RED + "Exiting...")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "Invalid choice, please try again.")
            time.sleep(1)

if __name__ == "__main__":
    menu()
