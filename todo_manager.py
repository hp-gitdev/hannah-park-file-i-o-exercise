print("=" * 35)
print("My To-Do List".center(35))
print("=" * 35)

#use a list to store tasks
todo_list = ["Buy groceries", "Finish homework", "Call the dentist"]
numbers = [1, 2, 3]
for i in range(len(todo_list)):
    print(f"{numbers[i]:<12} {todo_list[i]}")

print(f"Total tasks: {numbers[i]}")

# use append() for adding
new_task = input("What else would you like to do?")
print(f"1. Add a task: {new_task}")
todo_list.append(new_task)


# use pop() with an index for removing (remember: user sees 1-based numbers, Python uses 0-based)
#Handle the case the user enters an invalid task number with try/except

try:
    remove_task = int(input("Which numner of task would you like to remove?"))
    remove = todo_list.pop(remove_task - 1)
    print(f"2. Remove a task: {remove}")

except ValueError:
    print("Invalid number. Removing task number 2.")
    remove = todo_list.pop(1)
    print(f"Remove a task: Finish Homework")



print("Updated list:")
for i in range(len(todo_list)):
    print(f"{numbers[i]:<12} {todo_list[i]}")

print(f"\nTotal tasks: 3")