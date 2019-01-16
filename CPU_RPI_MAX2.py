#!/usr/bin/python
#>>>>ozmatox<<<<<

import os
import time

from random import randrange
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)

def getCPUtemperature():
        res = os.popen("vcgencmd measure_temp").readline()
        return(res.replace("temp=","").replace("'C\n",""))

msg="Temperatura Procesora Raspberry Pi 3  : " + getCPUtemperature() + "C"

while True:
    show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT))
    print(msg)
