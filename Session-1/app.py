from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/about')
def about():
    return 'about page!'

@app.route('/echo', methods = ['POST'])
def echo_post():
    data = request.json
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=8080)