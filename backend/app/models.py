from sqlalchemy import Column, Integer, String, Float, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Detection(Base):
    __tablename__ = "detections"
    id = Column(Integer, primary_key=True, index=True)
    video_id = Column(String, index=True)
    frame_number = Column(Integer)
    bounding_boxes = Column(JSON) 
    confidence_scores = Column(JSON)
    timestamp = Column(Float)
