from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Patient Management System</h1><p>This is your live homepage.</p>"

# Optional: Keep other routes below this if you add more later
@app.route('/patients')
def patients():
    return """
    <h2>Patient Records</h2>
    <ul>
        <li>Jane munene – Age 34 – Diabetes</li>
        <li>John waithaka – Age 45 – Hypertension</li>
        <li>Mary Wanjiru – Age 29 – Asthma</li>
    </ul>
    """