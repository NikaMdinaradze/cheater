from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class MessageRequest(BaseModel):
    message: str

class MessageResponse(BaseModel):
    response: str

@app.post("/", response_model=MessageResponse)
async def chat_with_gpt(request: MessageRequest):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": request.message}
        ]
    )
    reply = completion.choices[0].message["content"]
    return {"response": reply}

