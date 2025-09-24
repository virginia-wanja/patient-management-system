from flask import Flask, render_template, request

app = Flask(__name__)
patients = []

@app.route('/', methods=['GET', 'POST'])
def patients_view():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        condition = request.form['condition']
        patients.append({"name": name, "age": age, "condition": condition})
    return render_template('patients.html', patients=patients)
