
# Calorie Burn Prediction Using Machine Learning

## Project Overview
This project uses Machine Learning regression algorithms to predict the number of calories burnt based on user information and physical activity parameters.

The project also includes a Flask web application that allows users to enter their details and receive calorie burn predictions.

## Features
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Multiple regression model development and evaluation
- Best model selection
- Interactive web application using Flask
- Real-time prediction through user inputs

## Input Features
- Gender
- Age
- Height
- Weight
- Exercise Duration
- Heart Rate
- Body Temperature
- BMI

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Flask
- HTML
- CSS
- Joblib

## Project Structure
```text
calorie-burn-prediction/
│
├── app.py
├── model.joblib
├── metrics.json
├── calorie.ipynb
├── app.ipynb
├── calories.csv
├── requirements.txt
├── README.md
├── .gitignore
│
└── templates/
    └── index.html
```

## How to Run the Project

1. Clone the repository.
2. Install the required Python libraries.
3. Run the Flask application.

```bash
pip install -r requirements.txt
python app.py
```

4. Open your browser and visit:

http://127.0.0.1:5000/

## Project Objective
To develop a Machine Learning-based application that estimates calories burnt using physical activity and personal input parameters.
