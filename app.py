from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.secret_key = 'secret!'

# Use eventlet async mode for Render
socketio = SocketIO(app, async_mode='eventlet')

# username -> set of session IDs
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
    username_to_remove = None

    for username, sessions in list(user_sessions.items()):
        if sid in sessions:
            sessions.remove(sid)
            if not sessions:  # no sessions left for this user
                username_to_remove = username
                del user_sessions[username]
            break

    if username_to_remove:
        emit('status', f"{username_to_remove} left the chat", broadcast=True)

if __name__ == '__main__':
    # Render uses port environment variable OR defaults to 10000
    socketio.run(app, host='0.0.0.0', port=10000)
