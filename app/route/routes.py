import os
import pickle
from flask import Blueprint, render_template, request

from app.model.predictor import predict_gpa, required_study_time

app_routes = Blueprint('app_routes', __name__)

# Get the absolute path to the model files
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Get current file's directory
MODEL_DIR = os.path.join(BASE_DIR, "../model")  # Move up to `app` then into `model`

gpa_model_path_model_path = os.path.join(MODEL_DIR, "gpa_model.pkl")

# Load models safely
try:
    with open(gpa_model_path_model_path, 'rb') as f:
        study_model = pickle.load(f)
except FileNotFoundError:
    print("Error: Model files not found. Ensure 'exam_model.pkl' and 'study_model.pkl' exist in 'app/model/'.")
    exam_model, study_model = None, None


@app_routes.route('/', methods=['GET', 'POST'])
def index():
    predicted_gpa_score = None
    error = None

    if request.method == 'POST':
        try:
            # Extract values and validate
            study_time_weekly = int(request.form['study_time_weekly'])
            absences = int(request.form['absences'])
            tutoring = int(request.form['tutoring'])

            # Check that all inputs are valid
            if not all(isinstance(i, int) for i in [study_time_weekly, absences, tutoring]):
                raise ValueError("All inputs must be valid integers.")
            
            # Predict the GPA
            predicted_gpa_score = predict_gpa(study_time_weekly, tutoring, absences)

        except ValueError as e:
            error = "Invalid input. Please enter numerical values."

    return render_template('index.html', predicted_gpa_score=predicted_gpa_score, error=error)
