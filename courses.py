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

    def rate_lecture(self, lecturer, course, grade):
        if course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        grades_list = sum(list(self.grades.values()), [])
        if len(grades_list) == 0:
            res = 0
        else:
            res = round(int(sum(grades_list)) / len(grades_list), 1)
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            res = f'Это не студент. Можно сравнивать только со студентом.'
        elif self.average_grade() < other.average_grade():
            res = f'{other.name} {other.surname} сильнее, чем {self.name} {self.surname}'
        elif self.average_grade() > other.average_grade():
            res = f'{other.name} {other.surname} слабее, чем {self.name} {self.surname}'
        else:
            res = f'{other.name} {other.surname} и {self.name} {self.surname} равны'
        return res

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия:{self.surname} \n' \
              f'Средняя оценка за ДЗ:{self.average_grade()} \n' \
              f'Курсы в процессе изучения: {self.courses_in_progress} \n' \
              f'Завершенные курсы: {self.finished_courses}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        grades_list = sum(list(self.grades.values()), [])
        if len(grades_list) == 0:
            res = 0
        else:
            res = round(int(sum(grades_list)) / len(grades_list), 1)
        return res

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия:{self.surname} \n' \
              f'Средняя оценка за лекции:{self.average_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other,Lecturer):
            res = f'Это не студент. Можно сравнивать только со студентом.'
        elif self.average_grade() < other.average_grade():
            res = f'{other.name} {other.surname} сильнее, чем {self.name} {self.surname}'
        elif self.average_grade() > other.average_grade():
            res = f'{other.name} {other.surname} слабее, чем {self.name} {self.surname}'
        else:
            res = f'{other.name} {other.surname} и {self.name} {self.surname} равны'
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and\
                course in self.courses_attached and\
                course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия:{self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.add_courses('Введение в прогпаммирование')

nice_student = Student('Vera', 'Olegova', 'your_gender')
nice_student.courses_in_progress += ['Git']
nice_student.courses_in_progress += ['Python']
nice_student.add_courses('Введение в прогпаммирование')


cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

nice_mentor = Reviewer('Looks', 'Nice')
nice_mentor.courses_attached += ['Git']

extra_lecturer = Lecturer('Who', 'His')
extra_lecturer.courses_attached += ['Python']

intel_lecturer = Lecturer('Clever', 'Boy')
intel_lecturer.courses_attached += ['Git']


cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(nice_student, 'Python', 8)
cool_mentor.rate_hw(nice_student, 'Python', 8)
cool_mentor.rate_hw(nice_student, 'Python', 9)
nice_mentor.rate_hw(nice_student, 'Git', 10)
nice_mentor.rate_hw(nice_student, 'Git', 10)

best_student.rate_lecture(extra_lecturer, 'Python', 9)
best_student.rate_lecture(extra_lecturer, 'Python', 10)

best_student.rate_lecture(intel_lecturer, 'Git', 9)
best_student.rate_lecture(intel_lecturer, 'Git', 10)

nice_student.rate_lecture(extra_lecturer, 'Python', 9)
nice_student.rate_lecture(extra_lecturer, 'Git', 10)

print(best_student.grades)
print(nice_student.grades)
print()
print(extra_lecturer.grades)
print()
print(intel_lecturer.grades)
print()

print(cool_mentor)
print()
print(nice_mentor)
print()

print(extra_lecturer )
print()
print(intel_lecturer )
print()

print(best_student)
print()
print(nice_student)
print()
print(best_student > nice_student)
print(extra_lecturer > intel_lecturer)