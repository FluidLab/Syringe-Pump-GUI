from pump import Pump
import PySimpleGUI as sg
from GUI import WindowsQ as w
import numpy as np
# import tkinter as tk

#-------------modify with info of your pump
motor_serial_number = '00352818' 
motor_model = {
    motor_serial_number: 'T825',
}[motor_serial_number]
#-------------


# calculates pushing speed of pump with given Q in ml/s
# input in mm and ml/s
def QToPushspeed(D_syringe,Qs):
    Qs = Qs * 1000 # converting to mm^3
    pumpSpeed = Qs/((((D_syringe/2)**2)*np.pi))
    # pumpSpeed=9
    return pumpSpeed

Qs, D_syringe,pumpSpeed = 0,0,0
pump = Pump(motor_model, serial_no=motor_serial_number)


# drawing interface
# sg.theme('Reddit')
sg.theme('LightBlue5')
window = w.mainScreen(Qs,  D_syringe,pumpSpeed, "")
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        pump.stop()
        break

    if event == 'Submit':
        # Check if user filled in all fields
        if values[0] == '0' or values[1] == '0'  or values[0] == '' or values[1] == '' :
            warning = "Fill in fields with valid values"
            window.close()
            window = w.mainScreen(Qs,D_syringe, pumpSpeed, warning)

        # Collect data from fields
        else:
            Qs = float(values[0]) 
            D_syringe = float(values[1])
            pumpSpeed = QToPushspeed(D_syringe,Qs)

            window.close()
            window = w.mainScreen(Qs,  D_syringe, pumpSpeed,"")

    # Stop pump
    elif event == 'stop' or event==" ":
        pump.stop()
        window.close()
        window = w.mainScreen(Qs, D_syringe, pumpSpeed,"")

    # Bring bump back up
    elif event == 'reverse':
        pump.enable_motor()
        pump.move_with_speed(10)
        window.close()
        window = w.pumpRunningScreen(Qs, D_syringe,  pumpSpeed,"")
        
    # Start pump
    elif event == 'start':

        # Check for zero values
        if Qs ==0 or  D_syringe==0 :
            window.close()
            window = w.mainScreen(Qs, D_syringe, pumpSpeed, "Fill in fields with valid values")

        # Move pump
        else:
            if pump.move_with_speed(-1*pumpSpeed) == False:
                window.close()
                window = w.mainScreen(Qs, D_syringe, pumpSpeed,"Requested pumpspeed too high")
            else: 
                pump.enable_motor()
                pump.move_with_speed(-1*pumpSpeed)
                window.close()
                window = w.pumpRunningScreen(Qs,  D_syringe,pumpSpeed,"")

window.close()