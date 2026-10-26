import random
from analysis import calculate_age, calculate_student_average


def generate_student(index):
    year = random.randint(2000, 2006)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    birth_date = str(year) + "-" + str(month) + "-" + str(day)

    grades = []
    for _ in range(3):
        grades.append(round(random.uniform(0, 20), 2))

    return {
        "student_id": "STD" + str(index),
        "birth_date": birth_date,
        "grades": grades,
        "age": calculate_age(birth_date),
        "average": calculate_student_average(grades)
    }


def generate_students(num_students=10):
    students = []
    for i in range(1, num_students + 1):
        students.append(generate_student(i))
    return students
