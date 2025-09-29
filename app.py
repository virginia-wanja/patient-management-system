from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///patients.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))
    address = db.Column(db.String(200))

# Create the database tables once
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def patients_view():
    if request.method == "POST":
        new_patient = Patient(
            name=request.form["name"],
            age=request.form["age"],
            gender=request.form["gender"],
            address=request.form["address"]
        )
        db.session.add(new_patient)
        db.session.commit()
    patients = Patient.query.all()
    return render_template("patient.html", patients=patients)
if __name__ == "__main__":
    app.run(debug=True)