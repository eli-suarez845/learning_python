import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass  # syntax requires to have something written there
# this wat todos.txt file is created, for the 1st use

# # (image_source="add.png")
sg.theme("DarkPurple1")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button(size=2, image_source="add.png",
                       tooltip="Add to do", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[25, 10])  # (int, int) 25 characters,10 lines
edit_button = sg.Button("Edit")
complete_button = sg.Button(size=4, image_source="complete.png", key="Complete", tooltip="Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 12))
# this is a type of instance, layout is an argument and expects a list but
# [[]] is a list of object instances, buttons, text boxes, etc. Each is a row
while True:
    event, values = window.read(timeout=200)  # update after 10 milliseconds
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todo'].update(value=values['todos'])
            # poit to box instance amd to methods update
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]  # get todo existent by user
                # [0] give us the string
                new_todo = values['todo']  # from user

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)  # get the index of selected todo
                todos[index] = new_todo  # new_todo replaces the selected one
                functions.write_todos(todos)  # this modifies the todos.txt list
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 12))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)  # this update list box
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 12))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()

# If buttons aren't aligned it's because there have the same length.
# So we can use Columns:
#   col1 = sg.Column([[label1], [label2]])
#   col2 = sg.Column([[input1], [input2]])
#   col3 = sg.Column([[choose_button1], [choose_button2]])
