import time 
from netmiko import ConnectHandler 
import select_file

def send(device,net_connect,conf_file):
    # device> Enable
    net_connect.enable()
    prompt = net_connect.find_prompt()
    hostname = prompt[0:-1]
    
    # Send config to network device
    print("\n"+hostname+" : "+ device['host'])
    result = net_connect.send_config_from_file(conf_file)
    print("Yeah!!")
    # Write memory
    net_connect.save_config()    

def start():
    try:
        # Get ip list from .txt file
        Target_list = select_file.get_ip_list()
        # Push ip address into device inventory 
        device_profiles = select_file.inventory(Target_list)
        print("\n--- List of target device ---")
        print(*Target_list, sep = "\n")
        
        # Get config file path
        conf_file = select_file.get_conf_file()
        # Open conf_file and show content inside
        print("\nConfig inside your file: ")
        with open(conf_file,'r') as cf:
            Preview_conf = cf.read()
            print(Preview_conf+"\n")
    except:
        print("Fail to open file")
    
    try:
        while True:
            # Decision "yes" or "no" if do not enter any letter by defualt is "no"
            check_input = str(input("Post configure[y/n](n): "))
            if check_input == "Y" or check_input == "y":
                for device in device_profiles:
                    
                    try:
                        with ConnectHandler(**device) as net_connect:
                            send(device,net_connect,conf_file)
                            SSH_active = True  
                    except:
                        print(device['host']+" - Configure fail")
                        SSH_active = True 
                    try:    
                        if SSH_active == False:
                            print("Trying telnet...")
                            device["device_type"] = "cisco_ios_telnet"
                            with ConnectHandler(**device) as net_connect:
                                send(device,net_connect,conf_file)
                    except: 
                        print("Backup fail")
                        SSH_active = False
                         
                break
            elif check_input == "N" or check_input == "n" or check_input == "":
                print("Cancel configure\n")
                time.sleep(3)
                break
            else:
                print("% please enter y/n %")
                continue
    except:
        print("Go back to home page\n")