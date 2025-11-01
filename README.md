# 🧩 My Mini Flask App

A simple and lightweight web app built with **Flask** and **SQLite3**.  
It’s a small project that shows how the backend, frontend, and database work together to perform basic **CRUD** operations — specifically, creating and viewing user records.

---

## 🚀 What This App Can Do
- Display a list of all users stored in the database  
- Add new users with their name and email address  
- Handle data using **Flask** on the backend  
- Render pages dynamically with **Jinja2 templates**  
- Save everything persistently in an **SQLite** database  

---

## 🛠️ Tech Stack

| Area | Technology Used |
|------|-----------------|
| **Backend** | Flask (Python) |
| **Database** | SQLite3 |
| **Frontend** | HTML + Jinja2 |
| **Environment** | Virtual Environment (venv) |

---

## ⚙️ Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Ganeshchiluka5/my-mini-app.git
cd my-mini-app


2️⃣ Set Up a Virtual Environment
python -m venv venv
.\venv\Scripts\activate      # For Windows
# OR
source venv/bin/activate     # For macOS/Linux

3️⃣ Install the Required Packages
pip install flask

4️⃣ Run the App
python app.py


Then open your browser and go to 👉 http://127.0.0.1:5000

📂 Folder Structure
my-mini-app/
├── app.py               # Flask backend logic
├── data.db              # SQLite database file
├── templates/
│   └── index.html       # Main frontend template
└── README.md            # Documentation

🧠 How It Works

The frontend (index.html) displays the users and lets you add new ones.
The backend (app.py) handles the form submissions and talks to the database.
The database (data.db) stores all user information securely and pers'

💡 Future Ideas
Add “Edit” and “Delete” user options
Improve the UI using Bootstrap or TailwindCSS
Add form validation and better error handling

👨‍💻 About the Developer
Ganesh Chiluka
📧 chiluka.g@gmail.com
🌐 GitHub Profile
