# Setting Up MicroPython on ESP32 using VS Code and Pymakr

This guide provides detailed instructions on how to set up Visual Studio Code (VS Code) to program your ESP32 and ESP8266 boards using MicroPython with the Pymakr extension.

## Requirements

- ESP32 or ESP8266 board
- USB cable
- Computer with VS Code installed
- Python 3.x installed on your computer
- Node.js installed on your computer
- Pymakr extension for VS Code

## Steps

### 1. Install Visual Studio Code

Download and install [Visual Studio Code](https://code.visualstudio.com/) on your computer.

### 2. Install Python 3.x

Ensure you have Python 3.x installed on your computer. You can download it from the official [Python website](https://www.python.org/downloads/).

### 3. Install Node.js

Download and install [Node.js](https://nodejs.org/) on your computer. This is required for the Pymakr extension to work properly.

### 4. Install Pymakr Extension

1. Open VS Code.
2. Go to the Extensions view by clicking on the square icon in the sidebar or pressing `Ctrl+Shift+X`.
3. Search for "Pymakr" and click "Install".

### 5. Configure Pymakr

After installing the Pymakr extension, you need to configure it to work with your ESP32/ESP8266 board.

1. Connect your ESP32/ESP8266 board to your computer using a USB cable.
2. Open the Command Palette by pressing `Ctrl+Shift+P` and type "Pymakr > Global Settings".
3. Set the "address" to your board's serial port (e.g., `COM3` on Windows or `/dev/ttyUSB0` on Linux/Mac).

### 6. Write and Upload Your First MicroPython Script

1. Create a new file in VS Code with the `.py` extension.
2. Write your MicroPython code. For example:

    ```python
    from machine import Pin
    import time

    led = Pin(2, Pin.OUT)

    while True:
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)
    ```

3. Save the file.
4. Click on the "Upload" button in the bottom bar of VS Code to upload the script to your board.

### 7. Open the Pymakr Terminal

To interact with your board using the REPL (Read-Evaluate-Print Loop), open the Pymakr terminal:

1. Click on the "Pymakr Console" icon in the bottom bar.
2. You should see the MicroPython prompt (`>>>`), indicating that you are connected to the board.

### References

For more detailed instructions and troubleshooting tips, refer to the original tutorial on [Random Nerd Tutorials](https://randomnerdtutorials.com/micropython-esp32-esp8266-vs-code-pymakr/#pymakr).

For additional resources and technical support, visit the [MicroPython official website](https://micropython.org/), and the [MicroPython documentation for ESP32](https://docs.micropython.org/en/latest/esp32/quickref.html).

for the Driver use [CP210x USB to UART Bridge VCP Driver](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads)