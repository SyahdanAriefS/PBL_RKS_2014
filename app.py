from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home.html')
def home_html():
    return render_template('home.html')

@app.route('/location.html')
def location_html():
    return render_template('location.html')

@app.route('/network.html')
def network_html():
    return render_template('network.html')

@app.route('/history.html')
def history_html():
    return render_template('history.html')

@app.route('/device.html')
def device_html():
    return render_template('device.html')

if __name__ == '__main__':
    app.run(debug=True)
