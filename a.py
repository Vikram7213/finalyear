import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import joblib
# Load the dataset
data = pd.read_csv('station_day.csv')

# Drop rows with missing target values
data = data.dropna(subset=['AQI', 'AQI_Bucket'])

# Convert AQI_Bucket to numeric labels
label_encoder = LabelEncoder()
data['AQI_Bucket'] = label_encoder.fit_transform(data['AQI_Bucket'])

# Drop columns that are not features or target
data = data.drop(['StationId', 'Date'], axis=1)

# Define features and target
X = data.drop('AQI_Bucket', axis=1)
y = data['AQI_Bucket']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training data shape: {X_train.shape}")
print(f"Testing data shape: {X_test.shape}")


print("Model training complete and saved.")

# Load the model
clf = joblib.load('random_forest_model.pkl')

# Predict on the test set
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=label_encoder.classes_)

print(f"Model Accuracy: {accuracy}")
print("Classification Report:")
print(report)

