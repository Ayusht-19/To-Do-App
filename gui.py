import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label],[input_box,add_button]],
                   font=('Times New Roman',14))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todo = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todo.append(new_todo)
            functions.write_todos(todo)
        case sg.WIN_CLOSED:
            break

window.close()