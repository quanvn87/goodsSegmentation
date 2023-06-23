# goodsSegmentation

# Setup environment
Terminal:
$ conda create --name yolov8_segmentation
$ conda activate yolov8_segmentation
$ conda install ultralytics
# Train with pretrained model:
$ yolo task=segment mode=train epochs=100 data=data.yaml model=yolov8n-seg.pt imgsz=640 batch=50
# Validate the model:
After training rename "file best.pt" in ..runs\segment\train\weights into "goodsSegment.pt"
$ yolo task=segment mode=val model=goodsSegment.pt data=data.yaml
# Test with the webcam:
$ python predict.py
