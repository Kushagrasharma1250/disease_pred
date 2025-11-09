from flask import Flask, request, jsonify, render_template
import os
import pickle

app = Flask(__name__)

# Load models
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/parkinsons_model.sav', 'rb'))

@app.route('/')
def home():
    return "Health Assistant API is running!"

@app.route('/predict/diabetes', methods=['POST'])
def predict_diabetes():
    data = request.json
    features = [float(data[key]) for key in [
        'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
        'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
    ]]
    prediction = diabetes_model.predict([features])[0]
    result = 'The person is diabetic' if prediction == 1 else 'The person is not diabetic'
    return jsonify({'prediction': result})

@app.route('/predict/heart', methods=['POST'])
def predict_heart():
    data = request.json
    features = [float(data[key]) for key in [
        'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
        'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
    ]]
    prediction = heart_disease_model.predict([features])[0]
    result = 'The person is having heart disease' if prediction == 1 else 'The person does not have any heart disease'
    return jsonify({'prediction': result})

@app.route('/predict/parkinsons', methods=['POST'])
def predict_parkinsons():
    data = request.json
    features = [float(data[key]) for key in [
        'fo', 'fhi', 'flo', 'Jitter_percent', 'Jitter_Abs', 'RAP', 'PPQ', 'DDP',
        'Shimmer', 'Shimmer_dB', 'APQ3', 'APQ5', 'APQ', 'DDA', 'NHR', 'HNR',
        'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
    ]]
    prediction = parkinsons_model.predict([features])[0]
    result = "The person has Parkinson's disease" if prediction == 1 else "The person does not have Parkinson's disease"
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)