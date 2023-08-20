# UniMiko
Network Engineer tools by using Netmiko 
<br />
This project was developed to help engineer doing repeatly task in a few step.
<br />
I hope this program will be help and useful  
<br />
## Examples
<img src="pics/1.png" width="500">
<br />

- This is sample menu there have 5 functoins

<img src="pics/2.png" width="500">
<br />

- You can put group or single IP address into program by .txt file via [Tkinter dialogs](https://docs.python.org/3/library/dialog.html).
- Passwrod is hidden by using [getpass()](https://docs.python.org/3/library/getpass.html).
 
<img src="pics/3.png" width="500">

- In option 4 backup configuretion, you can choose your own show template via .txt file
- When backup success, program will write file into program folder location.

<img src="pics/4.png" width="500">

- In option 5 send config, you can choose your own config template via .txt file
- And post them by using [send_config_from_file()](https://ktbyers.github.io/netmiko/docs/netmiko/index.html#netmiko.BaseConnection.send_config_from_file)

## API Document
- [Netmiko](https://ktbyers.github.io/netmiko/docs/netmiko/index.html#netmiko.BaseConnection.send_config_from_file)
- [Tkinter](https://docs.python.org/3/library/tk.html)
- [getpass](https://docs.python.org/3/library/getpass.html)