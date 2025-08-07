from flask import Flask, request
import websocket_handler

app = Flask(__name__)

@app.route("/")
def dashboard():
    with open("static/dashboard.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route("/send", methods=["POST"])
def send_command():
    data = request.get_json()
    cmd = data.get("command")
    websocket_handler.broadcast({"command": "run", "code": cmd})
    return "Sent"

if __name__ == "__main__":
    websocket_handler.start_server()
    app.run(host="0.0.0.0", port=5000)
