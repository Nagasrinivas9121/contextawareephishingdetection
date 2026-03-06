from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os

from utils.url_checker import url_risk_score
from utils.header_checker import header_risk_score

# ===============================
# App Initialization
# ===============================
app = FastAPI(title="Hybrid Phishing Detection API")

# ===============================
# API LIVE / HEALTH CHECK
# ===============================
@app.get("/")
def api_live():
    return {
        "status": "API is LIVE",
        "service": "Hybrid Phishing Detection",
        "model": "Fine-Tuned DistilRoBERTa",
        "version": "1.1.0"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

# ===============================
# 🔥 Load FINE-TUNED MODEL (SAFE)
# ===============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "phishing-model")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

model.eval()

# ===============================
# Request Schema
# ===============================
class EmailRequest(BaseModel):
    email_text: str
    headers: dict | None = None

# ===============================
# Prediction Endpoint
# ===============================
@app.post("/predict")
def predict(data: EmailRequest):

    # 1️⃣ Context-aware NLP risk
    inputs = tokenizer(
        data.email_text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256
    )

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)

    text_risk = probs[0][1].item()  # phishing probability

    # 2️⃣ URL intelligence risk
    url_risk = url_risk_score(data.email_text)

    # 3️⃣ Header analysis risk
    header_risk = (
        header_risk_score(data.headers)
        if data.headers else 0.0
    )

    # 4️⃣ Final weighted risk score
    final_risk = round(
        (0.5 * text_risk) +
        (0.3 * url_risk) +
        (0.2 * header_risk),
        3
    )

    verdict = "Phishing" if final_risk >= 0.6 else "Legitimate"

    return {
        "verdict": verdict,
        "risk_score": final_risk,
        "signals": {
            "text_risk": round(text_risk, 3),
            "url_risk": round(url_risk, 3),
            "header_risk": round(header_risk, 3)
        }
    }