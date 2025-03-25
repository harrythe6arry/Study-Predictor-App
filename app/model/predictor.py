import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import gdown

# Step 1: Download the dataset from Google Drive
file_id = "1wR7emkfTjEfAWzgmxn_-eKLZ6q989BNN"
gdown.download(f"https://drive.google.com/uc?id={file_id}", "Student_performance_data.csv", quiet=False)

# Step 2: Load dataset
df = pd.read_csv("Student_performance_data.csv")
print(f"✅ Dataset loaded successfully: {df.shape[0]} rows and {len(df.columns)} columns.")

# Define project paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(BASE_DIR, "../../")
MODEL_DIR = os.path.join(BASE_DIR, "../model")

os.makedirs(MODEL_DIR, exist_ok=True)

# Features and target variable
X = df[['StudyTimeWeekly', 'Absences', 'Tutoring', 'Sports', 'Music']]
y_gpa = df['GPA']

# Train-test split
X_train, X_test, y_train_gpa, y_test_gpa = train_test_split(X, y_gpa, test_size=0.2, random_state=42)

# Train the GPA prediction model
gpa_model = LinearRegression()
gpa_model.fit(X_train, y_train_gpa)



# Save the trained model
gpa_model_path = os.path.join(MODEL_DIR, "gpa_model.pkl")

with open(gpa_model_path, 'wb') as f:
    pickle.dump(gpa_model, f)

print(f"✅ Model trained and saved successfully at: {gpa_model_path}")
