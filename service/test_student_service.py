import sys
import os

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from service.student_service import StudentService
from model.student_model import Student


service = StudentService()


# CREATE
student = Student(
    name="meena",
    email="meena@gmail.com",
    phone="9123456789",
    course="Python",
    age=22,
    status="Active"
)

try:
    saved_student = service.add_student(student)

    print("CREATE SUCCESS")
    print("ID:", saved_student.student_id)
    print("Name:", saved_student.name)
    print("Email:", saved_student.email)

except Exception as e:
    print("CREATE ERROR:", e)


# READ ALL
try:
    students = service.get_all_students()

    print("\nALL STUDENTS")

    for s in students:
        print(
            s.student_id,
            s.name,
            s.email,
            s.phone,
            s.course,
            s.age,
            s.status
        )

except Exception as e:
    print("READ ERROR:", e)


# READ BY ID
try:
    found = service.get_student_by_id(student.student_id)

    print("\nSTUDENT BY ID")
    print(
        found.student_id,
        found.name,
        found.email,
        found.phone,
        found.course,
        found.age,
        found.status
    )

except Exception as e:
    print("GET BY ID ERROR:", e)


# SEARCH
try:
    results = service.search_student("meena")

    print("\nSEARCH RESULT")

    for s in results:
        print(
            s.student_id,
            s.name,
            s.email,
            s.phone,
            s.course,
            s.age,
            s.status
        )

except Exception as e:
    print("SEARCH ERROR:", e)