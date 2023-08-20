from netmiko import ConnectHandler 
from time import sleep
import tkinter as tk
from tkinter import filedialog
import select_file

# Dictionary
vlans = {}
# Array
vlans_remove = []
check_input = ""

def add():
    while True: # If input is string, will be loop
        # Number of vlans 
        try:
            add_vlan_total = int(input("How many VLANs add: "))
            break
        except:
            print("% Please enter number only %")
            continue

    for i in range (add_vlan_total):
        while True: # If input is string, will be loop
            try:
                # Enter number VLAN
                vl_num_value = int(input("vlan "))
                break
            except:
                print("% Please enter number only %")
                continue
        name_key = input("  name ") # name VLAN
        # Set Name as kay and VLAN number as value
        vlans[vl_num_value] = name_key
                
    try:
        # Get ip list from .txt file
        Target_list = select_file.get_ip_list()
        print("\n--- Vlan summary ---") 
        for key,value in vlans.items(): # Print all VLAN that will be configured
            print(key, ':', value)
        print("\n--- List of target device ---")
        print(*Target_list, sep = "\n") # Print ip address Targets
    except:
        print("Fail to open file")
    
    try:
        # Decision "yes" or "no" if do not enter any letter by defualt is "no"
        print("\nPlease check information above before post configure")
        while True:
            check_input = str(input("Post configure[y/n](n): "))
            if check_input == "Y" or check_input == "y":
                for device in select_file.inventory(Target_list):
                    try:
                        with ConnectHandler(**device) as net_connect:
                            
                            # Configure VLAN <1-4094> name WORD
                            for k, v in vlans.items():
                                commands = [f"vlan {k}", f"name {v}"]
                                config_output = net_connect.send_config_set(commands) # Send config to network device

                            print("\n----------"+net_connect.find_prompt()+"---------")
                            print("\n----------"+device["host"]+"---------")
                            print(net_connect.send_command("sh vl br"))
                            print("")
                            # Write memory
                            net_connect.save_config()
                            
                    except:
                        print(device['host'] + " fail")
                break
            elif check_input == "N" or check_input == "n" or check_input == "":
                print("Cancel configure")
                sleep(3)
                break
            else:
                print("% please enter y/n %")
                continue
    except:
        print("Go back to home page\n")

def remove():
    while True: # If input is string, will be loop
        try:
            # Number of vlans 
            add_vlan_total = int(input("How many VLANs remove: "))
            break
        except:
            print("% Please enter number only %")
            continue

    for i in range (add_vlan_total):
        while True: # If input is string, will be loop
            try:
                # Enter number VLAN
                vl_num_value = int(input("no vlan "))
                break
            except:
                print("% Please enter number only %")
                continue
        vlans_remove.append(vl_num_value)
        
    try:
        #Open ip list from .txt file
        Target_list = select_file.get_ip_list()
        print("\n--- Vlan summary ---")
        for j in vlans_remove: # Print all VLAN that will be configured
            print("no vlan {}".format(j))
        print("\n--- List of target device ---")
        print(*Target_list, sep = "\n") # Print ip address targets
    except:
        print("Fail to open file")
        
    try:
        # Decision "yes" or "no" if do not enter any letter by defualt is "no" 
        print("\nPlease check information above before post configure")
        while True:
            check_input = str(input("Post configure[y/n](n): "))
            if check_input == "Y" or check_input == "y":
                for device in select_file.inventory(Target_list):
                    try:
                        with ConnectHandler(**device) as net_connect:

                            # Configure no vlan [number]
                            for j in vlans_remove:
                                commands = ["no vlan {}".format(j)]
                                # send config to network devices
                                config_output = net_connect.send_config_set(commands)

                            print("\n----------"+net_connect.find_prompt()+"---------")
                            print("\n----------"+device["host"]+"---------")
                            print(net_connect.send_command("sh vl br"))
                            print("")
                            # Write memory
                            net_connect.save_config()
                            
                    except:
                        print(device['host'] + " fail")
                break
            elif check_input == "N" or check_input == "n" or check_input == "":
                print("Cancel configure\n")
                sleep(3)
                break
            else:
                print("% please enter y/n %")
                continue
    except:
        print("Go back to home page\n")