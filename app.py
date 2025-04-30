from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Frontend se CORS allow karne ke liye

@app.route('/')
def home():
    return jsonify({"message": "Backend is running"})

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')

    # Aap yahan database me save kar sakte ho future me
    print(f"User Signup: {username}, {password}")

    return jsonify({"message": f"User {username} signed up successfully"})

@app.route('/api/data')
def data():
    return jsonify({"message": "Hello from backend!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    return f"User {name} signed up successfully with email {email}"





