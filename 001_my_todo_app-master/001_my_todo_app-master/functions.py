FILEPATH = "todos.txt"  # it´s a convention that says XXX is a constant


def get_todos(filepath=FILEPATH):  # green is default parameter
    """ Read a text file and return the list
    of to_do items.
    """  # this is a doc-string
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local  # this function returns something


def write_todos(todos_arg, filepath=FILEPATH):  # this function is like a procedure, it doesn´t return anything
    """ Write the to_do items list in the text file."""
    with open(filepath, 'w') as file:  # open method calls files, w is write
        file.writelines(todos_arg)  # the argument's method is a list


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
