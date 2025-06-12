from flask import Flask, render_template, send_from_directory

app = Flask(
    __name__,
    static_folder='static',  # Folder untuk file statis (gambar, css, js)
    template_folder='template'  # Folder untuk template HTML
)

# Route untuk halaman dashboard
@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Route untuk halaman victim
@app.route('/victim')
def victim():
    return render_template('victim.html')

# Route untuk halaman device
@app.route('/device')
def device():
    return render_template('device.html')

# Route untuk halaman settings
@app.route('/settings')
def settings():
    return render_template('settings.html')

# Route untuk servis file statik (jika diperlukan spesifik)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# Jalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)
