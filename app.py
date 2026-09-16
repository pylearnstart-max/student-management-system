from flask import Flask, request
from ai_student_summary import ai_agent

app = Flask(__name__)


@app.route("/ai/ask", methods=["POST"])
def ask_ai():
    data = request.get_json()

    question = data.get("question")

    if not question:
        return {"error": "Question is required"}, 400

    answer = ai_agent(question)

    return {
        "question": question,
        "answer": answer
    }


if __name__ == "__main__":
    app.run(debug=True)