
from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("model.joblib")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    gender = request.form["Gender"]
    age = float(request.form["Age"])
    height = float(request.form["Height"])
    weight = float(request.form["Weight"])
    duration = float(request.form["Duration"])
    heart_rate = float(request.form["Heart_Rate"])
    body_temp = float(request.form["Body_Temp"])

    # Calculate BMI
    bmi = weight / ((height / 100) ** 2)

    # Prepare input data
    input_data = pd.DataFrame([{
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "Duration": duration,
        "Heart_Rate": heart_rate,
        "Body_Temp": body_temp,
        "BMI": bmi
    }])

    # Predict calories
    prediction = model.predict(input_data)[0]

    return render_template(
        "index.html",
        prediction=round(float(prediction), 2)
    )


if __name__ == "__main__":
    app.run(debug=True)
