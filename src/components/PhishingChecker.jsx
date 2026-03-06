import { useState } from "react";
import axios from "axios";

function PhishingChecker() {
  const [emailText, setEmailText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleCheck = async () => {
    setLoading(true);
    try {
      const res = await axios.post("http://127.0.0.1:8000/predict", {
        email_text: emailText,
      });
      setResult(res.data);
    } catch (err) {
      alert("Backend not reachable");
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center px-4">
      <div className="bg-white w-full max-w-xl rounded-lg shadow-lg p-6">
        <h1 className="text-2xl font-bold text-center text-indigo-600">
          Phishing Email Detection
        </h1>

        <textarea
          className="w-full mt-6 p-3 border rounded-md"
          rows="6"
          placeholder="Paste email content here..."
          value={emailText}
          onChange={(e) => setEmailText(e.target.value)}
        />

        <button
          onClick={handleCheck}
          className="w-full mt-4 bg-indigo-600 text-white py-2 rounded-md"
        >
          {loading ? "Checking..." : "Check Phishing"}
        </button>

        {result && (
          <div className="mt-6 p-4 bg-indigo-50 rounded-md">
            <p className="font-semibold">
              Status:{" "}
              <span className="text-red-600">{result.label}</span>
            </p>
            <p>Confidence: {result.confidence}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default PhishingChecker;