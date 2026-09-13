# Jenkins automatic CI test
import sys
import os
import time
import sys
import os
import time

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from service.student_service import StudentService
from model.student_model import Student


service = StudentService()

# Track whether any test failed
test_failed = False


# CREATE
unique_id = int(time.time())

student = Student(
    name="meena",
    email=f"meena{unique_id}@gmail.com",
    phone="9123456790",
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
    test_failed = True


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
    test_failed = True


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
    test_failed = True


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
    test_failed = True


# Final test result
if test_failed:
    print("\nTESTS FAILED")
    sys.exit(1)
else:
    print("\nALL TESTS PASSED")
    sys.exit(0)

