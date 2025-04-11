# 🎤 Text-to-Speech API (OpenAI GPT-4o Mini)

A simple FastAPI server that converts text to speech using OpenAI's `gpt-4o-mini-tts` model.  
You can customize voice, tone, speed, emotions, and more.

---

## 🚀 Endpoint
POST /text-to-speech/

**Base URL:**  
`https://texttospeech-z3ri.onrender.com/text-to-speech/`

---

## 🧾 Parameters (`form-data`)

| Name           | Type     | Required | Description                                   |
|----------------|----------|----------|-----------------------------------------------|
| `input_text`   | string   | ✅ yes   | Text to convert to speech                     |
| `voice`        | string   | ❌ no    | Voice name (default: `nova`)                  |
| `instructions` | string   | ❌ no    | How to speak — tone, emotion, style, etc.     |

---

## 🗣 Available Voices

`alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer`

🎧 Listen to samples: [openai.com/demos/text-to-speech](https://openai.com/demos/text-to-speech)

---

## 💬 Sample Instructions

- `Speak like a storyteller.`
- `Use a calm and warm tone.`
- `Whisper softly with emotion.`

---

## 🔁 Example Request (curl)

```bash
curl -X POST https://texttospeech-z3ri.onrender.com/text-to-speech/ \
  -F "input_text=Hello! I am your AI speaker." \
  -F "voice=coral" \
  -F "instructions=Speak in a cheerful and calm manner." \
  --output speech.mp3
```

---

## 📦 Response
Returns an .mp3 file (audio/mpeg).
