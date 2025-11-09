# Health Assistant - Disease Prediction App

## Overview
This is a Flask-based web application that provides disease prediction using pre-trained machine learning models. The app can predict three types of conditions:
1. **Diabetes** - Based on 8 medical features
2. **Heart Disease** - Based on 13 cardiovascular features
3. **Parkinson's Disease** - Based on 22 vocal features

## Project Structure
```
.
├── app.py                      # Main Flask application
├── templates/
│   └── index.html              # Frontend HTML with embedded CSS and JavaScript
├── diabetes_model.sav          # Pre-trained diabetes prediction model
├── heart_disease_model.sav     # Pre-trained heart disease prediction model
├── parkinsons_model.sav        # Pre-trained Parkinson's disease prediction model
├── *.ipynb                     # Jupyter notebooks for model training
└── requirements.txt            # Python dependencies
```

## Technology Stack
- **Backend**: Flask 3.1.2
- **ML Framework**: scikit-learn 1.7.2
- **Data Processing**: pandas, numpy
- **Production Server**: gunicorn
- **Python Version**: 3.11

## Features
- Single-page web interface with three prediction forms
- Real-time predictions via AJAX requests
- Pre-trained models loaded at startup for fast predictions
- Responsive design with gradient styling

## Development
The app runs on Flask's development server:
- **Host**: 0.0.0.0 (accessible from all interfaces)
- **Port**: 5000
- **Debug Mode**: Enabled in development

## Deployment
Configured for Replit's autoscale deployment using:
- **Production Server**: gunicorn with port reuse enabled
- **Deployment Type**: Autoscale (stateless web application)

## API Endpoints
- `GET /` - Main page with prediction forms
- `POST /predict/diabetes` - Diabetes prediction endpoint
- `POST /predict/heart` - Heart disease prediction endpoint
- `POST /predict/parkinsons` - Parkinson's disease prediction endpoint

## Notes
- The ML models were trained with scikit-learn 1.0.2 but work with version 1.7.2 (with compatibility warnings)
- All models use the SVC (Support Vector Classification) or Logistic Regression algorithms
- Input validation is handled client-side and server-side

## Recent Changes
- **2025-11-09**: Initial Replit setup
  - Configured Flask app for Replit environment (0.0.0.0:5000)
  - Fixed requirements.txt encoding issue
  - Set up workflow for Flask development server
  - Configured gunicorn for production deployment
  - Added Python .gitignore
