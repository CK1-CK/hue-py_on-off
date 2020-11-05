# -*- coding: utf-8 -*-

#python -m pip install requests #Install Request Lib
#pip install discoverhue #Install discoverhue Lib

import requests
import json
import hue_getBridgeHttpAddress
import hue_userKey
import re
from datetime import datetime,tzinfo,timezone


motion_sensor_id=15

hue_user=hue_userKey.GetHueUserKey()  #Hue Benutzerschlüssel
http_address=hue_getBridgeHttpAddress.GetBridgeHttpAddress()

sensor = http_address+'api/'+hue_user+'/sensors/'+str(motion_sensor_id)


def GetLastMotionDateTime():
    try:
        r = requests.get(sensor)
    except:
        print("Error-Verbindungsaufbau")
        return -1

    try:
        #print(str(r.json()["state"]["presence"])) #Aktuell Bewegung?
        #print(str(r.json()["state"]["lastupdated"])) #Letzte Bewegung auslesen UTC

        m = re.search('(\\d\\d\\d\\d)-(\\d\\d)-(\\d\\d)T(\\d\\d):(\\d\\d):(\\d\\d)', str(r.json()["state"]["lastupdated"]))

        #print(m.group(1)) #Jahr
        #print(m.group(2)) #Monat
        #print(m.group(3)) #Tag
        #print(m.group(4)) #Stunde
        #print(m.group(5)) #Minute
        #print(m.group(6)) #Sekunde

        last_motion_utc=datetime(int(m.group(1)),int(m.group(2)),int(m.group(3)),int(m.group(4)),int(m.group(5)),int(m.group(6)))
        last_motion_localTime=last_motion_utc.replace(tzinfo=timezone.utc).astimezone(tz=None)

        #print(last_motion_utc) #Letzte Bewegung UTC
        #print(last_motion_localTime) #Letzte Bewegung Local Time
        return last_motion_localTime

    except:
        print("Error")
        return -1

GetLastMotionDateTime()
