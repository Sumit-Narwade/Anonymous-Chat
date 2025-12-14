🔮 Anonymous Chat Web App

A modern, real-time anonymous chat application built with Flask and Flask-SocketIO, supporting:

🌐 Public main room (everyone can chat)

🔒 Private rooms via 6-digit codes

🟢 Join / leave notifications

🌙 Dark/light mode

📱 Mobile responsive design

🚀 Features

Username prompt on first visit

Global chat room for all users

Create private rooms with auto-generated 6-digit code

Join private rooms via code (restricted access)

Real-time messaging

Join/Leave notifications in chat

Dark mode toggle for eye comfort

Responsive layout for desktop & mobile

🎨 Demo

Add a screenshot or GIF of your app here

🛠 Installation
Prerequisites

Python 3.10+

pip

Setup

Clone the repository

git clone https://github.com/your-username/anonymous-chat.git
cd anonymous-chat


Create a virtual environment (recommended)

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate


Install dependencies

pip install flask flask-socketio

▶️ Running the App
python app.py


Open your browser and go to:

http://localhost:5000

💡 How to Use

Enter your username on first visit

Join the Main Room automatically

Use Create Room button → generates a private 6-digit room code

Use Join Room button → enter code to join a private room

Chat with users in the same room only

Toggle Dark Mode with 🌙 button



📂 Project Structure
anonymous-chat/
│
├── app.py              # Flask backend with SocketIO
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend HTML file
└── static/
    └── style.css       # CSS styling for the app


<img width="1919" height="1019" alt="Screenshot 2025-12-14 214259" src="https://github.com/user-attachments/assets/118b5d8f-53a1-47a7-a131-16e03f4e971d" />
<img width="1919" height="1028" alt="Screenshot 2025-12-14 214247" src="https://github.com/user-attachments/assets/6a40ddf1-b2a4-4edc-8816-810ce098fb0b" />
<img width="1915" height="939" alt="Screenshot 2025-12-14 214235" src="https://github.com/user-attachments/assets/a4c60b4e-0a9c-4bbb-aef0-7d7f20939da5" />
<img width="1910" height="939" alt="Screenshot 2025-12-14 214223" src="https://github.com/user-attachments/assets/1cfa3ef5-7d67-4fc4-874e-a20401c2a005" />

