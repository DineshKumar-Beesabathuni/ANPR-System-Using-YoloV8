from ultralytics import YOLO
import cv2
import os
import glob
from screeninfo import get_monitors

# Load the trained model
model = YOLO('C:/Users/16756/OneDrive/Desktop/numberplate detection/runs/detect/train3/weights/best.pt')

# Path to the folder containing videos
video_folder = 'C:/Users/16756/OneDrive/Desktop/numberplate detection/demovideos'
output_folder = 'C:/Users/16756/OneDrive/Desktop/numberplate detection/outputs'
os.makedirs(output_folder, exist_ok=True)

# Get a list of all video files in the folder
video_files = glob.glob(os.path.join(video_folder, '*.mp4')) + glob.glob(os.path.join(video_folder, '*.avi'))

# Get screen resolution
screen = get_monitors()[0]
screen_width, screen_height = screen.width, screen.height

for video_file in video_files:
    # Open the video file
    cap = cv2.VideoCapture(video_file)

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    output_path = os.path.join(output_folder, os.path.basename(video_file))
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

        # Resize the frame to fit the screen
        resized_frame = cv2.resize(annotated_frame, (screen_width, screen_height))

        # Write the frame to the output video
        out.write(annotated_frame)

        # Display the frame
        cv2.imshow('Frame', resized_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release everything if job is finished
    cap.release()
    out.release()

cv2.destroyAllWindows()