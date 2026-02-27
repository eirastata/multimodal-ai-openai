from fastapi import FastAPI

from api.customerRouter import router as api_customer_router
from api.employeeRouter import router as api_employee_router
from api.salesRouter import router as api_sales_router
from api.textoRouter import router as api_openai_text
from api.visionRouter import router as api_openai_vision 
from api.speech_router import router as api_openai_speech 
from api.transcriptionRouter import router as api_openai_transcription

app = FastAPI()


app.include_router(api_customer_router)
app.include_router(api_employee_router)
app.include_router(api_sales_router)
app.include_router(api_openai_text)
app.include_router(api_openai_vision)
app.include_router(api_openai_speech)
app.include_router(api_openai_transcription)