import node_stack
import array_queue
import csv
import random

def read_file():
    tasks = []
    with open("tasks_01.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            tasks.append(Task(line[0],line[1]))
    return tasks

class Task:
    __slots__ = ["__name","__location"]
    def __init__(self,name,location):
        self.__name = name
        self.__location = location
    
    def __str__(self):
        return self.__name + " in " + self.__location
    
    def get_location(self):
        return self.__location 

class Crewmate:
    __slots__ = ["__color","__tasks","__murdered"]
    def __init__(self, color,tasks=[]):
        self.__color = color
        self.__murdered = False
        self.__tasks = tasks

    def next_task(self):
        return self.__tasks.pop()
    
    def __str__(self):
        string = self.__color + " Crewmate"
        if self.__murdered == True:
            print(string + "deceased")
        return string
    
    def get_tasks(self):
        return self.__tasks
    
    def is_murdered(self):
        self.__murdered = True

    def set_task(self,task):
        self.__tasks.append(task)

class Ship:
    __slots__ = ["__locations","__tasks"]
    def __init__(self,tasks):
        self.__tasks = tasks
        self.__locations = []

    def get_location(self):
        for i in range(len(self.__tasks)):
            self.__locations.append(self.__tasks[i].get_location())

    def check_imposters(self, num_of_imposters):
        if int(num_of_imposters) <= 4:
            pass
        else:
            raise ValueError

    def total_crew(self,colors,num_of_imposters,tasks):
        crew_size  = 10 - int(num_of_imposters)
        crew = array_queue.Queue()
        for i in range(crew_size):   
            index = random.randint(0,len(colors)-1)
            color = colors[index]
            n_task = random.randint(3,6)
            assigned_task = []
            for i in range(n_task):
                r = random.randint(0,len(tasks)-1)
                assigned_task.append(tasks[r])
            crew_m = Crewmate(color,assigned_task)
            crew.enqueue(crew_m)
        return crew

    def journey(self,num_of_imposters):
        self.check_imposters(num_of_imposters)
        colors = ["Black","Blue","Brown","Cyan","Green","Pink","Purple","Red","White","Yellow"]
        cafeteria = self.total_crew(colors,num_of_imposters,self.__tasks)
        self.get_location()
        imposter_location = []
        for i in range(int(num_of_imposters)):
            index = random.randint(0,len(self.__locations)-1)
            imposter_location.append(index)
        murdered_crew = []
        while not cafeteria.is_empty():
            crewmate = cafeteria.dequeue()
            if len(crewmate.get_tasks()) > 0:
                task = crewmate.next_task()
                current_task_location = task.get_location()
                if current_task_location not in imposter_location:
                    print(task,"completed!")
                    index = random.randint(0,len(self.__locations)-1)
                    imposter_location.append(index)
                    cafeteria.enqueue(crewmate)
                if current_task_location in imposter_location:
                    crewmate.is_murdered()
                    murdered_crew.append(crewmate)
                else:
                    crew_finished = 0 
                    while not cafeteria.is_empty():
                        crewmate = cafeteria.dequeue()
                        if len(crewmate.get_tasks()) > 0:
                            break
                        elif len(crewmate.get_tasks()) == 0:
                            crew_finished += 1
                    if crew_finished == cafeteria.size():
                        cafeteria.enqueue(crewmate)
                        print("Crew won")


                        break
                    else:
                        continue
            continue
        else:
            print("Imposter won all the crew are dead")

def main():
    while True:
        prompt = (input("Welcome to among us! Please enter player amount(1-4): "))
        l_task = read_file()
        ship = Ship(l_task)
        ship.get_location()
        ship.journey(prompt)
        return True
if __name__ == "__main__":
    main()

