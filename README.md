# UniMiko
Tools for network Engineer by using Netmiko 
<br />
This project was developed to help engineer configure and backup multiple network devices in onces.

## API Document
- [Netmiko](https://ktbyers.github.io/netmiko/docs/netmiko/index.html#netmiko.BaseConnection.send_config_from_file)
- [Tkinter](https://docs.python.org/3/library/tk.html)
- [getpass](https://docs.python.org/3/library/getpass.html)

## Using Netmiko to work with Cisco network device
- Add/remove VLANs
- Get show results and write backup files
- Send configuretion from .txt file

## Examples

### Main Menu
```
Loading…: 100%|██████████████████████████| 101/101 [00:01<00:00, 95.89it/s]

#################################################
-------------------------------------------------
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!       Welcone to UniMiko     !!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-------------------------------------------------
################################### Pratinporn ##

Now UniMiko have features:
1. Test SSH connection
2. Add vlan
3. Remove vlan
4. Backup configuretion
5. Send configure from .txt file

99. Exit
   ```

### Option 1, Test SSH connection
```
Do you want to [number]: 1
Select target devices in .txt file (IP address list):
Selected file: D:/UniMiko/IP_address_list_example.txt
Username: admin
Password:
Enable password:

----------192.168.159.100---------
TEST# is ready

----------192.168.159.101---------
SW-1# is ready

----------192.168.159.102---------
SW-2# is ready
```
### Option 2, Add vlan
```
Do you want to [number]: 2
How many VLANs add: 3
vlan 51
  name Admin
vlan 52
  name Sale
vlan 53
  name Engineer
Select target devices in .txt file (IP address list):
Selected file: D:/UniMiko/IP_address_list_example.txt

--- Vlan summary ---
51 : Admin
52 : Sale
53 : Engineer

--- List of target device ---
192.168.159.100
192.168.159.101
192.168.159.102
192.168.159.103

Please check information above before post configure
Post configure[y/n](n): y
Username: admin
Password:
Enable password:

----------TEST#---------

----------192.168.159.100---------

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi1/0, Gi1/1, Gi1/2, Gi1/3
51   Admin                            active
52   Sale                             active
53   Engineer                         active
1002 fddi-default                     act/unsup
1003 token-ring-default               act/unsup
1004 fddinet-default                  act/unsup
1005 trnet-default                    act/unsup
    ...
```
### Option 3, Remove vlan
```
Do you want to [number]: 3
How many VLANs remove: 3
no vlan 51
no vlan 52
no vlan 53
Select target devices in .txt file (IP address list):
Selected file: D:/UniMiko/IP_address_list_example.txt

--- Vlan summary ---
no vlan 51
no vlan 52
no vlan 53

--- List of target device ---
192.168.159.100
192.168.159.101
192.168.159.102
192.168.159.103

Please check information above before post configure
Post configure[y/n](n): y
Username: admin
Password:
Enable password:

----------TEST#---------

----------192.168.159.100---------

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi1/0, Gi1/1, Gi1/2, Gi1/3
1002 fddi-default                     act/unsup
1003 token-ring-default               act/unsup
1004 fddinet-default                  act/unsup
1005 trnet-default                    act/unsup
    ...
```
### Option 4, Backup configuretion
```
Do you want to [number]: 4
Select target devices in .txt file (IP address list):
Selected file: D:/UniMiko/IP_address_list_example.txt
Username: admin
Password:
Enable password:

--- List of target device ---
192.168.159.100
192.168.159.101
192.168.159.102
192.168.159.103

Choose configurtion file (.txt):
Selected file: D:/UniMiko/config/Show template.txt

Content inside your file:
show clock
show version
show inventory
show run
show switch
show ip int bri
show int status
show int des
show cdp nei
show cdp nei detail
show ether sum
show spanning-tree summary
show arp
show mac address-table
show logging
show int description

Please check information above before start backup
Start backup [y/n](n): y

TEST : 192.168.159.100
Backup success!!

SW-1 : 192.168.159.101
Backup success!!

SW-2 : 192.168.159.102
Backup success!!

SW-3 : 192.168.159.103
Backup success!!
```
- Create files and write results from show template
### Option 5, Send configure from .txt file
```
Do you want to [number]: 5
Select target devices in .txt file (IP address list):
Selected file: D:/UniMiko/IP_address_list_example.txt
Username: admin
Password:
Enable password:

--- List of target device ---
192.168.159.100
192.168.159.101
192.168.159.102
192.168.159.103

Choose configurtion file (.txt):
Selected file: D:/UniMiko/config/Sample config.txt

Config inside your file:
interface loopback 99
        ip add 9.9.9.9 255.255.255.255
        no shut
        exit
vl 99
        name TEST-VLAN
        exit
line vty 0 4
        transport input ssh telnet
        end

Post configure[y/n](n): y

TEST : 192.168.159.100
Yeah!!

SW-1 : 192.168.159.101
Yeah!!

SW-2 : 192.168.159.102
Yeah!!

SW-3 : 192.168.159.103
Yeah!!
```
- Send configuretion and save automatically
