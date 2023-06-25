import PySimpleGUI as sg


def convert(fluid_ounce, millimiters):
    result = fluid_ounce * 1 * 29.57353
    return result


fluid_ounce_label = sg.Text("Enter fluid ounce: ")
fluid_ounce_input = sg.Input(key="foo")

millimiters_label = sg.Text("Enter millimiters: ")
millimiters_input = sg.Input(key="mm")

button = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window("Convertor",
                   layout=[[fluid_ounce_label, fluid_ounce_input],
                           [millimiters_label, millimiters_input],
                           [button, output_label]])
