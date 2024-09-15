from transformers import pipeline
import openai

# Sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_text_sentiment(input_text: str):
    result = sentiment_pipeline(input_text)
    sentiment = result[0]['label']
    if sentiment == "NEGATIVE":
        insights = ["You seem stressed."]
        interventions = ["Try a mindfulness exercise", "Take deep breaths"]
    else:
        insights = ["You're doing fine today!"]
        interventions = ["Keep up the good work", "Enjoy some downtime"]
    return sentiment, insights, interventions

# OpenAI GPT for chat
openai.api_key = "your-api-key"

def ai_chat_response(user_message: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    return response.choices[0].message['content']
