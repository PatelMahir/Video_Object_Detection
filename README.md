# Video_Object_Detection

A basic video processing system that accepts video file uploads, runs object detection using YOLOv8 to detect people, stores results in a PostgreSQL database, and displays them on a web dashboard with real-time updates via WebSockets.

## Features
- **Backend**: Built with FastAPI, processes video files, and stores detection results.
- **Object Detection**: Uses YOLOv8 to detect people in video frames.
- **Database**: Stores detection data (frame number, bounding boxes, confidence scores, timestamp, video ID) in PostgreSQL.
- **Frontend**: React-based dashboard for uploading videos and viewing detection results.
- **Real-Time Updates**: WebSockets provide live updates during video processing.
- **Deployment**: Dockerized for easy setup and deployment.

## Tech Stack
- **Backend**: Python, FastAPI, OpenCV, YOLOv8, PyTorch, SQLAlchemy
- **Frontend**: React
- **Database**: PostgreSQL (SQLite supported for local testing)
- **Deployment**: Docker, Docker Compose

## Prerequisites
- Python 3.9+
- Node.js 16+
- Docker (optional, for containerized deployment)
- PostgreSQL (or SQLite for local testing)


## Setup Instructions

### Local Development
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd video_processing_system
2. Backend Setup
Navigate to the backend directory:
cd backend/app

Install dependencies:
pip install -r requirements.txt

Set up PostgreSQL:
Create a database named video_db.
Update DATABASE_URL in database.py with your credentials.

Run the FastAPI server:
uvicorn main:app --reload --host 0.0.0.0 --port 8000

3. Frontend Setup
Navigate to the frontend directory:
cd frontend

Install dependencies:
npm install

Start the React development server:
npm start

4. Access the Application
Backend API: http://localhost:8000
Frontend Dashboard: http://localhost:3000

5.Docker Deployment
Build and Run with Docker Compose
docker-compose up --build

Access the Application
Backend: http://localhost:8000
Frontend: http://localhost:3000
