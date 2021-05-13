from netmiko import ConnectHandler

username = "admin"
password = "cisco"

device = "10.0.15.106"
device_para = {'device_type': 'cisco_ios',
            'ip': device,
            'username': username,
            'password': password
            }
with ConnectHandler(**device_para) as ssh:
    print("Configuring %s..."%device)
    ssh.send_config_from_file('config_router.txt')
    ssh.save_config()
