import time
import framebuf
from machine import SPI, Pin

# Constants for ST7789
NOP = 0x00
SWRESET = 0x01
RDDID = 0x04
RDDST = 0x09
SLPIN = 0x10
SLPOUT = 0x11
PTLON = 0x12
NORON = 0x13
INVOFF = 0x20
INVON = 0x21
DISPOFF = 0x28
DISPON = 0x29
CASET = 0x2A
RASET = 0x2B
RAMWR = 0x2C
RAMRD = 0x2E
COLMOD = 0x3A
MADCTL = 0x36
FRMCTR1 = 0xB1
DISSET5 = 0xB6
PWCTR1 = 0xC0
PWCTR2 = 0xC1
VMCTR1 = 0xC5
GMCTRP1 = 0xE0
GMCTRN1 = 0xE1

class ST7789:
    def __init__(self, spi, width, height, reset, dc, cs, backlight, rotation=0):
        self.spi = spi
        self.width = width
        self.height = height
        self.reset = reset
        self.dc = dc
        self.cs = cs
        self.backlight = backlight
        self.rotation = rotation

        self.cs.init(self.cs.OUT, value=1)
        self.dc.init(self.dc.OUT, value=0)
        self.reset.init(self.reset.OUT, value=1)
        self.backlight.init(self.backlight.OUT, value=1)

        self.reset.value(1)
        time.sleep_ms(50)
        self.reset.value(0)
        time.sleep_ms(50)
        self.reset.value(1)
        time.sleep_ms(150)

        self.cursor_x = 0
        self.cursor_y = 0
        self.line_height = 8
        self.margin = 2

        self.init()

    def init(self):
        self._write_cmd(SWRESET)
        time.sleep_ms(150)
        self._write_cmd(SLPOUT)
        time.sleep_ms(150)
        self._write_cmd(COLMOD)
        self._write_data(0x55)  # 16-bit color
        time.sleep_ms(10)
        self._write_cmd(MADCTL)
        self._write_data(0x00)
        self._write_cmd(INVON)
        time.sleep_ms(10)
        self._write_cmd(NORON)
        time.sleep_ms(10)
        self._write_cmd(DISPON)
        time.sleep_ms(500)

    def _write_cmd(self, cmd):
        self.cs.value(0)
        self.dc.value(0)
        self.spi.write(bytearray([cmd]))
        self.cs.value(1)

    def _write_data(self, data):
        self.cs.value(0)
        self.dc.value(1)
        self.spi.write(bytearray([data]))
        self.cs.value(1)

    def fill(self, color):
        self._write_cmd(CASET)
        self._write_data(0x00)
        self._write_data(0x00)
        self._write_data((self.width - 1) >> 8)
        self._write_data((self.width - 1) & 0xFF)
        self._write_cmd(RASET)
        self._write_data(0x00)
        self._write_data(0x00)
        self._write_data((self.height - 1) >> 8)
        self._write_data((self.height - 1) & 0xFF)
        self._write_cmd(RAMWR)

        color_hi = color >> 8
        color_lo = color & 0xFF
        chunk_height = 8  # Adjust chunk height to a suitable size to avoid memory errors
        data = bytearray([color_hi, color_lo] * self.width * chunk_height)
        self.cs.value(0)
        self.dc.value(1)
        for y in range(0, self.height, chunk_height):
            self.spi.write(data)
        self.cs.value(1)

    def color565(self, r, g, b):
        return ((r & 0xf8) << 8) | ((g & 0xfc) << 3) | (b >> 3)

    def set_window(self, x0, y0, x1, y1):
        self._write_cmd(CASET)
        self._write_data(x0 >> 8)
        self._write_data(x0 & 0xFF)
        self._write_data(x1 >> 8)
        self._write_data(x1 & 0xFF)

        self._write_cmd(RASET)
        self._write_data(y0 >> 8)
        self._write_data(y0 & 0xFF)
        self._write_data(y1 >> 8)
        self._write_data(y1 & 0xFF)

        self._write_cmd(RAMWR)

    def pixel(self, x, y, color):
        self.set_window(x, y, x, y)
        self._write_data(color >> 8)
        self._write_data(color & 0xFF)

    def text(self, string, x, y, color):
        import framebuf
        width = len(string) * 8
        buf = bytearray(width * 8 // 8)
        fb = framebuf.FrameBuffer(buf, width, 8, framebuf.MONO_HMSB)
        fb.text(string, 0, 0, 1)
        self.blit_buffer(buf, x, y, width, 8, color)

    def blit_buffer(self, buf, x, y, w, h, color):
        color_hi = color >> 8
        color_lo = color & 0xFF
        buf2 = bytearray(w * h * 2)
        for i in range(len(buf)):
            for bit in range(8):
                if buf[i] & (1 << bit):
                    buf2[2 * (i * 8 + bit)] = color_hi
                    buf2[2 * (i * 8 + bit) + 1] = color_lo
        self.set_window(x, y, x + w - 1, y + h - 1)
        self._write_data_buffer(buf2)

    def _write_data_buffer(self, buf):
        self.dc.value(1)
        self.cs.value(0)
        self.spi.write(buf)
        self.cs.value(1)

    def print(self, string, color):
        import framebuf
        for char in string:
            if char == '\n':
                self.cursor_x = 0
                self.cursor_y += self.line_height + self.margin
                if self.cursor_y >= self.height:
                    self.scroll()
                    self.cursor_y -= self.line_height + self.margin
                continue
            width = 8
            buf = bytearray(width * self.line_height // 8)
            fb = framebuf.FrameBuffer(buf, width, self.line_height, framebuf.MONO_HLSB)
            fb.text(char, 0, 0, 1)
            self.blit_buffer(buf, self.cursor_x, self.cursor_y, width, self.line_height, color)
            self.cursor_x += width
            if self.cursor_x >= self.width:
                self.cursor_x = 0
                self.cursor_y += self.line_height + self.margin
                if self.cursor_y >= self.height:
                    self.scroll()
                    self.cursor_y -= self.line_height + self.margin

    def scroll(self):
        # Copy the display content up by one line height
        chunk_height = self.line_height + self.margin
        color_hi = 0
        color_lo = 0
        for y in range(0, self.height - chunk_height, chunk_height):
            self.set_window(0, y, self.width - 1, y + chunk_height - 1)
            buf = bytearray(self.width * chunk_height * 2)
            self.dc.value(0)
            self.cs.value(0)
            self.spi.readinto(buf)
            self.cs.value(1)
            self.set_window(0, y - chunk_height, self.width - 1, y - 1)
            self._write_data_buffer(buf)
        self.set_window(0, self.height - chunk_height, self.width - 1, self.height - 1)
        buf = bytearray(self.width * chunk_height * 2)
        self.dc.value(1)
        self.cs.value(0)
        self.spi.write(buf)
        self.cs.value(1)
