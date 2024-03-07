import os
os.environ['PYUSB_DEBUG'] = 'debug'

import libusb_package

for dev in libusb_package.find(find_all=True):
    print(dev)
    
import usb.core
usb.core.find()