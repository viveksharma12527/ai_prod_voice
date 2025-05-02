# import os
# import re
# import shutil
# import requests
# from gradio_client import Client, handle_file
#
# def extract_product_info(text: str) -> dict:
#     clean = text.replace("\n", " ").replace("  ", " ").strip()
#
#     product = re.search(r"\b([A-Z\s]{5,})\b(?=.*(€|\$|\d{2,3}[.,]\d{2]))", clean)
#     price = re.search(r"(€|\$)?\s?(\d{2,3}[.,]\d{2})", clean)
#     color = re.search(r"COLOR[:\-]?\s*([A-Za-z\s]+?)(?=\s[A-Z]{2,}|SIZE|SELECT|ADD|CHECK|$)", clean, re.IGNORECASE)
#     sizes = re.findall(r"\b(2[8-9]|3[0-9]|4[0-4])\b", clean)
#     desc = re.search(r"Shorts\s*-\s*(.*?)(?=SIZE\s+GUIDE|ADD|CHECK|$)", clean, re.IGNORECASE)
#
#     return {
#         "Product Name": re.sub(r"^(O|0)\s+", "", product.group(1).title().strip()) if product else "Not found",
#         "Price": f"{price.group(1) or ''}{price.group(2)}" if price else "Not found",
#         "Color": color.group(1).title().strip() if color else "Not found",
#         "Sizes Available": sorted(set(sizes)) if sizes else ["Not found"],
#         "Description": desc.group(0).strip() if desc else "Not available"
#     }
#
# def build_prompt(summary: dict) -> str:
#     return (
#         f"Product Name: {summary['Product Name']}\n"
#         f"Price: {summary['Price']}\n"
#         f"Color: {summary['Color']}\n"
#         f"Sizes Available: {', '.join(summary['Sizes Available'])}\n"
#         f"Description: {summary['Description']}\n\n"
#         f"Make it engaging and clear for online shoppers."
#     )
#
# def expand_with_huggingface(prompt: str, hf_token: str) -> str:
#     api_url = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
#     headers = {"Authorization": f"Bearer {hf_token}", "Content-Type": "application/json"}
#     payload = {"inputs": prompt, "parameters": {"max_new_tokens": 200}}
#
#     response = requests.post(api_url, headers=headers, json=payload)
#     if response.status_code == 200:
#         return response.json()[0]["generated_text"].strip()
#     raise RuntimeError(f"HF API error {response.status_code}: {response.text}")
#
# def speak_text_with_voicecloning(text: str, voice: str, output_path: str = "voice.wav"):
#     client = Client("VoiceCloning-be/text-to-speech")
#     result = client.predict(
#         text=text,
#         voice=voice,
#         rate=2,
#         pitch=2,
#         api_name="/predict"
#     )
#
#     audio_url = result[0]
#     if audio_url.startswith("/"):
#         shutil.copy(audio_url, output_path)
#     else:
#         r = requests.get(audio_url)
#         with open(output_path, "wb") as f:
#             f.write(r.content)
#
#     os.system(f"afplay {output_path}")
#
# def main():
#     image_path = "/Users/vivek/PycharmProjects/OcrProject/image.jpg"
#     hf_token = ""
#
#     if not os.path.exists(image_path):
#         print("❌ Image not found.")
#         return
#
#     client = Client("artificialguybr/Surya-OCR")
#     _, _, text = client.predict(
#         image=handle_file(image_path),
#         langs="en",
#         api_name="/ocr_workflow"
#     )
#
#     summary = extract_product_info(text)
#     print("\n🧠 Product Summary")
#     for k, v in summary.items():
#         print(f"{k}: {v}")
#
#     prompt = build_prompt(summary)
#     description = expand_with_huggingface(prompt, hf_token)
#
#     print("\n📝 Expanded Description:\n" + description)
#
#     speak_text_with_voicecloning(description, voice="en-US-JennyNeural - en-US (Female)")
#
# if __name__ == "__main__":
#     main()



from fastapi import FastAPI
from app.Controller import ocrController  # Use singular `Controller`, not `controllers`

app = FastAPI()

app.include_router(ocrController.router)
