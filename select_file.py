import tkinter as tk
from tkinter import filedialog
from getpass import getpass

def get_file_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.destroy()
    return file_path

def get_ip_list():    
    # Select file 
    print("Select target devices in .txt file (IP address list): ")
    selected_file = get_file_path()
    print(f"Selected file: {selected_file}")
    # Open file that you selected
    with open(selected_file, 'r') as file:
        # Use list comprehension to create a list of items from each line
        switch_list = file.read().splitlines()
        return switch_list

def get_conf_file():
    # Select file 
    print("\nChoose configurtion file (.txt): ")
    selected_file = get_file_path()
    print(f"Selected file: {selected_file}")
    return selected_file

def inventory(list):
    device_inventory = []
    username = str(input("Username: "))
    password = str(getpass("Password: "))
    secret = str(getpass("Enable password: "))

    for ip in list:
        device = {
            "device_type": "cisco_ios",
            "host": ip,
            "username": username,
            "password": password,
            "secret": secret  # Enable password
        }
        device_inventory.append(device)
    return device_inventory