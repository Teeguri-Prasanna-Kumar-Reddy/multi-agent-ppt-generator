import os
import shutil
from typing import List, Optional

from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse

from graph.ppt_graph import run_ppt_agent

app = FastAPI(title="GenAI PPT Agent")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "output"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


# -----------------------------
# Generate PPT Endpoint
# -----------------------------
@app.post("/generate-ppt")
async def generate_ppt(
    topic: str = Form(...),
    files: Optional[List[UploadFile]] = File(None),
):
    saved_files = []

    if files:
        for file in files:
            safe_name = os.path.basename(file.filename or "upload.bin")
            file_path = os.path.join(UPLOAD_DIR, safe_name)

            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            saved_files.append(file_path)

    result = run_ppt_agent({
        "topic": topic,
        "documents": saved_files,
    })

    ppt_path = result.get("ppt_path")
    if not ppt_path or not os.path.exists(ppt_path):
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": "PPT generation failed. Please check the backend logs.",
            },
        )

    return {
        "status": "success",
        "ppt_path": ppt_path,
        "download_url": f"/download?file={os.path.basename(ppt_path)}",
    }


# -----------------------------
# Download Endpoint
# -----------------------------
@app.get("/download")
def download(file: str):
    file_path = os.path.join(OUTPUT_DIR, file)

    if not os.path.exists(file_path):
        return {"error": "file not found"}

    return FileResponse(
        file_path,
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        filename=file,
    )


# -----------------------------
# Health Check
# -----------------------------
@app.get("/")
def health():
    return {"message": "GenAI PPT Agent Running"}