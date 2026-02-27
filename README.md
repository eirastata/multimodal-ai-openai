# Multimodal AI API using FastAPI and OpenAI

This project is a Multimodal AI API built with FastAPI and OpenAI, capable of handling multiple types of inputs:

## Features

* Text generation (chat)
* Image generation
* Speech generation (Text-to-Speech)
* Audio transcription (Speech-to-Text)
* Modular architecture using FastAPI routers

## Technologies

* Python
* FastAPI
* OpenAI API
* Uvicorn
* dotenv

## Project Structure

api/

* textoRouter.py
* visionRouter.py
* speech_router.py
* transcriptionRouter.py

main.py

## How to run

Create virtual environment:

python -m venv venv

Activate:

venv\Scripts\activate

Install dependencies:

pip install fastapi uvicorn openai python-dotenv python-multipart

Run server:

uvicorn main:app --reload

Open:

http://127.0.0.1:8000/docs

## Author

Tamine Eiras
