import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'  # is a specific object type, looks like a dicc
    todos.append(todo)
    functions.write_todos(todos)  # todo update todos.txt


st.title("My Todo App")
st.subheader("This is my first app:")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a new todo",
              on_change=add_todo, key='new_todo')  # on_change is like a custom function

st.session_state
