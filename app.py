from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Patient Management System</h1><p>This is your live homepage.</p>"

# Optional: Keep other routes below this if you add more later