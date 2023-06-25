# Create a desktop GUI program that gets feet and inches from the user
# and outputs the results in meters.

import PySimpleGUI as sg
from converters import convert

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, output_label]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")


window.close()