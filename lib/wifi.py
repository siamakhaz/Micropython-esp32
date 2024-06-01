import network
import utime

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.disconnect()
    
    wlan.connect(ssid, password)
    
    for _ in range(20):
        if wlan.isconnected():
            break
        utime.sleep(1)
    
    if wlan.isconnected():
        print('Connected to', ssid)
        print('IP Address:', wlan.ifconfig()[0])
        return wlan.ifconfig()[0]  # Return the IP address
    else:
        print('Failed to connect to', ssid)
        return None
