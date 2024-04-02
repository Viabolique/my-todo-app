import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Планировщик дел")
st.subheader("Это планировщик дел Алексея!")
st.write("Это приложение увеличит твою продуктивность, Евгений!")
st.write("Не тормози скорее дело впиши!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)  # writes updated todolist without removed
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Сюда пиши, Женя...",
              on_change=add_todo, key="new_todo")

print("Hello")

# st.session_state - shows  list in curly brackets underneath
