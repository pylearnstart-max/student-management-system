def create_student_prompt(student):
    prompt = f"""
You are a student management assistant.

Student details:
Name: {student['student_name']}
Age: {student['age']}
Course: {student['course']}
Status: {student['status']}

Task:
Give a simple 2-sentence summary about this student.
"""

    return prompt


student = {
    "student_name": "Sita",
    "age": 22,
    "course": "Python",
    "status": "Active"
}

prompt = create_student_prompt(student)

print("PROMPT:")
print(prompt)