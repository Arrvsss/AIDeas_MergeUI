from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/matchmaking')
def matchmaking():
    return render_template('Matchmaking_UI.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # Pass submitted form data back to template to retain inputs
        return render_template('profile.html', form_data=request.form)
    return render_template('profile.html', form_data={})

@app.route('/simulator')
def simulator():
    return render_template('Simulator_UI.html')

@app.route('/training')
def training():
    return render_template('Training_UI.html')

if __name__ == '__main__':
    app.run(debug=True)
