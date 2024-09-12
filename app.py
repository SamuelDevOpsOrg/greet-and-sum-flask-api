import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Handle the root URL and return a welcome message.
    
    Returns:
        jsonify: A JSON response with a welcome message.
    """
    return jsonify({"message": "Hello, World!!"})

# Sample route with parameters
@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    """
    Handle the /greet/<name> URL and return a personalized greeting message.
    
    Args:
        name (str): The name to include in the greeting.
    
    Returns:
        jsonify: A JSON response with a personalized greeting message.
    """
    return jsonify({"message": f"Hello, {name}!"})

# A route with a POST method
@app.route('/add', methods=['POST'])
def add():
    """
    Handle the /add URL and return the sum of two numbers provided in the request.
    
    Returns:
        jsonify: A JSON response with the result of the addition.
    """
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    return jsonify({"result": a + b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 80)))
    # app.run(debug=True)
