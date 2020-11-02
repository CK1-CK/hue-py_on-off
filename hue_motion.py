# -*- coding: utf-8 -*-

#python -m pip install requests #Install Request Lib
#pip install discoverhue #Install discoverhue Lib

import requests
import json
import hue_getBridgeHttpAddress
import hue_userKey


motion_sensor_id=15

hue_user=hue_userKey.GetHueUserKey()  #Hue Benutzerschlüssel

http_address=hue_getBridgeHttpAddress.GetBridgeHttpAddress()

sensor = http_address+'api/'+hue_user+'/sensors/'+str(motion_sensor_id)

try:
    r = requests.get(sensor)
    print(str(r.json()["state"]["presence"])) #Aktuell Bewegung?
    print(str(r.json()["state"]["lastupdated"])) #Letzte Bewegung auslesen
    
except:
    print("Error-Verbindungsaufbau")