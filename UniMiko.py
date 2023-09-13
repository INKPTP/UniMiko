import vlan
import Backupv2
import loading
import ssh_connection_test
import send_config_from_file

loading.start()
 
while True:
    print("""
          
 █████  █████             ███  ██████   ██████  ███  █████              
░░███  ░░███             ░░░  ░░██████ ██████  ░░░  ░░███               
 ░███   ░███  ████████   ████  ░███░█████░███  ████  ░███ █████  ██████ 
 ░███   ░███ ░░███░░███ ░░███  ░███░░███ ░███ ░░███  ░███░░███  ███░░███
 ░███   ░███  ░███ ░███  ░███  ░███ ░░░  ░███  ░███  ░██████░  ░███ ░███
 ░███   ░███  ░███ ░███  ░███  ░███      ░███  ░███  ░███░░███ ░███ ░███
 ░░████████   ████ █████ █████ █████     █████ █████ ████ █████░░██████ 
  ░░░░░░░░   ░░░░ ░░░░░ ░░░░░ ░░░░░     ░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░░  V0.7
                                
          """)
    print("Now UniMiko have features:")
    print("1. Test connection")
    print("2. Add vlan")
    print("3. Remove vlan")
    print("4. Backup configuretion")
    print("5. Send configure from .txt file")
    print("\n99. Exit\n")
    
    while True:
        try:
            Input = int(input("Do you want to [number]: "))
            if Input in range(1,6):
                break
            elif Input == 99:
                break
            else:
                print("Service unavailable")
                continue
        except:
            print("% Please enter number only %")
    if Input == 1:
        ssh_connection_test.status()
    elif Input == 2:
        vlan.add()
    elif Input == 3:
        vlan.remove()
    elif Input == 4:
        Backupv2.start()
    elif Input == 5:
        send_config_from_file.start()
    elif Input == 99:
        exit()
