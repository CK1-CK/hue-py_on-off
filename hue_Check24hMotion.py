# -*- coding: utf-8 -*-

from hue_motion import GetLastMotionDateTime
import time
from datetime import datetime,tzinfo,timezone
import email_send



def Check24hMotion(seconds=24*3600):
    tz_info = GetLastMotionDateTime().tzinfo
    #print(tz_info)

    diff = datetime.now(tz_info)-GetLastMotionDateTime()

    print("Letzte Bewegung vor: " + str(diff))


    if(diff.total_seconds() >= seconds):
        #try:
            email_send.SendEmail("kreissc1@gmail.com","Keine Bewegung - Wohnung","Es gab keine Bewegung seit: <br><br>Tagen: "+str(round(diff.total_seconds()/3600/24,4))+"<br><br>Stunden: " + str(round(diff.total_seconds()/3600,4)) +"<br><br>Minuten: "+str(round(diff.total_seconds()/60,2)))
            print("Email versandt")
            return 0
        #except:
        #    return -1
    else:
        return 0



Check24hMotion() #Default-Parameter is 24h
