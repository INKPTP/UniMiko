from netmiko import ConnectHandler
import select_file
import Cisco_ios

def status():
    try:
        # Get IP address list from .txt file
        Target_list = select_file.get_ip_list()
    except:
        print("Fail to open file")
    
    try:    
        for device in select_file.inventory(Target_list):
            try:
                with ConnectHandler(**device) as net_connect:
                    print("\n----------"+device['host']+"---------")
                    print(net_connect.find_prompt()+" is ready")
                    SSH_active = True
            except:
                print("\n"+device['host']+" not found")
                SSH_active = False
            
            try:    
                if SSH_active == False:
                    print("Trying telnet...")
                    device["device_type"] = "cisco_ios_telnet"
                    with ConnectHandler(**device) as net_connect:
                        print("\n----------"+device['host']+"---------")
                        print(net_connect.find_prompt()+" is ready")
            except: 
                print("\n"+device['host']+" not found")
            
    except:
        print("Go back to home page\n")
        