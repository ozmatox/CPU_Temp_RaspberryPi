#!/usr/bin/python
#!/bin/sh
 #!/bin/bash

import time
import os

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219

#serial = spi(port=0, device=0, gpio=noop())
#device = max7219(serial)
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)

virtual = viewport(device, width=300, height=10)
def getCPUtemperature():
        res = os.popen("vcgencmd measure_temp").readline()
        return(res.replace("temp=","").replace("'C\n",""))




with canvas(virtual) as draw:

    draw.text((0, 0), ">>> RPI TEMP: " + getCPUtemperature() + "C", fill="white")

for offset in range(120):
    virtual.set_position((offset, 2))
    time.sleep(0.1)
