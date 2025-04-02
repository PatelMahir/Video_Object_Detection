import React from 'react';

function VideoPlayer({ videoSrc }) {
  return (
    <div>
      <h2>Uploaded Video</h2>
      <video controls width="600" src={videoSrc}></video>
    </div>
  );
}

export default VideoPlayer;
