from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from openai import OpenAI

import os
from dotenv import load_dotenv
import base64
import io

load_dotenv()

router = APIRouter()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@router.post("/api/vision/generate")
def generate_image(data: dict):

    prompt = data.get("prompt", "")

    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )

    image_base64 = result.data[0].b64_json

    image_bytes = base64.b64decode(image_base64)

    return StreamingResponse(
        io.BytesIO(image_bytes),
        media_type="image/png",
        headers={
            "Content-Disposition": "inline; filename=image.png"
        }
    )