from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = "secret-key"

# Enable websocket properly on Render
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

# Track users per session
active_users = {}   # sid → username
user_sessions = {}  # username → set(sid)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("join")
def handle_join(username):
    sid = request.sid
    active_users[sid] = username

    if username not in user_sessions:
        user_sessions[username] = set()

    user_sessions[username].add(sid)

    emit("status", f"{username} joined the chat", broadcast=True)

@socketio.on("message")
def handle_message(data):
    username = data.get("username", "Anonymous")
    message = data.get("message", "")

    emit("message", {"username": username, "message": message}, broadcast=True)

@socketio.on("disconnect")
def handle_disconnect():
    sid = request.sid

    if sid in active_users:
        username = active_users[sid]

        # remove sid
        user_sessions[username].remove(sid)

        # remove username if no sessions left
        if len(user_sessions[username]) == 0:
            del user_sessions[username]
            emit("status", f"{username} left the chat", broadcast=True)

        del active_users[sid]

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=10000)
