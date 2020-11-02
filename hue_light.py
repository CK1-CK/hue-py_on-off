# -*- coding: utf-8 -*-

#python -m pip install requests #Install Request Lib
#pip install discoverhue #Install discoverhue Lib

import requests
import json
import discoverhue

http_adress='http://192.168.0.164/' #HUE Bridge IP-Adress incl. http
hue_user='abc'  #Hue Benutzerschlüssel
light_id=1

auto_detect_bridge=False

try:
    if bool(auto_detect_bridge):
        found = discoverhue.find_bridges()
        for bridge in found:
            print('Bridge ID {br} at {ip}'.format(br=bridge, ip=found[bridge]))
            http_adress=found[bridge]
except:
    print("Keine Bridge gefunden!")

light = http_adress+'api/'+hue_user+'/lights/'+str(light_id)

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