
import sys
import os

# Add project root folder to Python path
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from db import get_connection
from model.student_model import Student


class StudentRepository:

    # CREATE
    def add_student(self, student):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO students
            (
                student_name,
                email,
                phone,
                course,
                age,
                status
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING student_id
            """,
            (
                student.name,
                student.email,
                student.phone,
                student.course,
                student.age,
                student.status
            )
        )

        student.student_id = cursor.fetchone()[0]

        conn.commit()
        cursor.close()
        conn.close()

        return student

    # READ ALL
    def get_all_students(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                student_id,
                student_name,
                email,
                phone,
                course,
                age,
                status
            FROM students
            ORDER BY student_id
            """
        )

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        students = []

        for row in rows:
            student = Student(
                student_id=row[0],
                name=row[1],
                email=row[2],
                phone=row[3],
                course=row[4],
                age=row[5],
                status=row[6]
            )

            students.append(student)

        return students

    # READ BY ID
    def get_student_by_id(self, student_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                student_id,
                student_name,
                email,
                phone,
                course,
                age,
                status
            FROM students
            WHERE student_id = %s
            """,
            (student_id,)
        )

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if row is None:
            return None

        return Student(
            student_id=row[0],
            name=row[1],
            email=row[2],
            phone=row[3],
            course=row[4],
            age=row[5],
            status=row[6]
        )

    # UPDATE
    def update_student(self, student):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE students
            SET
                student_name = %s,
                email = %s,
                phone = %s,
                course = %s,
                age = %s,
                status = %s
            WHERE student_id = %s
            """,
            (
                student.name,
                student.email,
                student.phone,
                student.course,
                student.age,
                student.status,
                student.student_id
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        return student

    # DELETE
    def delete_student(self, student_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM students
            WHERE student_id = %s
            """,
            (student_id,)
        )

        conn.commit()

        cursor.close()
        conn.close()

        return True

    # SEARCH BY NAME
    def search_student(self, name):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                student_id,
                student_name,
                email,
                phone,
                course,
                age,
                status
            FROM students
            WHERE student_name ILIKE %s
            ORDER BY student_id
            """,
            (f"%{name}%",)
        )

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        students = []

        for row in rows:
            student = Student(
                student_id=row[0],
                name=row[1],
                email=row[2],
                phone=row[3],
                course=row[4],
                age=row[5],
                status=row[6]
            )

            students.append(student)

        return students
