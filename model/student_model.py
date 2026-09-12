class Student:

    def __init__(
        self,
        student_id=None,
        name=None,
        email=None,
        phone=None,
        course=None,
        age=None,
        status="Active"
    ):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone = phone
        self.course = course
        self.age = age
        self.status = status