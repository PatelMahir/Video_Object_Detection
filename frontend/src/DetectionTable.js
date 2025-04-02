import React from 'react';

function DetectionTable({ videoId, detections }) {
  return (
    <div>
      <h2>Detection Results</h2>
      <table border="1">
        <thead>
          <tr>
            <th>Frame Number</th>
            <th>Object Count</th>
          </tr>
        </thead>
        <tbody>
          {detections.map((detection, index) => (
            <tr key={index}>
              <td>{detection.frame_number}</td>
              <td>{detection.object_count}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default DetectionTable;
