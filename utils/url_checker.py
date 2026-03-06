import re

SUSPICIOUS_TLDS = [".zip", ".xyz", ".top", ".tk"]
SHORTENERS = ["bit.ly", "tinyurl", "goo.gl"]

def extract_urls(text: str):
    return re.findall(r"https?://[^\s]+", text)

def url_risk_score(text: str) -> float:
    urls = extract_urls(text)
    if not urls:
        return 0.0

    risk = 0.0
    for url in urls:
        if any(short in url for short in SHORTENERS):
            risk += 0.4
        if any(url.endswith(tld) for tld in SUSPICIOUS_TLDS):
            risk += 0.4
        if "login" in url or "verify" in url:
            risk += 0.3

    return min(risk, 1.0)