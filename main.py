from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import SentimentClassification
import uvicorn

try:
    classifier = SentimentClassification("./config.yaml")
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

app = FastAPI(
    title="Multilingual Sentiment Analysis API",
    description="API phân tích cảm xúc đa ngôn ngữ sử dụng mô hình từ Hugging Face.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

class TextInput(BaseModel):
    text: str

@app.get('/')
async def root():
    return {
        "name": "Multilingual Sentiment Analysis API",
        "model": "tabularisai/multilingual-sentiment-analysis",
        "description": "Gửi POST request chứa văn bản tới /predict để phân tích cảm xúc (Positive, Negative, Neutral,...)."
    }

@app.get('/health')
async def health_check():
    return {"status": "ok", "message": "API is up and running!"}

@app.post('/predict')
async def predict_sentiment(request: TextInput):
    if not request.text or not request.text.strip():
        raise HTTPException(status_code=400, detail="Văn bản đầu vào không được để trống.")
    
    try:
        result = classifier.predict(request.text)
        return {
            "success": True,
            "input_text": request.text,
            "prediction": result["label"],
            "confidence_score": result["confidence"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi hệ thống trong quá trình phân tích: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)