
from flask import Blueprint, request, jsonify

from model.student_model import Student
from service.student_service import StudentService


student_api = Blueprint("student_api", __name__)

service = StudentService()


def student_to_dict(student):
    return {
        "student_id": student.student_id,
        "name": student.name,
        "email": student.email,
        "phone": student.phone,
        "course": student.course,
        "age": student.age,
        "status": student.status
    }


# CREATE STUDENT
@student_api.route("/students", methods=["POST"])
def add_student():

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Request body is required"
            }), 400

        student = Student(
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            course=data.get("course"),
            age=data.get("age"),
            status=data.get("status", "Active")
        )

        saved_student = service.add_student(student)

        return jsonify({
            "message": "Student added successfully",
            "student": student_to_dict(saved_student)
        }), 201

    except ValueError as e:

        return jsonify({
            "error": str(e)
        }), 400

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# GET ALL STUDENTS
@student_api.route("/students", methods=["GET"])
def get_all_students():

    try:
        students = service.get_all_students()

        result = []

        for student in students:
            result.append(student_to_dict(student))

        return jsonify(result), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# GET STUDENT BY ID
@student_api.route("/students/<int:student_id>", methods=["GET"])
def get_student_by_id(student_id):

    try:
        student = service.get_student_by_id(student_id)

        return jsonify(
            student_to_dict(student)
        ), 200

    except ValueError as e:

        return jsonify({
            "error": str(e)
        }), 404

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# UPDATE STUDENT
@student_api.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Request body is required"
            }), 400

        student = Student(
            student_id=student_id,
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            course=data.get("course"),
            age=data.get("age"),
            status=data.get("status", "Active")
        )

        updated_student = service.update_student(student)

        return jsonify({
            "message": "Student updated successfully",
            "student": student_to_dict(updated_student)
        }), 200

    except ValueError as e:

        return jsonify({
            "error": str(e)
        }), 400

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# DELETE STUDENT
@student_api.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):

    try:
        service.delete_student(student_id)

        return jsonify({
            "message": "Student deleted successfully"
        }), 200

    except ValueError as e:

        return jsonify({
            "error": str(e)
        }), 404

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# SEARCH STUDENT BY NAME
@student_api.route("/students/search/<string:name>", methods=["GET"])
def search_student(name):

    try:
        students = service.search_student(name)

        result = []

        for student in students:
            result.append(student_to_dict(student))

        return jsonify(result), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500
# AI TOOL - GET STUDENT DATA
@student_api.route("/students/<int:student_id>/ai", methods=["GET"])
def get_student_ai(student_id):

    try:
        from ai_tool import get_student_from_db

        student = get_student_from_db(student_id)

        if not student:
            return jsonify({
                "error": "Student not found"
            }), 404

        return jsonify({
            "message": "Student data retrieved using AI tool",
            "student": {
                "student_id": student[0],
                "student_name": student[1],
                "email": student[2],
                "phone": student[3],
                "course": student[4],
                "age": student[5],
                "status": student[6]
            }
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500 
# AI QUESTION ENDPOINT
@student_api.route("/students/ai", methods=["POST"])
def student_ai_question():

    try:
        data = request.get_json()

        if not data or "question" not in data:
            return jsonify({
                "error": "Question is required"
            }), 400

        question = data["question"]

        from ai_student_summary import ai_agent

        response = ai_agent(question)

        return jsonify({
            "question": question,
            "ai_response": response
        }), 200

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500