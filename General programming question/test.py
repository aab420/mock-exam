import numpy as np 
class Students:
    def __innit__(self, courses):
        self.courses = dict(courses)

    def add_course(self, course_name, year, grade):
        course_name = input()
        grade = int(input("Input the grade:"))
        year = int(input("Input the year:"))
        listOfKeys = []
        for i in self.courses.keys():
            listOfKeys.append(i)
        if course_name not in listOfKeys:
            self.courses[course_name] = {"year": year, "grade": grade}
        elif course_name in listOfKeys:
            while True:
                print("This course already exists, would you like to change it?")
                answer = input()
                if answer == "yes" or "y":
                    self.courses[course_name] = {"year": year, "grade": grade}
                elif answer == "no" or "n":
                    exit()
                else:
                    continue 
            
    def change_grade(self, course, grade):
        course = input()
        year = int(input())
        grade = int(input())
        if course in self.courses.keys():
            self.grade = grade
        if course not in self.courses.keys():
            while True:
                print("This course is not in the dictionary, would you like to add it?")
                answer = input()
                if answer == "yes" or "y":
                    self.courses[course] = {"year": year, "grade": grade}
                elif answer == "no" or "n":
                    exit()
                else:
                    continue
        
    def calculate_mean(self, year):
        #self.year = int(year)
        year = int(input())
        list
        if year in self.courses.keys(year):
            if self.courses.values() == year:
                
        else:
            print(f"There are no courses in year {year}")

students1 = [Students({"Computing I": {"year": 1, "grade": np.random.randint(0,100)}, "Mathematics": {"year": 1, "grade": np.random.randint(0,100)}} for i in range(10))]
#students2 = [Students("Mathematics", {"year": 1, "grade": (np.random.randint(0,100))} for i in range(10)]
studentArray = []
studentArray.append(students1)
print(studentArray)

course = input() or None
def calculate_overall_mean(anylist, anycourse):
    for student in anylist:
        for item, value in self.courses.items():

    if anycourse == None:
        for i in anylist:
            average = 




    emissions = []
    for i in anylist:
        distance = ((i.velocity[0]**2 + i.velocity[1]**2)**0.5)*t
        totalemissions = i.emissions(distance)
        emissions.append(totalemissions)
    sumemissions = 0 

    for i in emissions:
        sumemissions += i 
        average = sumemissions/50
    return average
