from functions import get_todos,write_todos
import time

now = time.strftime("%b %d , %Y, %H:%M:%S")
print("It is ", now)
""" 
get_todos and write_todos are imported from other script 
named as 'functions'
"""

while True:
    user_action = input("Type add, show , edit , complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

     #new_todos = [item.strip('\n') for item in todos]  list comprehension

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}){item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter the new iteam : ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[8:])

            todos = get_todos()
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            print(number)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("No item with that number")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Enter Valid command.")

print("Bye")




