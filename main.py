from pump import Pump
import PySimpleGUI as sg
from GUI import Windows as w

#-------------modify with info of your pump
motor_serial_number = '00352818' 
motor_model = {
    motor_serial_number: 'T825',
}[motor_serial_number]
#-------------


# calculates pushing speed of pump with given flowspeed in mm/s
# input in mm and mm/s
def flowspeedToPushspeed(D_syringe, D_tube,flowspeed):
    return flowspeed*((D_tube/D_syringe)**2)

flowspeed, D_tube, D_syringe,pumpSpeed = 0,0,0,0
pump = Pump(motor_model, serial_no=motor_serial_number)


# drawing interface
# sg.theme('Reddit')
sg.theme('LightBlue5')
window = w.mainScreen(flowspeed, D_tube, D_syringe,pumpSpeed, "")
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        pump.stop()
        break

    if event == 'Submit':
        # Check if user filled in all fields
        if values[0] == '0' or values[1] == '0' or values[2] == '0' or values[0] == '' or values[1] == '' or values[2] == '':
            warning = "Fill in fields with valid values"
            window.close()
            window = w.mainScreen(flowspeed, D_tube, D_syringe, pumpSpeed, warning)

        # Collect data from fields
        else:
            flowspeed = float(values[0]) 
            D_tube = float(values[1])
            D_syringe = float(values[2])
            pumpSpeed = flowspeedToPushspeed(D_syringe, D_tube,flowspeed)

            window.close()
            window = w.mainScreen(flowspeed, D_tube, D_syringe, pumpSpeed,"")

    # Stop pump
    elif event == 'stop' or event==" ":
        pump.stop()
        window.close()
        window = w.mainScreen(flowspeed, D_tube, D_syringe, pumpSpeed,"")

    # Bring bump back up
    elif event == 'reverse':
        pump.enable_motor()
        pump.move_with_speed(10)
        window.close()
        window = w.pumpRunningScreen(flowspeed, D_tube, D_syringe, pumpSpeed,"")
        
    # Start pump
    elif event == 'start':

        # Check for zero values
        if flowspeed ==0 or  D_tube==0 or  D_syringe== 0:
            window.close()
            window = w.mainScreen(flowspeed, D_tube, D_syringe, pumpSpeed, "Fill in fields with valid values")

        # Move pump
        else:
            if pump.move_with_speed(-1*pumpSpeed) == False:
                window.close()
                window = w.mainScreen(flowspeed, D_tube, D_syringe, pumpSpeed,"Requested pumpspeed too high")
            else: 
                pump.enable_motor()
                pump.move_with_speed(-1*pumpSpeed)
                window.close()
                window = w.pumpRunningScreen(flowspeed, D_tube, D_syringe,pumpSpeed,"")

window.close()