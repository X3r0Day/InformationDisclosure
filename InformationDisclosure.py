import subprocess
import time
import os
from colorama import Fore, Style

f_check = False
f_type = []

def execute_command(command):
    """
    Executes a shell command and captures the output.
    Returns stdout if successful, or stderr if there is an error.
    """
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"


def basic_query(url):
    """
    Executes a basic query for the given URL using the Wayback Machine CDX API.
    """
    command = f"""
    curl -G "https://web.archive.org/cdx/search/cdx" \
    --data-urlencode "url={url}/*" \
    --data-urlencode "collapse=urlkey" \
    --data-urlencode "output=text" \
    --data-urlencode "fl=original"
    """
    return execute_command(command)


def filtered_query(url, extensions):
    """
    Executes a filtered query for the given URL and file extensions using the Wayback Machine CDX API.
    """
    command = f"""
    curl "https://web.archive.org/cdx/search/cdx?url={url}/*&collapse=urlkey&output=text&fl=original&filter=original:.*\\.({extensions})$" | tee output.txt
    """
    return execute_command(command)


def files_type():
    global f_type
    f_type = input("Enter the file type: (e.g. pdf|txt|xml or txt)\n> ").split("|")
    global f_check
    f_check = True


def show_intro():
    os.system("clear" if os.name != "nt" else "cls")
    print(Fore.CYAN + Style.BRIGHT)
    print('''
.___          _____        ________   .__                 
|   |  ____ _/ ____\____   \______ \  |__|  ______  ____  
|   | /    \\   __\/  _ \   |    |  \ |  | /  ___/_/ ___\ 
|   ||   |  \|  | (  <_> )  |    `   \|  | \___ \ \  \___ 
|___||___|  /|__|  \____/  /_______  /|__|/____  > \___  >
          \/                       \/          \/      \/ 33                                                  
    ''')
    print(Fore.GREEN + Style.BRIGHT + "Version: dev-alpha-1.0\n" + Style.RESET_ALL)
    print("Created by: " + Fore.RED, Style.BRIGHT + "X3r0Day" + Style.RESET_ALL)
    print(Fore.YELLOW + "\nA tool to query and analyze archived data from the Wayback Machine.\n" + Style.RESET_ALL)
    time.sleep(2)


def main():
    global f_check
    global f_type

    show_intro()

    while True:
        print("\n*** Information Disclosure Tool ***\n")
        print("1. Basic Query: Fetch all URLs for a given site.")
        print("2. Filtered Query: Fetch URLs for specific file types (e.g., pdf, json, xlsx).")
        print("3. Enter file type you want to search for.")
        print("4. Exit.")
        
        choice = input("\nChoose an option (1, 2, 3, or 4): ").strip()

        if choice == "4":
            print("Exiting the program.")
            break

        if choice not in ["1", "2", "3"]:
            print("Invalid choice. Please try again.")
            continue

        if choice == "3":
            files_type()
            continue # This thing took me time to fix 😭 I wasn't able to make it run files_type function lmfao

        url = input("\nEnter the site (e.g., example.com): ").strip()
        if not url:
            print("URL cannot be empty. Please try again.")
            continue

        if choice == "1":
            print("\nExecuting Basic Query...\n")
            output = basic_query(url)

        elif choice == "2":
            if f_check:
                extensions = f_type
            else:
                extensions = [
                    "xls", "xml", "xlsx", "json", "pdf", "sql", "doc", "docx", "pptx", "txt",
                    "git", "zip", "tar.gz", "tgz", "bak", "7z", "rar", "log", "cache", "secret",
                    "db", "backup", "yml", "gz", "config", "csv", "yaml", "md", "md5", "exe",
                    "dll", "bin", "ini", "bat", "sh", "tar", "deb", "rpm", "iso", "img", "env",
                    "apk", "msi", "dmg", "tmp", "crt", "pem", "key", "pub", "asc"
                ]
            print("\nExecuting Filtered Query...\n")
            output = filtered_query(url, extensions)

        output_file = "output.txt"
        with open(output_file, "w") as file:
            file.write(output)

        print(f"\nQuery results have been saved to '{output_file}'.\n")
        print("Output Preview:\n")
        print(output)


if __name__ == "__main__":
    main()
