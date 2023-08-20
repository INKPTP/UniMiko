from netmiko import ConnectHandler
import time
import select_file

def start():
    try:
        #Open ip list from .txt file
        Target_list = select_file.ip_list()
        device_profiles = select_file.inventory(Target_list)
        print("\n--- List of target device ---")
        print(*Target_list, sep = "\n")
    except:
        print("Fail to open file")
    
    try:
        print("\nPlease check information above before start backup")
        while True:
            check_input = str(input("Start backup [y/n](n): "))
            if check_input == "Y" or check_input == "y":
                for device in device_profiles:
                    try:
                        with ConnectHandler(**device) as net_connect:
                            net_connect.enable()
                            prompt = net_connect.find_prompt()
                            hostname = prompt[0:-1]
                            
                            print("\n"+hostname+" : "+ device['host']+"\n")
                            output1 = net_connect.send_command('show clock')
                            output2 = net_connect.send_command('show version')
                            output3 = net_connect.send_command('show inventory')
                            output5 = net_connect.send_command('show run')
                            output4 = net_connect.send_command('show switch')
                            output6 = net_connect.send_command('show ip int bri')
                            output7 = net_connect.send_command('show int status')
                            output8 = net_connect.send_command('show int des')
                            output9 = net_connect.send_command('show cdp nei')
                            output10 = net_connect.send_command('show cdp nei detail')
                            output11 = net_connect.send_command('show ether sum')
                            output12 = net_connect.send_command('show spanning-tree summary')
                            output13 = net_connect.send_command('show arp')
                            output14 = net_connect.send_command('show mac address-table')
                            output15 = net_connect.send_command('show logging')
                            output16 = net_connect.send_command('show int description')
                            
                            with open("{}.txt".format(device['host']), "w") as f:
                                f.writelines('{}#\n'.format(hostname))
                                f.writelines('#####{}#####\n'.format(device['host']))
                                f.writelines('@#show clock\n')
                                f.writelines(output1)
                                f.writelines('@#show version\n')
                                f.writelines(output2)
                                f.writelines('@#show inventory\n')
                                f.writelines(output3)
                                f.writelines('@#show switch\n')
                                f.writelines(output4)
                                f.writelines('@#show run\n')
                                f.writelines(output5)
                                f.writelines('@#show ip int bri\n')
                                f.writelines(output6)
                                f.writelines('@#show int status\n')
                                f.writelines(output7)
                                f.writelines('@#show int des\n')
                                f.writelines(output8)
                                f.writelines('@#show cdp nei\n')
                                f.writelines(output9)
                                f.writelines('@#show cdp nei detail\n')
                                f.writelines(output10)
                                f.writelines('@#show ether sum\n')
                                f.writelines(output11)
                                f.writelines('@#show spanning-tree summary\n')
                                f.writelines(output12)
                                f.writelines('@#show arp\n')
                                f.writelines(output13)
                                f.writelines('@#show mac address-table\n')
                                f.writelines(output14)
                                f.writelines('@#show logging\n')
                                f.writelines(output15)
                                f.writelines('@#show int description\n')
                                f.writelines(output16)
                                print('Backup Successfully!!')
                    except:
                        print(device['host']+" - Backup fail")
                time.sleep(3)
                break
            elif check_input == "N" or check_input == "n" or check_input == "":
                print("Cancel backup")
                time.sleep(3)
                break
            else:
                print("% please enter y/n %")
                continue
    except:
        print("Go back to home page\n")