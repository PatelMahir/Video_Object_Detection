import cv2
from ultralytics import YOLO
from .database import save_detection
import uuid
import os

async def process_video(video_path: str, broadcast_progress):
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(video_path)
    video_id = str(uuid.uuid4())
    frame_number = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLO detection
        results = model(frame)
        boxes = results[0].boxes.xyxy.tolist()  # Bounding boxes
        scores = results[0].boxes.conf.tolist()  # Confidence scores
        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0

        person_boxes = [box for i, box in enumerate(boxes) if results[0].boxes.cls[i] == 0]
        person_scores = [score for i, score in enumerate(scores) if results[0].boxes.cls[i] == 0]

        save_detection(video_id, frame_number, person_boxes, person_scores, timestamp)

        # Broadcast progress
        await broadcast_progress({
            "video_id": video_id,
            "frame_number": frame_number,
            "object_count": len(person_boxes)
        })

        frame_number += 1

    cap.release()
    os.remove(video_path) 
    return {"video_id": video_id}
