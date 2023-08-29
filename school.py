#imports

from enum import Enum
import pickle
 



#class's

class Actions(Enum):
    ADD_STUDENT = 1
    SHOW_STUDENTS = 2
    ADD_GRADE = 3
    SHOW_GRADES= 4   
    SHOW_AVARAGE= 5
    EXIT = 0

class Test:
    def __init__(self, type, grade):
        self.type =type
        self.grade =grade

class Student:
    
    def __init__(self, name, age=20):
        self.name = name
        self.age = age
        self.tests_list = []

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'
    
    def add_test(self, type, grade):
        self.tests_list.append (Test(type,grade))

    def show_grades(self):
        for x in self.tests_list:
            print(f'test: {x.type}, grade: {x.grade}')
    
    def calculate_average(self):
        total_grades = sum(int(test.grade) for test in self.tests_list)
        return total_grades / len(self.tests_list)
        

    def print_avarage(self):
        average = self.calculate_average()
        print(f'Average for {self.name}: {average}')

    @staticmethod
    def load_students():
        try:
            with open('students.pkl', 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []

    @classmethod
    def save_students(cls, students):
        with open('students.pkl', 'wb') as file:
            pickle.dump(students, file)
        


#var

students = []




# Menu function

def menu():
    while True:
        for x in Actions:
            print (f'{x.name} = {x.value}')
        user_selection = Actions(int(input("enter your selection:")))
        if user_selection == Actions.ADD_STUDENT: add_student()
        if user_selection == Actions.SHOW_STUDENTS: show_students()
        if user_selection == Actions.ADD_GRADE: add_grade()
        if user_selection == Actions.SHOW_GRADES: show_grades()
        if user_selection == Actions.SHOW_AVARAGE: show_avarage()
        if user_selection == Actions.EXIT: return

def add_student():
    name = input("enter name:")
    age = input ("enter age:")
    students.append(Student(name,age))
    print(f'{name} added to students')

def show_students():
    for x in students:
        print (x)

def search():
    name2search = input("enter student's name:")
    for x in students:
        if name2search == x.name:
            return x
        
def add_grade():
    student2add = search()
    type = input("enter test:")
    grade = input("enter grade:")
    student2add.add_test(type, grade)
    print(f'{type} was added')
        
def show_grades():
    student2showGrades = search()
    student2showGrades.show_grades()

def show_avarage():
    student2showAvarage = search()
    student2showAvarage.print_avarage()

# entery point

if __name__ == '__main__':
    students = Student.load_students()
    menu()
    Student.save_students(students)
    print("GoodBye:)")