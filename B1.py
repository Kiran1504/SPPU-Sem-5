class Task:
    def __init__(self, id , at: int, bt: int):
        self.id = id
        self.at = at
        self.bt = bt
        self.ct = -1
        self.tat = -1
        self.wt = -1

    def display(self):
        print(self.id, self.at, self.bt)

class Schedular:
    def __init__(self) -> None:
        self.taskList = []
        pass
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
        def sortTaskList(l):
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
        
        copyList = self.taskList.copy()
        sortTaskList(copyList)
        currTime = copyList[0].at
        print("Executing task using FCFS Scheduling Algorithm: ")
        print()
        totalWaitTime = 0
        totalTurnAroundTime = 0
        for i in copyList:
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
        pass



t = Schedular()
t.addToList()
t.firstComeFirstServe()
t.displayList()
# t.display()
