from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello, World! Testing GitHub Actions Pipeline Deployment"})

# Sample route with parameters
@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

# A route with a POST method
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    return jsonify({"result": a + b})

if __name__ == '__main__':
    app.run(debug=True)
