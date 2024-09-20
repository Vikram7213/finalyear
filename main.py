from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

# Initialize the Flask application
app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('random_forest_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    data = request.json
    df = pd.DataFrame(data)
    pod_name = os.getenv('HOSTNAME')
    print(f"Pod Name: {pod_name}")
    # Assuming the data is in the same format as the model's training data
    predictions = model.predict(df)
    return jsonify(
        {
        'predictions':predictions.tolist(), 
        'pod_name': pod_name
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
