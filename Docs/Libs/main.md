
# main.py

This is the main entry point of the MicroPython program. It contains the primary application logic that is executed after the initialization code in `boot.py`.

## Example Code
```python
# main.py
import time
from lib import lcd
from lib import st7789_simple
from lib import webserver
from lib import wifi

# Initialize LCD
lcd.lcd_init()

# Connect to WiFi
wifi.connect_wifi('your_ssid', 'your_password')

# Start the web server
webserver.start_webserver()

while True:
    # Display some text on the LCD
    lcd.lcd_display_text("Hello, TTGO!")
    time.sleep(5)
    # Clear the display
    st7789_simple.st7789_init()
    time.sleep(5)
```
