import time
from netmiko import ConnectHandler 
import select_file

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
        #Open command template from .txt file
        print("\nContent inside your file: ")
        with open(conf_file,'r') as f:
            command_list = f.read().splitlines()
            print(*command_list, sep = "\n")
    except:
        print("Fail to open file")
    
    try:
        print("\nPlease check information above before start backup")
        while True:
            # Decision "yes" or "no" if do not enter any letter by defualt is "no"
            check_input = str(input("Start backup [y/n](n): "))
            if check_input == "Y" or check_input == "y":
                for device in device_profiles:
                    try:
                        with ConnectHandler(**device) as net_connect:
                            # device> Enable
                            net_connect.enable()
                            prompt = net_connect.find_prompt()
                            hostname = prompt[0:-1]
                            
                            # print hostname and IP address
                            print("\n"+hostname+" : "+ device['host']+"")
                            # Create {ip address}.txt file 
                            with open("{}.txt".format(device['host']), "w") as f:
                                for command in command_list:
                                    # Write {device name}# {command} into file
                                    f.writelines("\n"+hostname+"# "+command+"\n")
                                    # Write command output into file
                                    f.writelines(net_connect.send_command(command))
                                print('Backup Success!!')          
                    except:
                        print("Backup fail")
                break
            elif check_input == "N" or check_input == "n" or check_input == "":
                print("Cancel backup\n")
                time.sleep(3)
                break
            else:
                print("% please enter y/n %")
                continue
    except:
        print("Go back to home page\n")        