import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Student_performance_data.csv")
print(f"✅ Dataset loaded successfully: {df.shape[0]} rows and {len(df.columns)} columns.")


ind_var =  ['ParentalSupport', 'StudyTimeWeekly', 'Absences', 'Tutoring', 'Sports', 'Music', 'Extracurricular']

def multiple_regression_model():
    X = df[ind_var]
    y = df['GPA']

    model = LinearRegression()
    model.fit(X, y)

    b0 = model.intercept_
    coeffs = model.coef_

    equation = f"GPA = {b0:.4f}"
    for factor, coef in zip(ind_var, coeffs):
        equation += f" + ({coef:.4f} * {factor})"
    print("Model Equation:")
    print(equation)

    y_pred = model.predict(X)
    r_squared = model.score(X, y)
    mse = np.mean((y - y_pred) ** 2)

    print(f"R-squared: {r_squared:.4f}")
    print(f"Mean Squared Error: {mse:.4f}")

    return b0, coeffs

b0, coeffs = multiple_regression_model()

coeffs = np.round(coeffs, 2)
b0 = round(b0, 2)

def predict_gpa(study_time, tutoring, absences, parental_support=0,
                extracurricular=0, sports=0, music=0):
    predicted_gpa = (b0 +
                     coeffs[0] * parental_support +
                     coeffs[1] * study_time +
                     coeffs[2] * absences +
                     coeffs[3] * tutoring +
                     coeffs[4] * sports +
                     coeffs[5] * music +
                     coeffs[6] * extracurricular)
    print(predicted_gpa)
    if predicted_gpa > 4.0:
        predicted_gpa = 4.0
    elif predicted_gpa < 0.0:
        predicted_gpa = 0.0

    return round(predicted_gpa, 2)


def required_study_time(expected_gpa, tutoring=0, absences=0, parental_support=0,
                        extracurricular=0, sports=0, music=0):
    required_study_time = (expected_gpa - (b0 +
                                           coeffs[0] * parental_support +
                                           coeffs[2] * absences +
                                           coeffs[3] * tutoring +
                                           coeffs[4] * sports +
                                           coeffs[5] * music +
                                           coeffs[6] * extracurricular)) / coeffs[1]
    if required_study_time < 0:
        return 0.0
    return round(required_study_time, 2)