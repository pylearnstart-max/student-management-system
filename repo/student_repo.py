from db import get_connection


class StudentRepository:

    # CREATE
    def add_student(self, student):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO Students
        (Name, Email, Phone, Course, Age, Status)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        cursor.execute(
            query,
            student.name,
            student.email,
            student.phone,
            student.course,
            student.age,
            student.status
        )

        conn.commit()
        cursor.close()
        conn.close()

    # READ ALL
    def get_all_students(self):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT StudentID, Name, Email, Phone, Course, Age, Status
        FROM Students
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows

    # READ BY ID
    def get_student_by_id(self, student_id):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT StudentID, Name, Email, Phone, Course, Age, Status
        FROM Students
        WHERE StudentID = ?
        """

        cursor.execute(query, student_id)

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        return row

    # UPDATE
    def update_student(self, student):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE Students
        SET Name = ?,
            Email = ?,
            Phone = ?,
            Course = ?,
            Age = ?,
            Status = ?
        WHERE StudentID = ?
        """

        cursor.execute(
            query,
            student.name,
            student.email,
            student.phone,
            student.course,
            student.age,
            student.status,
            student.student_id
        )

        conn.commit()

        cursor.close()
        conn.close()

    # DELETE
    def delete_student(self, student_id):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        DELETE FROM Students
        WHERE StudentID = ?
        """

        cursor.execute(query, student_id)

        conn.commit()

        cursor.close()
        conn.close()