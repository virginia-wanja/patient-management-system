from flask import Flask, render_template, request

app = Flask(__name__)
patients = []
@app.route("/", methods=["GET", "POST"])
def patients_view():
    selected_condition = None
    filtered_patients = patients
    if request.method == "POST":
        selected_condition = request.form["condition"]
        filtered_patients = [patient for patient in patients if patient["condition"] == selected_condition]
    return render_template("patient.html", patients=filtered_patients)
