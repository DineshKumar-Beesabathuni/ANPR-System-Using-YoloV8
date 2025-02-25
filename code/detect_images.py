from ultralytics import YOLO
import os
import glob

# Load the trained model
model = YOLO(r'C:/Users/16756/OneDrive/Desktop/numberplate detection/runs/detect/train3/weights/best.pt')

# Path to the folder containing images
image_folder = r'C:/Users/16756/OneDrive/Desktop/numberplate detection/demoimages'

# Get a list of all image files in the folder
image_files = glob.glob(os.path.join(image_folder, '*.jpg')) + glob.glob(os.path.join(image_folder, '*.jpeg')) + glob.glob(os.path.join(image_folder, '*.png'))

# Process each image
for image_file in image_files:
    # Perform inference on the image
    results = model(image_file)

    # Display the results
    for result in results:
        result.show()
