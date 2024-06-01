
# boot.py

This file contains the initialization code that runs when the device boots up. It sets up the environment for the main application.

## Example Code
```python
# boot.py
import machine
import network

def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('your-ssid', 'your-password')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

# Call the connect function
connect_wifi()
```
