
from ai_tool import get_student_from_db, search_students_by_name
import re


# TOOL 1
def get_student_tool(student_id):
    return get_student_from_db(student_id)


# TOOL 2
def search_student_tool(name):
    return search_students_by_name(name)


# STEP 1: CREATE TOOL CALL
def create_tool_call(question):

    question_lower = question.lower()

    # Student ID
    match = re.search(r"student\s+(\d+)", question_lower)

    if match:

        student_id = int(match.group(1))

        return {
            "tool": "get_student_from_db",
            "arguments": {
                "student_id": student_id
            }
        }

    # Student name
    if "named" in question_lower:

        name = question_lower.split("named", 1)[1].strip()

        return {
            "tool": "search_students_by_name",
            "arguments": {
                "name": name
            }
        }

    return None


# STEP 2: EXECUTE TOOL
def execute_tool(tool_call):

    tool_name = tool_call["tool"]
    arguments = tool_call["arguments"]

    print("\nTOOL CALL:")
    print(tool_name)

    print("ARGUMENTS:")
    print(arguments)

    if tool_name == "get_student_from_db":

        student_id = arguments["student_id"]

        result = get_student_tool(student_id)

        return result


    if tool_name == "search_students_by_name":

        name = arguments["name"]

        result = search_student_tool(name)

        return result


    return None


# STEP 3: AGENT LOOP
def ai_agent(question):

    print("USER:", question)

    # Agent creates tool call
    tool_call = create_tool_call(question)

    if not tool_call:
        return "I don't know which tool to use."

    print("\nAGENT DECISION:")
    print(tool_call)

    # Execute tool
    tool_result = execute_tool(tool_call)

    print("\nTOOL RESULT:")
    print(tool_result)

    # Agent checks tool result
    if not tool_result:

        return "No student data found."

    # Final response
    if tool_call["tool"] == "get_student_from_db":

        student = tool_result

        return (
            f"{student[1]} is {student[5]} years old "
            f"and is studying {student[4]}. "
            f"The student is currently {student[6]}."
        )


    if tool_call["tool"] == "search_students_by_name":

        students = tool_result

        result = []

        for student in students:

            result.append(
                f"ID: {student[0]}, "
                f"Name: {student[1]}, "
                f"Course: {student[4]}, "
                f"Age: {student[5]}, "
                f"Status: {student[6]}"
            )

        return "\n".join(result)


# TEST
if __name__ == "__main__":

    question = "Give me details of student 5"

    response = ai_agent(question)

    print("\nFINAL ANSWER:")
    print(response)

