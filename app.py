from flask import Flask, render_template, request, redirect
import oracledb

app = Flask(__name__)

# --- Oracle Database Connection Settings ---
username = "ganesh_user"
password = "Ganesh123"
dsn = "localhost:1521/XEPDB1"  # hostname:port/service_name

# --- Home Page: Display All Users ---
@app.route('/')
def index():
    try:
        con = oracledb.connect(user=username, password=password, dsn=dsn)
        cur = con.cursor()
        cur.execute("SELECT id, name, email FROM users ORDER BY id")
        users = cur.fetchall()
        con.close()
        return render_template('index.html', users=users)
    except Exception as e:
        return f"❌ Database Error: {str(e)}"

# --- Add New User ---
@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']

    try:
        con = oracledb.connect(user=username, password=password, dsn=dsn)
        cur = con.cursor()
        cur.execute("INSERT INTO users (name, email) VALUES (:1, :2)", (name, email))
        con.commit()
        con.close()
    except Exception as e:
        return f"❌ Insert Error: {str(e)}"

    return redirect('/')

if __name__ == '__main__':
    print("✅ Flask app connected to Oracle Database (XEPDB1)!")
    app.run(debug=True)
