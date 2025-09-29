from flask import Flask, render_template, request

app = Flask(__name__)
patients = []
@app.route("/", methods=["GET", "POST"])
def patients_view():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        address = request.form["address"]
        patients.append({
            "name": name,
            "age": age,
            "gender": gender,
            "address": address
        })
    return render_template("patient.html", patients=patients)