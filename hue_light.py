# -*- coding: utf-8 -*-

#python -m pip install requests #Install Request Lib
#pip install discoverhue #Install discoverhue Lib

import requests
import json
import hue_getBridgeHttpAddress
import hue_userKey


light_id=1
hue_user= hue_userKey.GetHueUserKey()  #Hue Benutzerschlüssel

http_address=hue_getBridgeHttpAddress.GetBridgeHttpAddress()

light = http_address+'api/'+hue_user+'/lights/'+str(light_id)

try:
    r = requests.get(light)

    #print(str(r.json()["state"]["on"])) #Status der Lampe auslesen

    if str(r.json()["state"]["on"]) == 'False':
        put_dict='{"on": true}' #Lampe einschalten
    else:
        put_dict='{"on": false}' #Lampe ausschalten

    r = requests.put(light+'/state', put_dict)
    
except:
    print("Error-Verbindungsaufbau")