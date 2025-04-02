from fastapi import FastAPI, UploadFile, File, WebSocket
from fastapi.responses import JSONResponse
from .video_processor import process_video
from .database import init_db, save_detection, get_detections
import asyncio

app = FastAPI()

# WebSocket clients
connected_clients = set()

@app.on_event("startup")
async def startup_event():
    init_db()  # Initialize database on startup

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    video_path = f"uploads/{file.filename}"
    with open(video_path, "wb") as buffer:
        buffer.write(await file.read())
    
    # Process video and send updates via WebSocket
    results = await process_video(video_path, broadcast_progress)
    return JSONResponse(content={"message": "Video processed", "video_id": results["video_id"]})

@app.get("/detections/{video_id}")
async def fetch_detections(video_id: str):
    detections = get_detections(video_id)
    return JSONResponse(content=detections)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            await websocket.receive_text()  # Keep connection alive
    except Exception:
        connected_clients.remove(websocket)

async def broadcast_progress(message: dict):
    for client in connected_clients:
        await client.send_json(message)
