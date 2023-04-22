FILEPATH = "todo.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do item."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH,):
    """ Write a to-do item list in the text file."""
    with open('todo.txt', 'w') as local_file_two:
        local_file_two.writelines(todos_arg)



if __name__ == "__main__":
    print("Welcome to To-do app")
