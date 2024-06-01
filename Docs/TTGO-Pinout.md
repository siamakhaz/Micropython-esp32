# TTGO T-Display ESP32 1.14 Inch Module Pinout

This document provides a detailed description of the pinout for the TTGO T-Display ESP32 1.14 Inch module, along with an annotated image for reference.

![TTGO T-Display ESP32 1.14 Inch Module Pinout](https://github.com/Xinyuan-LilyGO/TTGO-T-Display/blob/master/image/pinmap.jpg?raw=true)

### Pin Descriptions

#### Left Side of the Display:
- **3V3**: 3.3V power
- **GND**: Ground
- **21**: GPIO21 (Wire_SDA)
- **22**: GPIO22 (Wire_SCL)
- **17**: GPIO17
- **2**: GPIO2 (TOUCH2, ADC12)
- **15**: GPIO15 (TOUCH3, ADC13)
- **13**: GPIO13 (TOUCH4, ADC14)
- **12**: GPIO12 (TOUCH5, ADC15)
- **GND**: Ground
- **GND**: Ground
- **3V3**: 3.3V power

#### Right Side of the Display:
- **3V3**: 3.3V power
- **5V**: 5V power
- **37**: GPIO37
- **38**: GPIO38
- **39**: GPIO39 (ADC3)
- **32**: GPIO32 (TOUCH9, ADC4)
- **33**: GPIO33 (TOUCH8, ADC5)
- **25**: GPIO25 (DAC1, ADC18)
- **26**: GPIO26 (DAC2, ADC19)
- **27**: GPIO27 (TOUCH7, ADC17)
- **GND**: Ground
- **5V**: 5V power

#### Display Connections:
- **MOSI**: GPIO19
- **SCLK**: GPIO18
- **CS**: GPIO5
- **DC**: GPIO16
- **RST**: GPIO23
- **BL**: GPIO4 (Backlight)

#### Other Components:
- **Button 1 (GPIO0)**
- **Button 2 (GPIO35)**

### Key Pin Functions:
- **SPI Pins**: Used for communication with the display
  - **MOSI**: GPIO19
  - **SCLK**: GPIO18
  - **CS**: GPIO5
  - **DC**: GPIO16
  - **RST**: GPIO23
  - **BL**: GPIO4 (used to control the backlight)

- **Touch Pins**: These GPIO pins are also used as touch inputs.
  - **GPIO2, GPIO12, GPIO13, GPIO15, GPIO32, GPIO33, GPIO27**

- **Analog-to-Digital Converter (ADC) Pins**: These pins can be used to read analog signals.
  - **GPIO2, GPIO12, GPIO13, GPIO15, GPIO25, GPIO26, GPIO27, GPIO32, GPIO33, GPIO39**

- **Digital-to-Analog Converter (DAC) Pins**: Used for analog output.
  - **GPIO25, GPIO26**

- **I2C Pins**: Used for I2C communication.
  - **SDA (GPIO21)**
  - **SCL (GPIO22)**

This pinout diagram provides a clear overview of the available pins and their functionalities on the TTGO T-Display ESP32 1.14 Inch module, making it easier to understand how to interface with various peripherals and sensors.

### References
For more detailed information and technical support, you can refer to the [official LilyGO GitHub repository](https://github.com/Xinyuan-LilyGO/TTGO-T-Display).

