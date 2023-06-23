from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor

model = YOLO("goodsSegment.pt")
model.predict(source=0, show=True, conf=0.5)