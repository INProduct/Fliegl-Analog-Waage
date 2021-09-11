import os
import network
import json

'''
There are five values for authmode:

            * 0 -- open
            * 1 -- WEP
            * 2 -- WPA-PSK
            * 3 -- WPA2-PSK
            * 4 -- WPA/WPA2-PSK
'''

try:
    with open('path_config.json', 'r') as file:
        path_config = json.loads(file.read())
except:
    with open('path_config.json', 'w') as file:
        path_config = {
            'log_path': 'var',
            'config_path': 'etc',
            'websrv_path': 'www',
        }
        js = json.dumps(path_config)
        file.write(js)

try:
    with open('wlan_config.json', 'r') as file:
        wlan_config = json.loads(file.read())
except:
    with open('wlan_config.json', 'w') as file:
        wlan_config = {
            'essid': 'INProduct',
            'password': 'INProduct2021',
            'authmode': '3',
        }
        js = json.dumps(wlan_config)
        file.write(js)

# Create directories

for path in path_config.values():
    if path not in os.listdir():
        os.mkdir(path)


# NETWORK
# station disabled
sta_if = network.WLAN(network.STA_IF)
sta_if.active(False)

# access point enabled
ap_if = network.WLAN(network.AP_IF)
ap_if.config(essid=wlan_config['essid'], authmode=int(wlan_config['authmode']), password=wlan_config['password'])
ap_if.active(True)
