from netmiko import ConnectHandler

cisco_Switch = {
    "device_type": "cisco_ios",
    "host": "192.168.10.162,
    "username": "admin",
    "password": "cisco",
    "secret": "cisco"}

with ConnectHandler(**cisco_Switch) as net_connect:
    
    net_connect.enable()
    output - net_connect.send_config_from_file('iosv_l3_config.txt')

    print (output)
    net_connect.disconnect()
