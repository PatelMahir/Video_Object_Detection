from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

DATABASE_URL = "postgresql://user:password@localhost:5432/video_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def save_detection(video_id, frame_number, bounding_boxes, confidence_scores, timestamp):
    db = SessionLocal()
    detection = Detection(
        video_id=video_id,
        frame_number=frame_number,
        bounding_boxes=bounding_boxes,
        confidence_scores=confidence_scores,
        timestamp=timestamp
    )
    db.add(detection)
    db.commit()
    db.refresh(detection)
    db.close()
    return detection

def get_detections(video_id):
    db = SessionLocal()
    results = db.query(Detection).filter(Detection.video_id == video_id).all()
    db.close()
    return [{"frame_number": r.frame_number, "object_count": len(r.bounding_boxes)} for r in results]
