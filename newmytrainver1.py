from ultralytics import YOLO
ms = [
    'yolov8n',
    'yolo11n',
]
if __name__ == "__main__":
    for m in ms:
        model= YOLO(m + ".pt")
        model.train(
            data=r"newseaurchin.yaml",
            epochs=100,
            imgsz=640,
            batch=-1,
            cache=False,
            workers=0,
            project="newresult",
            name=m,
    )