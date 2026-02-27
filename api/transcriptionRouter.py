from fastapi import APIRouter, UploadFile, File
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@router.post("/api/transcription/generate")
async def transcribe_audio(file: UploadFile = File(...)):

    audio_bytes = await file.read()

    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=("audio.mp3", audio_bytes, file.content_type)
    )

    return {
        "text": transcription.text
    }