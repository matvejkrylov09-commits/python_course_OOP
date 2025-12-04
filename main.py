class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished = []
        self.in_progress = []
        self.marks = {} 

    def avg_mark(self):
        total = []
        for m in self.marks.values():
            total += m
        if total:
            return sum(total) / len(total)
        return 0

    def rate_lect(self, lect, subject, mark):
        if isinstance(lect, Lecturer) and subject in self.in_progress and subject in lect.assigned_courses:
            if subject in lect.marks:
                lect.marks[subject].append(mark)
            else:
                lect.marks[subject] = [mark]
        else:
            return "Ошибка"

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за ДЗ: {self.avg_mark():.1f}\n"
                f"Курсы в процессе: {', '.join(self.in_progress)}\n"
                f"Законченные курсы: {', '.join(self.finished)}")

    def __lt__(self, other):
        return self.avg_mark() < other.avg_mark()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.assigned_courses = []


class Reviewer(Mentor):
    def rate_hw(self, student, subject, mark):
        if isinstance(student, Student) and subject in self.assigned_courses and subject in student.in_progress:
            if subject in student.marks:
                student.marks[subject].append(mark)
            else:
                student.marks[subject] = [mark]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.marks = {}

    def avg_mark(self):
        total = []
        for m in self.marks.values():
            total += m
        if total:
            return sum(total) / len(total)
        return 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.avg_mark():.1f}")

    def __lt__(self, other):
        return self.avg_mark() < other.avg_mark()


# Создаем студентов
s1 = Student("Ольга", "Алёхина", "F")
s1.in_progress += ["Python"]

s2 = Student("Иван", "Сидоров", "M")
s2.in_progress += ["Python"]

# Создаем лекторов
l1 = Lecturer("Иван", "Иванов")
l1.assigned_courses += ["Python"]

l2 = Lecturer("Пётр", "Петров")
l2.assigned_courses += ["Python"]

# Создаеми проверяющих
r1 = Reviewer("Мария", "Лисина")
r1.assigned_courses += ["Python"]

r2 = Reviewer("Антон", "Волков")
r2.assigned_courses += ["Python"]

# Оценки студентам
r1.rate_hw(s1, "Python", 9)
r1.rate_hw(s1, "Python", 10)
r2.rate_hw(s2, "Python", 8)

# Оценки лекторам
s1.rate_lect(l1, "Python", 7)
s1.rate_lect(l2, "Python", 9)
s2.rate_lect(l1, "Python", 8)

# Функции подсчета средних
def avg_students_mark(students, subject):
    all_marks = []
    for st in students:
        if subject in st.marks:
            all_marks += st.marks[subject]
    if all_marks:
        return sum(all_marks) / len(all_marks)
    return 0


def avg_lecturers_mark(lecturers, subject):
    all_marks = []
    for lect in lecturers:
        if subject in lect.marks:
            all_marks += lect.marks[subject]
    if all_marks:
        return sum(all_marks) / len(all_marks)
    return 0



print(s1)
print()
print(l1)
print()
print(r1)
print()
print("Средняя студентов по Python:", avg_students_mark([s1, s2], "Python"))
print("Средняя лекторов по Python:", avg_lecturers_mark([l1, l2], "Python"))