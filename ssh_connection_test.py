from netmiko import ConnectHandler
import select_file

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
            except:
                print("\n"+device['host']+" not found\n")
    except:
        print("Go back to home page\n")