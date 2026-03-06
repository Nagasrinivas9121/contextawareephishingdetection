def header_risk_score(headers: dict) -> float:
    risk = 0.0

    if headers.get("spf") == "fail":
        risk += 0.4
    if headers.get("dkim") == "fail":
        risk += 0.3
    if headers.get("dmarc") == "fail":
        risk += 0.3

    sender = headers.get("from", "")
    reply_to = headers.get("reply_to", "")

    if reply_to and sender and reply_to not in sender:
        risk += 0.4

    return min(risk, 1.0)