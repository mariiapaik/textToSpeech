from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from openai import OpenAI
from pathlib import Path
import uuid
import os

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/text-to-speech/")
async def text_to_speech(
    input_text: str = Form(...),
    voice: str = Form("nova"),
    instructions: str = Form("Speak in a natural tone.")
):
    filename = f"{uuid.uuid4()}.mp3"
    speech_file_path = Path("output") / filename
    speech_file_path.parent.mkdir(parents=True, exist_ok=True)

    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice=voice,
        input=input_text,
        instructions=instructions
    ) as response:
        response.stream_to_file(speech_file_path)

    return FileResponse(
        path=speech_file_path,
        media_type="audio/mpeg",
        filename="speech.mp3"
    )
