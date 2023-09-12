from netmiko import ConnectHandler
import json
import select_file

def getcdpnei():
    try:
        # Get IP address list from .txt file
        Target_list = select_file.get_ip_list()
    except:
        print("Fail to open file")
    
    try:
        for device in select_file.inventory(Target_list):
            try:
                with ConnectHandler(**device) as net_connect:
                    net_connect.enable()
                    prompt = net_connect.find_prompt()
                    hostname = prompt[0:-1]
                            
                    output = net_connect.send_command('show run int gi 0/2', use_textfsm=True)
                    json_output = json.dumps(output, indent=4)
                    print(output)
                    print()
                    print(json_output)
                    
            except:
                print("\n"+device['host']+" not found")
    except:
        print("Go back to home page\n")
        
getcdpnei()