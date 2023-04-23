user_prompt = "Enter a to do:"  # user_prompt is a variable

#while 2 > 1:  # mientras 2 sea mayor que 1, repite input
    #todo = input(user_prompt)
    #print(todo)
    #print("Next...")

todos = [] # empty list

while True:
    todo = input(user_prompt) # input is a function
    todos.append(todo) # method are attached to data types to other objects
    print(todos)

# Enter a to do: make cake
# [' make cake']
# Enter a to do:fold clothes
# [' make cake', 'fold clothes']
# Enter a to do:

#     todo.append()
# AttributeError: 'str' object has no attribute 'append'
# It doesn´t make sense to append something to a string! It makes sense to append something to a list, like todos = []

