from flask import Flask, request, jsonify

app = Flask(__name__)

students = []

@app.route('/students')
def getAllStudents():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def addStudent():
    data = request.get_json()
    if data and 'name' in data and 'age' in data:
        students.append({'name': data['name'], 'age': data['age']})
    return jsonify({'message': 'student added successfully!'})

if __name__ == "__main__" :
    app.run(port=8080, debug=True)