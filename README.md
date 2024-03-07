# Syringe-Pump-GUI
A user-friendly Python GUI and related code to control Nanotec LSA421S14-A-UKGI-152 linear actuators via USB, for the purposes of controlling the flow rate from a syringe mounted along the actuator axis.

## Installation Instructions for Windows Machines
1. Verify that your Python version is >3.7, otherwise the GUI won't work.

2. Ensure that all necessary Python modules (PySimpleGUI, ticlib, etc.) have been pip-installed.

3. pip install pyusb

4. pip install libusb

5. libusb-1.0.dll should be automatically added to wherever your Python installation's site-packages folder is located, something like "C:\Users\Public\AppData\Roaming\Python\site-packages\libusb\_platform\_windows\x64" and "C:\Users\Public\AppData\Roaming\Python\site-packages\libusb\_platform\_windows\x86".

6. Find these two paths, and add them to the Windows PATH variable (System Properties->Advanced->Environment Variables...->Path->Edit...)

7. If for some reason this doesn't work, download and install the latest libusb Windows binary from [https://libusb.info](https://libusb.info/) if not already present.