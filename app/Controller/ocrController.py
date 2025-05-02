from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.Services.OcrService import process_image_and_generate_description
import shutil, os

router = APIRouter()
UPLOAD_PATH = "temp_uploaded_image.jpg"

@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    with open(UPLOAD_PATH, "wb") as f:
        shutil.copyfileobj(file.file, f)
    try:
        result = process_image_and_generate_description(UPLOAD_PATH)
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.remove(UPLOAD_PATH)
