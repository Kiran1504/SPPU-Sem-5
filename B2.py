class Task:
    def __init__(self, id , at: int, bt: int):
        self.id = id
        self.at = at
        self.bt = bt
        self.ct = -1
        self.tat = -1
        self.wt = -1
        self.rem_bt = bt

    def display(self):
        print(self.id, self.at, self.bt)

class Schedular:
    def __init__(self) -> None:
        self.taskList = []
        pass

    def sortTaskList(self, l):
        n = len(l)
        for i in range(n-1):
            swapped = False
            for j in range(0, n-i-1):
                if(l[j].at > l[j+1].at):
                    temp = l[j]
                    l[j] = l[j+1]
                    l[j+1] = temp
                    swapped = True
            if not swapped:
                break

    def addToList(self):
        while True:
            print("Enter -1 task id to exit")
            id = input("Enter the task id: ")
            if id == '-1': break
            at = int(input("Enter the arrival time: "))
            bt = int(input("Enter the brust time: "))
            self.taskList.append(Task(id, at, bt))
            print()
    
    def displayList(self):
        print("Task id  | AT  | BT  | CT  | TAT  | WT  ")
        for i in self.taskList:
            print(i.id, end = " "*(8 - len(i.id)))
            print(" |", i.at, end=" "*(4 - len(str(i.at))))
            print("|", i.bt, end=" "*(4 - len(str(i.bt))))
            print("|", i.ct, end=" "*(4 - len(str(i.ct))))
            print("|", i.tat, end=" "*(5 - len(str(i.tat))))
            print("|", i.wt, end=" "*(4 - len(str(i.wt))))
            print()
            # i.display()

    def firstComeFirstServe(self):
        
        copyList = self.taskList.copy()
        self.sortTaskList(copyList)
        currTime = copyList[0].at
        print("Executing task using FCFS Scheduling Algorithm: ")
        print()
        totalWaitTime = 0
        totalTurnAroundTime = 0
        for i in copyList:
            if currTime < i.at:
                currTime = i.at
            currTime += i.bt
            print(f"Last Executed Task - {i.id} for - {i.bt} units of time -- current time - {currTime}")
            i.ct = currTime
            i.tat = i.ct - i.at
            i.wt = i.tat - i.bt
            totalTurnAroundTime += i.tat
            totalWaitTime += i.wt
        print()
        print("Average Wait time is: ", float(totalWaitTime/len(copyList)))
        print("Average Turn Around Time time is: ", float(totalTurnAroundTime/len(copyList)))
        print()
        self.displayList();
        pass

    def shortestJobFirst(self):
        print()
        print("Executing task using FCFS Scheduling Algorithm: ")
        print()
        
        # self.taskList.sort(key=lambda x: x.at)  # Sort tasks by arrival time
        copyList = self.taskList.copy()
        self.sortTaskList(copyList)
        current_time = 0
        totalTurnAroundTime = 0
        totalWaitTime = 0
        completed_tasks = []
        
        while len(completed_tasks) < len(copyList):
            available_tasks = [t for t in copyList if t.at <= current_time and t not in completed_tasks]
            
            if not available_tasks:
                current_time += 1
                continue
            
            task = min(available_tasks, key=lambda x: x.bt)
            print(f"Last Executed Task - {task.id} for - {task.bt} units of time -- current time - {current_time}")
            task.ct = current_time + task.bt
            task.tat = task.ct - task.at
            task.wt = task.tat - task.bt
            current_time = task.ct
            completed_tasks.append(task)
            totalTurnAroundTime += task.tat
            totalWaitTime += task.wt
        print()
        print("Average Wait time is: ", float(totalWaitTime/len(completed_tasks)))
        print("Average Turn Around Time time is: ", float(totalTurnAroundTime/len(completed_tasks)))
        print()
        pass

    def roundRobin(self):
        print()
        print("Executing task using Round Robin Scheduling Algorithm: ")
        print()
        
        # self.taskList.sort(key=lambda x: x.at)  # Sort tasks by arrival time
        copyList = self.taskList.copy()
        self.sortTaskList(copyList)
        current_time = 0
        totalTurnAroundTime = 0
        totalWaitTime = 0
        completed_tasks = []
        ready_queue = []

        # print("copyList", copyList)
        self.time_quantum = int(input("\nEnter the time quantum: "))
        available_tasks = [t for t in copyList if t.at <= current_time and t not in completed_tasks]
        
        for i in available_tasks:
            if i not in ready_queue:
                ready_queue.append(i)
        while len(completed_tasks) < len(copyList):

            if not ready_queue:
                current_time += 1
                continue
            # print("available", [i.id for i in available_tasks])
            # print(" ready_queue", [i.id for i in ready_queue])
            task = ready_queue.pop(0)
            time_slice = min(task.rem_bt, self.time_quantum)
            task.rem_bt -= time_slice
            current_time += time_slice
            print(f"Last Executed Task - {task.id} for - {time_slice} units of time -- current time - {current_time}")
            if task.rem_bt <= 0:
                task.ct = current_time
                task.tat = task.ct - task.at
                task.wt = task.tat - task.bt
                totalTurnAroundTime += task.tat
                totalWaitTime += task.wt
                completed_tasks.append(task)
            else:
                available_tasks = [t for t in copyList if t.at <= current_time and t not in completed_tasks]
            
                for i in available_tasks:
                    if i not in ready_queue and i != task:
                        ready_queue.append(i)
                ready_queue.append(task)
        print()
        print("Average Wait time is: ", float(totalWaitTime/len(completed_tasks)))
        print("Average Turn Around Time time is: ", float(totalTurnAroundTime/len(completed_tasks)))
        print()
        self.displayList()
        pass

    def priorityScheduling(self):
        pass



t = Schedular()
t.addToList()
# t.firstComeFirstServe()
# t.shortestJobFirst()
# t.displayList()
t.roundRobin()
# t.display()
