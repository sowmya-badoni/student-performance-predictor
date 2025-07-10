# Student Performance Predictor

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Step 1: Load the dataset
df = pd.read_csv("student_performance_dataset.csv")

# Step 2: Convert "Result" column to numbers
df['Result'] = df['Result'].map({'Pass': 1, 'Fail': 0})

# Step 3: Split into features and target
X = df[['Hours_Studied', 'Attendance', 'Internal_Marks']]
y = df['Result']

# Step 4: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 6: Predict and check accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("✅ Model Accuracy:", accuracy)

# Step 7: Save the model
joblib.dump(model, "model.pkl")
print("✅ Model saved as model.pkl")
