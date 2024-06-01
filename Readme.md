### Documentation

## Overview

This project is designed for the TTGO T-Display ESP32 1.14 Inch Module and runs on MicroPython firmware. It includes several Python files and libraries to manage the display, WiFi connectivity, and web server functionality.

### Files and Libraries

#### 1. `boot.py`
This file contains the initialization code that runs when the device boots up. It sets up the environment for the main application.

#### 2. `main.py`
This is the main entry point of the MicroPython program. It contains the primary application logic that is executed after the initialization code in `boot.py`.

#### Libraries in the `lib` Directory

##### `lib/lcd.py`
This library handles the interaction with the LCD display. It includes functions and classes to initialize the display, draw graphics, and manage the screen.

**Example Functions:**
- `lcd_init()`: Initializes the LCD display.
- `lcd_display_text(text)`: Displays text on the LCD.

##### `lib/st7789_simple.py`
This library provides a simplified interface for the ST7789 display driver used in the TTGO T-Display. It includes methods for basic display operations.

**Example Functions:**
- `st7789_init()`: Initializes the ST7789 display.
- `st7789_draw_pixel(x, y, color)`: Draws a pixel at the specified coordinates with the given color.

##### `lib/webserver.py`
This library sets up a web server on the ESP32. It includes functions to handle HTTP requests, serve web pages, and respond to API calls.

**Example Functions:**
- `start_webserver()`: Starts the web server.
- `handle_request(request)`: Handles incoming HTTP requests.

##### `lib/wifi.py`
This library manages WiFi connectivity. It includes functions to connect to a WiFi network, handle disconnections, and retrieve network information.

**Example Functions:**
- `connect_wifi(ssid, password)`: Connects to a WiFi network with the given SSID and password.
- `disconnect_wifi()`: Disconnects from the current WiFi network.

### Example Usage

Here’s an example of how you might use these libraries in your `main.py`:

```python
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

### References

- [MicroPython official website](https://micropython.org/)
- [MicroPython documentation for ESP32](https://docs.micropython.org/en/latest/esp32/quickref.html)
- [TTGO T-Display GitHub repository](https://github.com/Xinyuan-LilyGO/TTGO-T-Display)
- Original tutorial: [Random Nerd Tutorials](https://randomnerdtutorials.com/micropython-esp32-esp8266-vs-code-pymakr/#pymakr)
