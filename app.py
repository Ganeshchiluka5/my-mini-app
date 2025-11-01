from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Home page - show all users
@app.route('/')
def index():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    con.close()
    return render_template('index.html', users=rows)

# Add user page - handle form submission
@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']

    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    con.commit()
    con.close()

    return redirect('/')

if __name__ == '__main__':
    print("✅ Flask server starting on http://127.0.0.1:5000")
    app.run(debug=True)
