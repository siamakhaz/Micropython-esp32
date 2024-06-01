from machine import Pin, SPI
import st7789_simple as st7789_simple

def init_lcd():
    # Initialize SPI for TTGO
    spi = SPI(1, baudrate=26700000, polarity=1, phase=1, sck=Pin(18), mosi=Pin(19), miso=Pin(25))
    display = st7789_simple.ST7789(
        spi, 190, 280,  # Width and height of the display
        reset=Pin(23, Pin.OUT),
        dc=Pin(16, Pin.OUT),
        cs=Pin(5, Pin.OUT),
        backlight=Pin(4, Pin.OUT),
        rotation=0
    )

    # Initialize the display
    display.init()

    # Set the backlight on
    display.backlight.value(1)
    display.fill(display.color565(0, 0, 0))

    return display

def display_text(display, text, x, y, color):
    display.text(text, x, y, color)
