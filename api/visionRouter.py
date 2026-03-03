from fastapi import APIRouter
from fastapi.responses import Response
from openai import OpenAI

import os
from dotenv import load_dotenv
import base64

load_dotenv()

router = APIRouter()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@router.post("/api/vision/generate")
def generate_image(data: dict):

    try:
        prompt = data.get("prompt", "")

        result = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )

        image_base64 = result.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)

        return Response(
            content=image_bytes,
            media_type="image/png"
        )

    except Exception as e:
        print("ERRO VISION:", e)
        return {"error": str(e)}