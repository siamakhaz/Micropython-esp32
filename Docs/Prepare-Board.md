# Flashing MicroPython Firmware to ESP32

This guide provides step-by-step instructions on how to flash MicroPython firmware onto an ESP32 using `esptool.py`.

## Requirements

- ESP32 board
- USB cable
- Computer with Python 3.x installed
- MicroPython firmware for ESP32
- `esptool.py` utility

## Steps

### 1. Install Python 3.x

Ensure you have Python 3.x installed on your computer. You can download it from the official [Python website](https://www.python.org/downloads/).

### 2. Install `esptool.py`

Install `esptool.py` using pip. Open your terminal or command prompt and run:

```sh
pip install esptool
```

### 3. Download MicroPython Firmware

Download the latest MicroPython firmware for the ESP32 from the [official MicroPython website for LILYGO TTGO LoRa32](https://micropython.org/download/LILYGO_TTGO_LORA32/). For example, you can use the firmware [LILYGO_TTGO_LORA32-20240222-v1.22.2.bin](https://micropython.org/resources/firmware/LILYGO_TTGO_LORA32-20240222-v1.22.2.bin).

### 4. Connect ESP32 to Your Computer

Use a USB cable to connect the ESP32 board to your computer. Make sure the appropriate drivers are installed. 

### 5. Erase Flash Memory

Before flashing the new firmware, it's recommended to erase the flash memory. Run the following command, replacing `PORT` with the appropriate serial port name (e.g., `COM3` on Windows or `/dev/ttyUSB0` on Linux/Mac):

```sh
esptool.py --port PORT erase_flash
```

### 6. Flash MicroPython Firmware

Flash the downloaded MicroPython firmware to the ESP32. Replace `PORT` with your serial port name and `FIRMWARE` with the path to the downloaded firmware file:

```sh
esptool.py --chip esp32 --port PORT --baud 460800 write_flash -z 0x1000 FIRMWARE
```

### 7. Verify Installation

After flashing, you can verify the installation by connecting to the ESP32 using a serial terminal (like PuTTY or screen). Open the terminal and connect to the appropriate serial port at 115200 baud. You should see the MicroPython prompt (`>>>`).

### Example Commands:

```sh
# Install esptool
pip install esptool

# Erase flash
esptool.py --port COM3 erase_flash

# Flash MicroPython firmware
esptool.py --chip esp32 --port COM3 --baud 460800 write_flash -z 0x1000 LILYGO_TTGO_LORA32-20240222-v1.22.2.bin
```

For more detailed instructions, refer to the original tutorial on [Random Nerd Tutorials](https://randomnerdtutorials.com/flashing-micropython-firmware-esptool-py-esp32-esp8266/).

### References

For additional resources and technical support, visit the [MicroPython official website](https://micropython.org/), the [MicroPython documentation for ESP32](https://docs.micropython.org/en/latest/esp32/quickref.html), and the [Random Nerd Tutorials](https://randomnerdtutorials.com/) blog.
