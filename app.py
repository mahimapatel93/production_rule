from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Flask to App is Running 🚀"

# Sample GET API
@app.route("/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "Guest")
    return jsonify({
        "message": f"Hello {name}"
    })

# Sample POST API
@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json
    return jsonify({
        "status": "success",
        "received_data": data
    })

if __name__ == "__main__":
    app.run(debug=True)
