from pydantic import BaseModel
from typing import List, Dict

class CheckInRequest(BaseModel):
    user_id: int
    input_text: str

class SentimentResponse(BaseModel):
    sentiment: str
    insights: List[str]
    interventions: List[str]

class BiometricData(BaseModel):
    heart_rate: int
    sleep_duration: float

class ChatRequest(BaseModel):
    user_message: str
