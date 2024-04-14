from ultralytics import YOLO
import torch

# Define paths
data_cfg = "E:\ProjectFiles\Python\pothole_v1\datasets\v3\data.yaml"  # Path to your data config file
weights = "yolov8m.pt"  # Path to pre-trained weights (optional)
epochs = 25  # Number of training epochs
# batch_size = 3  # Batch size for training
imgsz = 640  # Image size for training

# Set device (assuming single GPU)
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Using device: {device}')

# # Initialize model
# model = YOLO(weights).to(device)

# # Start training
# model.train(
#     data=data_cfg,
#     epochs=epochs,
#     imgsz=imgsz,
#     device=device)

# # Save the trained model
# model.save("400_trained.pt")

# print("Training completed! Saved model to yolov8_custom_trained.pt")