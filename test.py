from netmiko import ConnectHandler

ip_list = ["192.168.159.100"]
device_inventory = []

for ip in ip_list:
    device = {
        "device_type": "cisco_ios_telnet",
        "host": ip,
        "username": "admin",
        "password": "admin"
    }
    device_inventory.append(device)
    
for device in device_inventory:
    try:
        with ConnectHandler(**device) as net_connect:
            print(net_connect.find_prompt()+" is ready")
    except:
        print("\n"+device['host']+" not found")