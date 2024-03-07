import PySimpleGUI as sg

class Windows:

    def mainScreen(flowspeed, D_tube, D_syringe,speedPump, warning):
        layout = [
        [sg.Text("Change parameters")],
        [sg.Text('Desired flowspeed (f)'),sg.InputText(),sg.Text('mm/s')],
        [sg.Text('Diameter tube (Dt)'),sg.InputText(),sg.Text('mm')],
        [sg.Text('Diameter syringe (Ds)'),sg.InputText(), sg.Text('mm')],
        [sg.Submit(), sg.Text(warning, text_color = 'red')], 
        [sg.Text('f = ' + str(flowspeed) + ' mm/s'), sg.Text('Dt = '+ str(D_tube) + ' mm'), sg.Text('Ds = '+ str(D_syringe) + ' mm')],
        [sg.Text('Calculated speed of pump = '+ str(speedPump) + ' mm/s')],
        [sg.Button("Start pump", key='start'), sg.Button("Reverse", key='reverse')]
        ]
        window = sg.Window("💧 Pumpware 💧", layout, return_keyboard_events=True)
        return window

    def pumpRunningScreen(flowspeed, D_tube, D_syringe,speedPump,warning):
        layout = [
        [sg.Text("Change parameters")],
        [sg.Text('Desired flowspeed (f)'),sg.InputText(),sg.Text('mm/s')],
        [sg.Text('Diameter tube (Dt)'),sg.InputText(),sg.Text('mm')],
        [sg.Text('Diameter syringe (Ds)'),sg.InputText(), sg.Text('mm')],
        [sg.Submit()], 
        [sg.Text('f = ' + str(flowspeed) + ' mm/s'), sg.Text('Dt = '+ str(D_tube) + ' mm'), sg.Text('Ds = '+ str(D_syringe) + ' mm')],
        [sg.Text('Calculated speed of pump = '+ str(speedPump) + ' mm/s')],
        [sg.Text("PRESS SPACEBAR TO STOP", text_color = 'red'),sg.Button("Stop", key='stop',button_color =('white','red'))]
        ]
        window = sg.Window("💧 Pumpware 💧", layout, return_keyboard_events=True)
        return window



class WindowsQ:

    def mainScreen(flowspeed, D_syringe,speedPump, warning):
        layout = [
        [sg.Text("Change parameters")],
        [sg.Text('Volumetric speed (Q)'),sg.InputText(),sg.Text('mL/s')],
        [sg.Text('Diameter syringe (Ds)'),sg.InputText(), sg.Text('mm')],
        [sg.Submit(), sg.Text(warning, text_color = 'red')], 
        [sg.Text('Q = ' + str(flowspeed) + ' mL/s'), sg.Text('Ds = '+ str(D_syringe) + ' mm')],
        [sg.Text('Calculated speed of pump = '+ str(speedPump) + 'mm/s')],
        [sg.Button("Start pump", key='start'), sg.Button("Reverse", key='reverse')]
        ]
        window = sg.Window("💧 Pumpware 💧", layout, return_keyboard_events=True)
        return window

    def pumpRunningScreen(Q, D_syringe,speedPump,warning):
        layout = [
        [sg.Text("Change parameters")],
        [sg.Text('Volumetric speed (Q))'),sg.InputText(),sg.Text('mL/s')],
        [sg.Text('Diameter syringe (Ds)'),sg.InputText(), sg.Text('mm')],
        [sg.Submit()], 
        [sg.Text('Q = ' + str(Q) + ' mL/s'), sg.Text('Ds = '+ str(D_syringe) + ' mm')],
        [sg.Text('Calculated speed of pump = '+ str(speedPump) + ' mm/s')],
        [sg.Text("PRESS SPACEBAR TO STOP", text_color = 'red'),sg.Button("Stop", key='stop',button_color =('white','red'))]
        ]
        window = sg.Window("💧 Pumpware 💧", layout, return_keyboard_events=True)
        return window