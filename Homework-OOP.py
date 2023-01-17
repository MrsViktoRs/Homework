def res(dict_value):
    if isinstance(dict_value, dict):
        value =[]
        for element in dict_value.values():
            for i in element:
                value.append(i)
                result = sum(value) / len(value)
    elif isinstance(dict_value, list):
        result = sum(dict_value) / len(dict_value)                    
    return round(result, 1)        

def student_res(list_student, course):
    result = []
    for student in list_student:
        if course in student.grades:
            result += student.grades[course]
    return res(result)

def lectorer_res(list_lecturer, course):
    result = []
    for lecturer in list_lecturer:
        if course in lecturer.grades:
            result += lecturer.grades[course]
    return res(result)             

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}    
        
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка' 

    def __str__(self):
        progress = ', '.join(self.courses_in_progress)
        finish = ', '.join(self.finished_courses)
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {res(self.grades)}\n'
                  f'Курсы в процессе изучения: {progress}\nЗавершенные курсы: {finish}')
        return result 
                                 
    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Это не студент")
            return    
        return res(self.grades) < res(other.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
         
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {res(self.grades)}'
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Это не лектор")
            return
        return res(self.grades) < res(other.grades)    

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
     
super_lecturer = Lecturer('Ivan', 'Pupkin') 
super_lecturer.courses_attached += ['Python']
super_lecturer.courses_attached += ['English']

great_lecturer = Lecturer('John', 'Dilinger')
great_lecturer.courses_attached += ['Git']
great_lecturer.courses_attached += ['English']

best_student = Student('Ruoy', 'Eman', 'M')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.courses_in_progress += ['English']
best_student.finished_courses += ['Введение в програмирование']
best_student.rate_hw(super_lecturer, "Python", 10)
best_student.rate_hw(super_lecturer, "Python", 5)
best_student.rate_hw(super_lecturer, "Python", 10)
best_student.rate_hw(super_lecturer, "English", 10)
best_student.rate_hw(great_lecturer, "Git", 5)
best_student.rate_hw(great_lecturer, "Git", 10)
best_student.rate_hw(great_lecturer, "English", 10)

nice_student = Student('Holly', 'Switch', 'W')
nice_student.courses_in_progress += ['Python']
nice_student.courses_in_progress += ['Git']
nice_student.courses_in_progress += ['English']
nice_student.finished_courses += ['Введение в програмирование']
nice_student.rate_hw(super_lecturer, "Python", 9)
nice_student.rate_hw(super_lecturer, "Python", 7)
nice_student.rate_hw(super_lecturer, "Python", 9)
nice_student.rate_hw(super_lecturer, "English", 9)
nice_student.rate_hw(great_lecturer, "Git", 9)
nice_student.rate_hw(great_lecturer, "Git", 8)
nice_student.rate_hw(great_lecturer, "English", 8)

mr_reviewer = Reviewer('Max', 'Jobs')
mr_reviewer.rate_hw(best_student, "Python", 9)
mr_reviewer.rate_hw(best_student, "Python", 8)
mr_reviewer.rate_hw(nice_student, "Python", 8)
mr_reviewer.rate_hw(nice_student, "Python", 10)
mr_reviewer.rate_hw(nice_student, "English", 10)

good_reviewer = Reviewer('Paul', 'Grays')
good_reviewer.rate_hw(best_student, "Git", 10)
good_reviewer.rate_hw(best_student, "Git", 7)
good_reviewer.rate_hw(nice_student, "Git", 10)
good_reviewer.rate_hw(nice_student, "Git", 8)
good_reviewer.rate_hw(nice_student, "English", 8)

list_student = [best_student, nice_student]
list_lecturer = [super_lecturer, great_lecturer]