# import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
# this is a type of instance, layout is an argument and expects a list but
# [[]] is a list of object instances, buttons, text boxes, etc. Each is a row
window.read()
window.close()