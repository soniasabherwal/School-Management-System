from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
students = [
    {"id": 1, "name": "Alice", "classroom": "10A"},
    {"id": 2, "name": "Bob", "classroom": "10B"}
]

faculty = [
    {"id": 1, "name": "Mr. Smith", "subject": "Mathematics"},
    {"id": 2, "name": "Ms. Johnson", "subject": "English"}
]

exams = [
    {"id": 1, "subject": "Mathematics", "date": "2024-12-10"},
    {"id": 2, "subject": "English", "date": "2024-12-12"}
]

exam_results = [
    {"student_id": 1, "exam_id": 1, "score": 95},
    {"student_id": 2, "exam_id": 2, "score": 88}
]

classrooms = [
    {"id": "10A", "students": 30},
    {"id": "10B", "students": 25}
]

# Routes
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/faculty', methods=['GET'])
def get_faculty():
    return jsonify(faculty)

@app.route('/exams', methods=['GET'])
def get_exams():
    return jsonify(exams)

@app.route('/exam_results', methods=['GET'])
def get_exam_results():
    return jsonify(exam_results)

@app.route('/classrooms', methods=['GET'])
def get_classrooms():
    return jsonify(classrooms)

if __name__ == '__main__':
    app.run(debug=True)
