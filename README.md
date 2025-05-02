# 🛍️ AI-Powered Product Description Extractor & Narrator

This Python project uses Optical Character Recognition (OCR) to extract product information from images (e.g., e-commerce screenshots), generates an engaging description using a Hugging Face Large Language Model (LLM), and finally converts it into a natural-sounding voice using Hugging Face’s voice cloning API.

---

## 🚀 Features

- ✅ Extract product **name, price, color, size**, and **description** from an image.
- ✨ Generate a **clear and engaging product summary** using a Hugging Face LLM (`Mixtral-8x7B-Instruct-v0.1`).
- 🎙️ Convert the summary into **human-like speech** using Hugging Face’s **VoiceCloning-be/text-to-speech** space.
- 💬 Supports customization of voice, pitch, and speed.

---
```
OcrProject/
├── app/
│   ├── main.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── ocr_controller.py
│   └── services/
│       ├── __init__.py
│       └── ocr_service.py
├── .env
├── requirements.txt

```
⚙️ Key Components

/app/controllers/ocr_controller.py
Defines FastAPI router.
Handles file upload.
Calls service logic.

/app/services/ocr_service.py
extract_product_info: Uses regex on OCR text.
build_prompt: Creates LLM prompt.
expand_with_huggingface: Calls Mixtral-8x7B LLM.
speak_text_with_voicecloning: Uses Gradio TTS.
process_image_and_generate_description: Ties it all together.


```shell
uv pip install -r requirements.txt
uv run -- uvicorn app.main:app --reload
```