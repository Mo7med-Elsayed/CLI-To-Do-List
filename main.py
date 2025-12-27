message = """1 - Add tasks to a list
2 - Mark tasks as complete
3 - View tasks
4 - Quit
"""

tasks = []


def addTask():
  print("=============================================")
  task = input("Add a task description: ")
  print("=============================================")
  tasks.append(task)

def taskDone():
  print("=============================================")
  taskNumber = input("Enter the task number: ")
  print("=============================================")
  tasks.pop(int(taskNumber) - 1)

def viewTasks():
  print("=============================================")
  for task in tasks:
    print(task)
  print("=============================================")
    
    
while True:
  print(message)
  choice = input("Enter your choice: ")

  if choice == "1":
    addTask()
  elif choice == "2":
    taskDone()
  elif choice == "3":
    viewTasks()
  elif choice == "4":
    break
  else:
    print("Invalid choice, Enter a number from 1 to 4")