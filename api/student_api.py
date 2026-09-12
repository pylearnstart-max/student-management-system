from flask import Blueprint, request, jsonify

from model.student_model import Student
from service.student_service import StudentService


student_api = Blueprint("student_api", __name__)

service = StudentService()


# CREATE
@student_api.route("/students", methods=["POST"])
def add_student():

    try:
        data = request.get_json()

        student = Student(
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            course=data.get("course"),
            age=data.get("age"),
            status=data.get("status", "Active")
        )

        message = service.add_student(student)

        return jsonify({
            "message": message
        }), 201

    except ValueError as e:

        return jsonify({
            "error": str(e)
        }), 400

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# GET ALL
@student_api.route("/students", methods=["GET"])
def get_all_students():

    try:
        rows = service.get_all_students()

        students = []

        for row in rows:
            students.append({
                "student_id": row[0],
                "name": row[1],
                "email": row[2],
                "phone": row[3],
                "course": row[4],
                "age": row[5],
                "status": row[6]
            })

        return jsonify(students), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# GET BY ID
@student_api.route("/students/<int:student_id>", methods=["GET"])
def get_student_by_id(student_id):

    try:
        row = service.get_student_by_id(student_id)

        student = {
            "student_id": row[0],
            "name": row[1],
            "email": row[2],
            "phone": row[3],
            "course": row[4],
            "age": row[5],
            "status": row[6]
        }

        return jsonify(student), 200

    except ValueError as e:

        return jsonify({
            "error": str(e)
        }), 404

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# UPDATE
@student_api.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):

    try:
        data = request.get_json()

        student = Student(
            student_id=student_id,
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            course=data.get("course"),
            age=data.get("age"),
            status=data.get("status", "Active")
        )

        message = service.update_student(student)

        return jsonify({
            "message": message
        }), 200

    except ValueError as e:

        return jsonify({
            "error": str(e)
        }), 400

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# DELETE
@student_api.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):

    try:
        message = service.delete_student(student_id)

        return jsonify({
            "message": message
        }), 200

    except ValueError as e:

        return jsonify({
            "error": str(e)
        }), 404

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500
@app.route("/students/search/<string:name>", methods=["GET"])
def search_student(name):
    students = StudentService.search_student(name)
    return jsonify(students), 200