class ToDoList():
    tasks = []

    def __init__(self):
        a=0

    def runLoop(self,command):
        self.command = input("Enter command...")
        print ('command')
        if self.command == 'add':
            add_task
        if self.command == 'print':
            tasks(enumerate(1, 1))
            for task in tasks:
                print (task)
        if self.command == 'delete':
            del_task
        if self.command == 'sort':
            sort_task
        if self.command == 'edit':
            edit_task
        if self.command == 'save':
            save_tasks
        if self.command == 'open':
            open_tasks
        if self.command == 'quit':
            quit()
    def add_task(self):
        task = input()
        tasks.append(task)
        tasks(enumerate(1, 1))

    def del_task(self):
        x = input()
        del tasks[x]
        tasks(enumerate(1, 1))	
			
    def sort_task(self):
        tasks.sort() 
        print (tasks)

    def edit_task(self):
        x = input()
        print (tasks[x])
        t = input()
        print (replace(tasks, tasks[x]))

    def save_tasks(self):
        with open("to_do.txt","w") as file:
            for task in tasks:
                file.write ("%s\n" % task)
                
    def open_tasks(self):
        with open("to_do.txt", "w") as file:
            tasks = file.read()
            print (tasks)
