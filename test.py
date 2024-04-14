from pathlib import Path


# Path to your downloaded YOLOv8 model weights
model_weights = Path("best.pt")  # Replace with your model name

# Load the model


# Define a list of image paths
image_paths = [Path("./test_images/test1.jpg"), Path("./test_images/test3.jpg"), Path("./test_images/test2.jpg")]

print(image_paths[0])
