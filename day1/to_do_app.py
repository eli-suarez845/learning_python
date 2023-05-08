# user_prompt = "Enter a to do:"  # user_prompt is a variable

# while 2 > 1:  # mientras 2 sea mayor que 1, repite input
# todo = input(user_prompt)
# print(todo)
# print("Next...")

# todos = [] # empty list

# while True:
# todo = input(user_prompt) # input is a function
# todos.append(todo) # method are attached to data types to other objects
# print(todos)

# Enter a to do: make cake
# [' make cake']
# Enter a to do:fold clothes
# [' make cake', 'fold clothes']
# Enter a to do:

#     todo.append()
# AttributeError: 'str' object has no attribute 'append'
# It doesn´t make sense to append something to a string! It makes sense to append something to a list, like todos = []

def get_todos(filepath="todos.txt"):  # green is default parameter
    """ Read a text ffile and return the list
    of to_do items.
    """  # this is a doc-string
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local  # this function returns something


def write_todos(todos_arg, filepath="todos.txt"):  # this function is like a procedure, it doesn´t return anything
    """ Write the to_do items list in the text file."""
    with open(filepath, 'w') as file:  # open method calls files, w is write
        file.writelines(todos_arg)  # the argument's method is a list


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()  # for removing the space in "add "

    if user_action.startswith('add'):
        todo = user_action[4:]  # slicing from index 4 and go on, c in clean is index 4

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)


    elif user_action.startswith('show'):  # elif do not check the other options if add is True

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"  # f-strings are something that contains the {} where you enter a variable
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])  # convert a string in a number
            number = number - 1  # index starts at zero but user don't know that

            todos = get_todos()
            print("Here are the existing todos:", todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'  # to access items from a list

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"To do {todos_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:  # if none of options are True
        print("Command is not valid")

print("Bye!")

#  Match-case is usually to match a string out of a predefined number of strings (e.g., a series of commands, months of the year, etc.)

# What is the difference between a while loop and a for-loop?
# A while loop iterates as long as the while-condition is True.
# A for-loop iterates that many times as there are items in the list that is being iterated.
# if, elif, else, or, not are Boolean operators
