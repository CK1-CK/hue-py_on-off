# -*- coding: utf-8 -*-
 
import requests

ip_adresse='192.168.0.100' #HUE Bridge IP-Adresse
hue_user='XXXXXXXXXXXXXXXXXX' #Hue Benutzerschlüssel

light = 'http://'+ip_adresse+'/api/'+hue_user+'/lights/1/state'

r = requests.get(light)


#put_string='{"on":false}' #Lampe ausschalten
put_string='{"on":true}' #Lampe einschalten

r = requests.put(light, put_string)
