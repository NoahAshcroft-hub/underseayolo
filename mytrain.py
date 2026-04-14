from ultralytics import YOLO
if __name__ == "__main__":
    model = YOLO(r"ultralytics/cfg/models/v8/yolov8my_CBAM.yaml")
    model.train(
        data=r"newseaurchin.yaml",
        epochs=100,
        imgsz=640,
        batch=16,
        cache=False,
        workers=0,
    )