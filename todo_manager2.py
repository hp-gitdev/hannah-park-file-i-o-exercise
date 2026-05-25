todo_list = ["Buy groceries", "Finish homework", "Call the dentist"]

print("1.", todo_list[0])
print("2.", todo_list[1])
print("3.", todo_list[2])

total_tasks = len(todo_list)
print(f"\nTotal tasks: {total_tasks}")

add = (input("What task would you like to add onto your to-do list?"))
print(f"Add a task: {add}")
todo_list.append(add)

for i, task in enumerate(todo_list, start = 1):
    print(f"{i}. {task}")


try: 
    delete_task_text = int(input("What number task would you like to remove?"))
    todo_list.pop(delete_task_text - 1)

except ValueError:
    print("Please enter a numeric number. E.g. 2")
    delete_task_text = (input("What number is that?"))

    todo_list.pop(delete_task_text - 1)

except IndexError:
    print("That number doesn't exist. Try again from the number provided:")

    todo_list.pop(delete_task_text - 1)

print("Updated list:")


for i, task in enumerate(todo_list, start = 1):
    print(f"{i}. {task}")


total_tasks = int(len(todo_list))
print(f"\nTotal tasks: {total_tasks}")