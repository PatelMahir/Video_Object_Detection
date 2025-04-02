import React, { useState, useEffect } from 'react';
import VideoPlayer from './VideoPlayer';
import DetectionTable from './DetectionTable';

function App() {
  const [videoFile, setVideoFile] = useState(null);
  const [videoId, setVideoId] = useState(null);
  const [detections, setDetections] = useState([]);
  const [ws, setWs] = useState(null);

  useEffect(() => {
    const websocket = new WebSocket('ws://localhost:8000/ws');
    websocket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setDetections((prev) => [...prev, data]);
    };
    setWs(websocket);
    return () => websocket.close();
  }, []);

  const handleUpload = async (event) => {
    const file = event.target.files[0];
    setVideoFile(URL.createObjectURL(file));
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('http://localhost:8000/upload/', {
      method: 'POST',
      body: formData,
    });
    const result = await response.json();
    setVideoId(result.video_id);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Video Processing Dashboard</h1>
      <input type="file" accept="video/*" onChange={handleUpload} />
      {videoFile && <VideoPlayer videoSrc={videoFile} />}
      {videoId && <DetectionTable videoId={videoId} detections={detections} />}
    </div>
  );
}

export default App;
