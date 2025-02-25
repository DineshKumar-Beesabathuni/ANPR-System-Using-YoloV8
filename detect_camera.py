from ultralytics import YOLO
import cv2
import os

# Load the trained model
model = YOLO('C:/Users/16756/OneDrive/Desktop/numberplate detection/runs/detect/train3/weights/best.pt')

# Open the camera feed
cap = cv2.VideoCapture(0)  # Use 0 for the default camera, or replace with the appropriate camera index

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
output_folder = 'C:/Users/16756/OneDrive/Desktop/numberplate detection/outputs'
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, 'output_camera.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference on the frame
    results = model(frame)

    # Draw the results on the frame
    annotated_frame = results[0].plot()

    # Write the frame to the output video
    out.write(annotated_frame)

    # Display the frame
    cv2.imshow('Frame', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()