# ORION – Multimodal AI Assistant

Fullstack multimodal AI system integrating Large Language Models, Image Generation, Text-to-Speech and Speech-to-Text using FastAPI and OpenAI.

This project demonstrates how to build a structured AI application with modular backend architecture and a custom frontend interface.

---

## Overview

ORION is a multimodal assistant capable of handling different types of input and output:

- Conversational AI (Chat)
- AI Image Generation
- Text-to-Speech (TTS)
- Speech-to-Text (STT)

The system is designed following clean architecture principles, separating each AI capability into independent routers.

---

## Architecture

The backend is structured using modular routers to improve scalability and maintainability.

```
api/
 ├── textoRouter.py
 ├── speech_router.py
 ├── transcriptionRouter.py
 ├── visionRouter.py
frontend/
 ├── templates/
 │    ├── index.html
 │    ├── chat.html
 │    ├── vision.html
 │    ├── speech.html
 │    └── transcription.html
 └── static/
main.py
```

Each feature is exposed through a dedicated API endpoint, while the frontend consumes these endpoints via asynchronous fetch requests.

---

## Technologies

- Python
- FastAPI
- OpenAI API
- HTML5
- Bootstrap
- JavaScript (Fetch API)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/eirastata/multimodal-ai-openai.git
cd multimodal-ai-openai
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate the environment:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is not available:

```bash
pip install fastapi uvicorn openai python-dotenv
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key_here
```

---

## Running the Application

Start the server with:

```bash
uvicorn main:app --reload --port 9000
```

Access in your browser:

```
http://127.0.0.1:9000
```

---

## API Endpoints

- POST /api/text/chat
- POST /api/vision/generate
- POST /api/speech/generate
- POST /api/transcription/generate

---

## Design Decisions

- Modular FastAPI routers for separation of concerns
- Streaming and binary responses for media handling
- Base64 decoding for image generation
- Clean frontend-backend separation
- Environment variable protection for API credentials

---

## Purpose

This project demonstrates practical integration of multimodal AI capabilities into a structured fullstack application, suitable for portfolio presentation and technical evaluation.

---

## License

MIT License
