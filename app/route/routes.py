from flask import Blueprint, render_template, request
from app.model.predictor import predict_gpa, required_study_time

app_routes = Blueprint('app_routes', __name__)
@app_routes.route('/', methods=['GET', 'POST'])
def index():
    predicted_value = None
    error = None
    prediction_type = "gpa"

    if request.method == 'POST':
        try:
            prediction_type = request.form['prediction_type']
            absences = float(request.form['absences'])
            tutoring = float(request.form['tutoring'])
            parent_support = request.form['parent_support']
            extra_activities = request.form['extra_activities']
            sport = request.form['sport']
            music = request.form['music']

            print(f"absences: {absences}, tutoring: {tutoring}")
            print(f"parent_support: {parent_support}, extra_activities: {extra_activities}")
            print(f"sport: {sport}, music: {music}")

            if absences < 0:
                return render_template('index.html', predicted_value=None, error="Please put absences greater than 0",
                                       prediction_type=prediction_type)
            if prediction_type == "gpa":
                study_time_weekly = float(request.form['study_time_weekly'])
                if study_time_weekly < 0:
                    return render_template('index.html', predicted_value=None, error="Please put study time greater than 0",
                                           prediction_type=prediction_type)
                predicted_value = predict_gpa(study_time_weekly, tutoring, absences)
            elif prediction_type == "study_hours":
                expected_gpa = float(request.form['expected_gpa'])
                if expected_gpa < 0.0:
                    return render_template('index.html', predicted_value=None, error="Please put GPA greater than 0",)
                if expected_gpa > 4.0:
                    return render_template('index.html', predicted_value=None, error="Please put GPA less than or equal to 4",
                                           prediction_type=prediction_type)
                predicted_value = required_study_time(expected_gpa, tutoring, absences)
            else:
                error = "Invalid prediction type."

        except ValueError:
            error = "Invalid input. Please enter numerical values."

    return render_template('index.html', predicted_value=predicted_value, error=error, prediction_type=prediction_type)