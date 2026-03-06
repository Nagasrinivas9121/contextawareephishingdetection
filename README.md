Context Flow Based Phishing Email Identification using NLP
Overview

Phishing attacks are one of the most common cybersecurity threats where attackers send fraudulent emails to trick users into revealing sensitive information such as passwords, banking credentials, and personal data. Traditional detection methods rely on blacklists and rule-based systems, which are often ineffective against newly generated phishing attacks.

This project proposes a Context Flow Based Phishing Email Detection System using Natural Language Processing (NLP). The system analyzes the contextual meaning of email text and identifies suspicious patterns to classify emails as Phishing or Legitimate.

The solution combines transformer-based NLP models, URL feature analysis, and header inspection to generate a phishing risk score.

Features

Context-aware phishing email detection using NLP

URL risk analysis for suspicious links

Hybrid phishing detection model

REST API using FastAPI

Interactive frontend interface

Real-time phishing risk scoring

System Architecture

The system follows a layered architecture:

User submits email content

Backend API receives the request

Preprocessing cleans the email text

NLP model analyzes the email context

URL analyzer checks suspicious links

Risk score is calculated

Final classification result is returned

Tech Stack
Technology	Purpose
Python	Backend development
FastAPI	REST API framework
PyTorch	Deep learning framework
Transformers (HuggingFace)	NLP models
React.js	Frontend interface
Tailwind CSS	UI styling



Project Structure
phishing-detection-nlp/
│
├── backend/
│   ├── main.py
│   ├── train_distilroberta.py
│   ├── utils/
│   │   ├── url_checker.py
│   │   └── header_checker.py
│   └── phishing-model/
│
├── frontend/
│   ├── src/
│   ├── components/
│   └── App.js
│
├── dataset/
│   └── phishing_data.csv
│
├── docs/
│   └── project_report.pdf
│
└── README.md



Installation
Clone the Repository
git clone https://github.com/yourusername/phishing-detection-nlp.git
cd phishing-detection-nlp
Backend Setup

Install dependencies:

pip install fastapi uvicorn torch transformers datasets

Run the API server:

uvicorn main:app --reload

API will run on:

http://127.0.0.1:8000

Swagger API docs:

http://127.0.0.1:8000/docs
API Example
Request
POST /predict

Request Body:

{
 "email_text": "Your account has been suspended. Click here to verify."
}
Response
{
 "verdict": "Phishing",
 "risk_score": 0.82,
 "signals": {
   "text_risk": 0.91,
   "url_risk": 0.72,
   "header_risk": 0.60
 }
}
Model Training

Train the NLP model using:

python train_distilroberta.py

The trained model will be saved in:

phishing-model/
Dataset

The model is trained using publicly available phishing email datasets including:

Kaggle Phishing Email Dataset

PhishTank URL Database

Enron Email Dataset

Results
Metric	Value
Accuracy	95%
Precision	93%
Recall	94%
F1 Score	93.5%
Future Improvements

Browser extension for phishing detection

Real-time email gateway integration

Larger dataset training

Advanced transformer models (BERT / RoBERTa)

Contributors

Kaki Supriya

Kondraju Kavya

Konidala Keerthi

Nakkala Latha Sri

Department of Computer Science and Engineering
St. Mary's Group of Institutions, Guntur
License
This project is developed for academic purposes as part of the B.Tech Project Work (CSE – Artificial Intelligence and Data Science).

This project is developed for academic purposes as part of the B.Tech Project Work (CSE – Artificial Intelligence and Data Science).
