from fastapi import APIRouter
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter()


@router.post("/api/text/chat")
async def chat(data: dict):

    message = data["message"]

    moderation = client.moderations.create(
        model="omni-moderation-latest",
        input=message
    )

    if moderation.results[0].flagged:
        return {
            "response": "Mensagem bloqueada pela moderação."
        }

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return {
        "response": response.choices[0].message.content
    }