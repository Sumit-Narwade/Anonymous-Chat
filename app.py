from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# room_code -> set(usernames)
rooms = {
    "MAIN": set()
}

# sid -> {username, room}
users = {}


def generate_room_code():
    return str(random.randint(100000, 999999))


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('set_username')
def set_username(username):
    users[request.sid] = {"username": username, "room": "MAIN"}
    join_room("MAIN")
    rooms["MAIN"].add(username)
    emit('status', f"{username} joined MAIN room", room="MAIN")


@socketio.on('send_message')
def send_message(msg):
    user = users.get(request.sid)
    if not user:
        return
    emit(
        'message',
        {
            "username": user["username"],
            "message": msg
        },
        room=user["room"]
    )


@socketio.on('create_room')
def create_room():
    code = generate_room_code()
    switch_room(request.sid, code)
    emit('room_created', code)


@socketio.on('join_room_code')
def join_room_code(code):
    if code not in rooms:
        emit('error', 'Invalid room code')
        return
    switch_room(request.sid, code)


def switch_room(sid, new_room):
    user = users[sid]
    old_room = user["room"]
    username = user["username"]

    # Leave old room
    leave_room(old_room)
    rooms[old_room].discard(username)
    emit('status', f"{username} left the room", room=old_room)

    # Join new room
    join_room(new_room)
    rooms.setdefault(new_room, set()).add(username)
    user["room"] = new_room
    emit('status', f"{username} joined the room", room=new_room)


@socketio.on('disconnect')
def disconnect():
    user = users.get(request.sid)
    if not user:
        return
    username = user["username"]
    room = user["room"]

    rooms[room].discard(username)
    emit('status', f"{username} left the chat", room=room)
    del users[request.sid]


if __name__ == '__main__':
    socketio.run(app, debug=True)
