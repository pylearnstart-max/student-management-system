from repo.student_repo import StudentRepository


class StudentService:

    def __init__(self):
        self.repo = StudentRepository()

    # CREATE
    def add_student(self, student):

        if not student.name:
            raise ValueError("Name is required")

        if not student.email:
            raise ValueError("Email is required")

        if student.age is not None and student.age < 18:
            raise ValueError("Age must be 18 or above")

        self.repo.add_student(student)

        return "Student added successfully"

    # READ ALL
    def get_all_students(self):

        return self.repo.get_all_students()

    # READ BY ID
    def get_student_by_id(self, student_id):

        student = self.repo.get_student_by_id(student_id)

        if not student:
            raise ValueError("Student not found")

        return student

    # UPDATE
    def update_student(self, student):

        if not student.name:
            raise ValueError("Name is required")

        if not student.email:
            raise ValueError("Email is required")

        if student.age is not None and student.age < 18:
            raise ValueError("Age must be 18 or above")

        existing = self.repo.get_student_by_id(student.student_id)

        if not existing:
            raise ValueError("Student not found")

        self.repo.update_student(student)

        return "Student updated successfully"

    # DELETE
    def delete_student(self, student_id):

        existing = self.repo.get_student_by_id(student_id)

        if not existing:
            raise ValueError("Student not found")

        self.repo.delete_student(student_id)

        return "Student deleted successfully"
    # SEARCH BY NAME
    def search_student(self, name):

        return self.repo.search_student(name)