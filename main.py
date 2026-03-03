from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from api.customerRouter import router as api_customer_router
from api.employeeRouter import router as api_employee_router
from api.salesRouter import router as api_sales_router
from api.textoRouter import router as api_openai_text
from api.visionRouter import router as api_openai_vision
from api.speech_router import router as api_openai_speech
from api.transcriptionRouter import router as api_openai_transcription


app = FastAPI()


templates = Jinja2Templates(directory="frontend/templates")


app.mount(
    "/static",
    StaticFiles(directory="frontend/static"),
    name="static"
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse(
        "chat.html",
        {"request": request}
    )

@app.get("/vision")
def vision_page(request: Request):
    return templates.TemplateResponse("vision.html", {"request": request})

@app.get("/speech")
def speech_page(request: Request):
    return templates.TemplateResponse("speech.html", {"request": request})

@app.get("/transcription")
def transcription_page(request: Request):
    return templates.TemplateResponse("transcription.html", {"request": request})

app.include_router(api_customer_router)
app.include_router(api_employee_router)
app.include_router(api_sales_router)
app.include_router(api_openai_text)
app.include_router(api_openai_vision)
app.include_router(api_openai_speech)
app.include_router(api_openai_transcription)