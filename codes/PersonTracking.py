from collections import defaultdict
import cv2
from ultralytics import YOLO
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
import time


class TrackerThread(QThread):
    """Define a custom thread class for handling video tracking."""

    # Signal to emit frames once they're ready to be displayed.
    frame_ready = pyqtSignal(np.ndarray)

    def __init__(self, video_path):
        super().__init__()
        self.video_path = video_path
        self.model = YOLO('yolov8n.pt')  # Load the YOLOv8 model for person detection.
        self.track_history = defaultdict(list)  # Dictionary to store tracking history of each object.
        self._is_running = True  # Flag to control the thread's execution.

    def stop(self):
        """Set the running flag to False to stop the thread."""

        self._is_running = False
        self.wait()  # Wait for the thread to finish executing.

    def run(self):
        """Run the thread."""
        cap = cv2.VideoCapture(self.video_path)
        frame_skip = 5
        frame_count = 0
        fps = cap.get(cv2.CAP_PROP_FPS)  # Gets the raw frame rate of the video
        delay = (1 / fps) * frame_skip  # Calculating delay time

        # Loop until the thread is stopped or video ends.
        while self._is_running and cap.isOpened():
            success, frame = cap.read()
            if not success:
                break

            # Only each (frame_skip) frame is processed
            if frame_count % (frame_skip + 1) == 0:
                results = self.model.track(source=frame, stream=True, classes=[0], imgsz=[736], persist=True,
                                           tracker='custom_tracker.yaml')
                if results:
                    for result in results:
                        if hasattr(result, 'boxes') and result.boxes:
                            if hasattr(result.boxes, 'id') and result.boxes.id is not None:
                                boxes = result.boxes.xywh.cpu()
                                track_ids = result.boxes.id.int().cpu().tolist()

                                # Draw annotations on the frame.
                                annotated_frame = result.plot()

                                # Update tracking history and draw tracks
                                for box, track_id in zip(boxes, track_ids):
                                    x, y, w, h = box
                                    center = (x + w / 2, y + h / 2)
                                    self.track_history[track_id].append(center)
                                    # Limit track history to 30 points.
                                    if len(self.track_history[track_id]) > 30:
                                        self.track_history[track_id].pop(0)

                                    if len(self.track_history[track_id]) > 1:
                                        cv2.polylines(annotated_frame, [
                                            np.array(self.track_history[track_id], dtype=np.int32).reshape((-1, 1, 2))],
                                                      isClosed=False, color=(255, 0, 0), thickness=2)

                                # Emit the processed frame.
                                self.frame_ready.emit(annotated_frame)
                            else:
                                # Emit the processed frame when not detect person.
                                self.frame_ready.emit(frame)
                        else:
                            # Emit the processed frame when not detect person.
                            self.frame_ready.emit(frame)
                else:
                    # Emit the processed frame when not detect person.
                    self.frame_ready.emit(frame)
                time.sleep(delay)

            frame_count += 1

        cap.release()
