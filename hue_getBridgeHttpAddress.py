# -*- coding: utf-8 -*-

#pip install validators

import discoverhue
import validators

http_address='http://192.168.0.164/' #HUE Bridge IP-Adress incl. http

def GetBridgeHttpAddress():
    global http_address
    try:
        if validators.url(http_address):
            return http_address
        else:
            found = discoverhue.find_bridges()
            for bridge in found:
                print('Bridge ID {br} at {ip}'.format(br=bridge, ip=found[bridge]))
                http_address=found[bridge]
                return http_address #Return the first found Bridge
    except:
        print("Keine Bridge gefunden!")
        return -1


if __name__ == '__main__':
    GetBridgeHttpAddress()