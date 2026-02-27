from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from openai import OpenAI

import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

router = APIRouter()


@router.post("/api/speech/generate")
async def generate_speech(body: dict):

    text = body["text"]

    def audio_generator():

        with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=text
        ) as response:

            for chunk in response.iter_bytes():

                yield chunk


    return StreamingResponse(
        audio_generator(),
        media_type="audio/mpeg",
        headers={
            "Content-Disposition": "inline; filename=audio.mp3"
        }
    )