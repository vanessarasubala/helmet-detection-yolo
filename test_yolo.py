from ultralytics import YOLO

# load pretrained model
model = YOLO("yolov8n.pt")

# test on sample image
results = model("https://ultralytics.com/images/bus.jpg", save=True)

print("Done!")