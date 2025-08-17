from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/matchmaking')
def matchmaking():
    return render_template('Matchmaking_UI.html')

@app.route('/profile')
def profile():
    return render_template('Profile.html')

@app.route('/simulator')
def simulator():
    return render_template('Simulator_UI.html')

@app.route('/training')
def training():
    return render_template('Training_UI.html')

if __name__ == '__main__':
    app.run(debug=True)