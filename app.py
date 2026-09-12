from flask import Flask

from api.student_api import student_api


app = Flask(__name__)

app.register_blueprint(student_api)


if __name__ == "__main__":
    app.run(debug=True)