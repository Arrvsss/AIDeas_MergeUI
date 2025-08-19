from flask import Flask, render_template, request, jsonify, redirect, url_for
import os, json

app = Flask(__name__)

# make profile page the landing page
@app.route('/')
def index():
    return redirect(url_for('profile'))

@app.route('/matchmaking')
def matchmaking():
    return render_template('Matchmaking_UI.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/save_profile', methods=['POST'])
def save_profile():
    data = request.get_json() or {}
    os.makedirs('data', exist_ok=True)
    with open(os.path.join('data', 'profile.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return jsonify(success=True)

@app.route('/profile')
def profile():
    """
    If a saved profile exists on the server (data/profile.json) render a read-only view.
    Otherwise render the editable profile form.
    """
    profile_path = os.path.join('data', 'profile.json')
    if os.path.exists(profile_path):
        with open(profile_path, 'r', encoding='utf-8') as f:
            profile_data = json.load(f)
        return render_template('profile_view.html', profile=profile_data)
    # fallback: show the form page
    return render_template('Profile.html')

@app.route('/profile/edit')
def profile_edit():
    # Force showing the edit form
    return render_template('Profile.html')

@app.route('/profile/delete', methods=['POST'])
def profile_delete():
    profile_path = os.path.join('data', 'profile.json')
    try:
        if os.path.exists(profile_path):
            os.remove(profile_path)
    except Exception:
        pass
    return redirect(url_for('profile_edit'))

@app.route('/simulator')
def simulator():
    return render_template('Simulator_UI.html')

@app.route('/training')
def training():
    return render_template('Training_UI.html')

if __name__ == '__main__':
    app.run(debug=True)