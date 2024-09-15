from fastapi import FastAPI
from app.models import CheckInRequest, SentimentResponse, BiometricData, ChatRequest
from app.utils import analyze_text_sentiment, ai_chat_response
from app.db import create_db, add_user_checkin, add_biometric_data

app = FastAPI()

# Initialize database
create_db()

@app.post("/checkin", response_model=SentimentResponse)
async def analyze_sentiment(checkin: CheckInRequest):
    sentiment, insights, interventions = analyze_text_sentiment(checkin.input_text)
    add_user_checkin(checkin.user_id, sentiment)
    return SentimentResponse(sentiment=sentiment, insights=insights, interventions=interventions)

@app.post("/biometrics/{user_id}")
async def add_biometric(user_id: int, biometrics: BiometricData):
    add_biometric_data(user_id, biometrics.heart_rate, biometrics.sleep_duration)
    return {"status": "success"}

@app.post("/chat", response_model=dict)
async def chat_with_ai(request: ChatRequest):
    response = ai_chat_response(request.user_message)
    return {"response": response}
