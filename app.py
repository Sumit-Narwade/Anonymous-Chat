from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
import os

app = Flask(__name__)
app.secret_key = 'secret!'

# IMPORTANT for Render
socketio = SocketIO(app, cors_allowed_origins="*")

# username -> session list
user_sessions = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def handle_join(username):
    sid = request.sid
    if username not in user_sessions:
        user_sessions[username] = set()
    user_sessions[username].add(sid)
    emit('status', f"{username} joined the chat", broadcast=True)

@socketio.on('message')
def handle_message(data):
    username = data.get('username', 'Anonymous')
    message = data.get('message', '')
    send({'username': username, 'message': message}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    sid = request.sid
    user_left = None

    for username, sessions in list(user_sessions.items()):
        if sid in sessions:
            sessions.remove(sid)
            if not sessions:
                user_left = username
                del user_sessions[username]
            break

    if user_left:
        emit('status', f"{user_left} left the chat", broadcast=True)

# FINAL RENDER COMPATIBLE SERVER RUNNER
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host='0.0.0.0', port=port)
