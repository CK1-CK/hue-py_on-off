# -*- coding: utf-8 -*-

#python -m pip install requests #Install Request Lib
#pip install discoverhue #Install discoverhue Lib

import requests
import json
import discoverhue

http_adress='http://192.168.0.164/' #HUE Bridge IP-Adress incl. http
hue_user='abc'  #Hue Benutzerschlüssel
motion_sensor_id=15

auto_detect_bridge=False

try:
    if bool(auto_detect_bridge):
        found = discoverhue.find_bridges()
        for bridge in found:
            print('Bridge ID {br} at {ip}'.format(br=bridge, ip=found[bridge]))
            http_adress=found[bridge]
except:
    print("Keine Bridge gefunden!")

sensor = http_adress+'api/'+hue_user+'/sensors/'+str(motion_sensor_id)

try:
    r = requests.get(sensor)
    print(str(r.json()["state"]["presence"])) #Aktuell Bewegung?
    print(str(r.json()["state"]["lastupdated"])) #Letzte Bewegung auslesen
    
except:
    print("Error-Verbindungsaufbau")