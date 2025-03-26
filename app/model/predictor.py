import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression 

# Load dataset
df = pd.read_csv("Student_performance_data.csv")
print(f"✅ Dataset loaded successfully: {df.shape[0]} rows and {len(df.columns)} columns.")

def multiple_regression_model():
    X = df[['StudyTimeWeekly', 'Tutoring', 'Absences']]
    y = df['GPA']
    
    # Fit the model using Linear Regression
    model = LinearRegression()
    model.fit(X, y)
    
    # Get the model coefficients
    b0 = model.intercept_ 
    b1, b2, b3 = model.coef_
    
    # model equation
    print(f"Model: GPA = {b0:.4f} + {b1:.4f} * StudyTimeWeekly + {b2:.4f} * Tutoring + {b3:.4f} * Absences")
    
    # Predict the GPA
    y_pred = model.predict(X)
    
    # Calculate R-squared and Mean Squared Error
    r_squared = model.score(X, y)
    mse = np.mean((y - y_pred)**2)

    print(f"R-squared: {r_squared:.4f}")
    print(f"Mean Squared Error: {mse:.4f}")

    return b0, b1, b2, b3

b0, b1, b2, b3 = multiple_regression_model()

def predict_gpa(study_time, tutoring, absences):
    predicted_gpa = b0 + b1 * study_time + b2 * tutoring + b3 * absences
    if predicted_gpa > 4.0:
        return 4.0
    elif predicted_gpa < 0.0:
        return 0.0
    return round(predicted_gpa, 2)

def required_study_time(expected_gpa, tutoring=0, absences=0):
    required_study_time = (expected_gpa - b0 - b2 * tutoring - b3 * absences) / b1
    if required_study_time < 0:
        return 0.0
    return round(required_study_time,2)