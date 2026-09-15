id="3f0d2a"
from db import get_connection


# TOOL 1: Get student by ID
def get_student_from_db(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT student_id, student_name, email, phone, course, age, status
        FROM students
        WHERE student_id = %s
    """

    cursor.execute(query, (student_id,))
    student = cursor.fetchone()

    cursor.close()
    conn.close()

    return student


# TOOL 2: Search students by name
def search_students_by_name(name):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT student_id, student_name, email, phone, course, age, status
        FROM students
        WHERE student_name ILIKE %s
    """

    cursor.execute(query, (f"%{name}%",))
    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return students


# TEST TOOLS
if __name__ == "__main__":

    # Test Tool 1
    student = get_student_from_db(2)

    print("TOOL 1 - GET STUDENT:")
    print(student)

    print()

    # Test Tool 2
    students = search_students_by_name("meena")

    print("TOOL 2 - SEARCH STUDENTS:")
    
    for student in students:
        print(student)

# TOOL DEFINITIONS

student_tools = [

    {
        "name": "get_student_from_db",
        "description": "Get student details using student ID.",
        "input": {
            "student_id": "integer"
        }
    },

    {
        "name": "search_students_by_name",
        "description": "Search students using student name.",
        "input": {
            "name": "string"
        }
    }
]


# TEST TOOL DEFINITIONS
if __name__ == "__main__":

    print("AVAILABLE TOOLS:")

    for tool in student_tools:
        print("\nTool Name:", tool["name"])
        print("Description:", tool["description"])
        print("Input:", tool["input"])



