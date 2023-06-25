import PySimpleGUI

import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[25, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 12))
# this is a type of instance, layout is an argument and expects a list but
# [[]] is a list of object instances, buttons, text boxes, etc. Each is a row
while True:
    event, values = window.read()
    print(1, event)  # todos
    print(2, values)  # dic
    print(3, values['todos'])  # list of that part
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todo'].update(value=values['todos'])
            # poit to box instance amd to methods update
        case "Edit":
            todo_to_edit = values["todos"][0]  # get todo existent by user
            # [0] give us the string
            new_todo = values['todo']  # from user

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)  # get the index of selected todo
            todos[index] = new_todo  # new_todo replaces the selected one
            functions.write_todos(todos)  # this modifies the todos.txt list
            window['todos'].update(values=todos)
        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(value=values["todos"][0])  # this update list box
            window["todo"].update(value="")
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
# imprime info sobre el evento: ('Add', {'todo': 'algo'})
