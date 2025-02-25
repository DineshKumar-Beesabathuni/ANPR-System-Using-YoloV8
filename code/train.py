from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n.yaml')  # You can choose different model sizes like yolov8s.yaml, yolov8m.yaml, etc.

# Train the model
model.train(data='data.yaml', epochs=100, imgsz=640)