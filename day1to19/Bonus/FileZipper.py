import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key = "output", text_color="yellow")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                             [label2, input2, choose_button2],
                             [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)  # filepath is value, folder is dest_dir
    # Compress: is the event,
    # key is {0:, Value is:'C:/Users/Elisa/Pictures/Lexica/A grey...jpg;
    # key is Choose, value is:'C:/Users/Elisa/Pictures/Lexica/A grey cat...jpg
    window["output"].update(value="Compression completed!")

window.close()