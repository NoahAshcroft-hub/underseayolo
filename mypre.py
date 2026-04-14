from ultralytics import YOLO
model=YOLO(r"D:\deeplearnning\ultralytics-8.3.163\result\yolo11n\yolo11n\weights\best.pt")
model.predict(
    source=r"D:\haidann\new",
    save=True,
    save_txt=True,
    show=False,
    conf=0.25,
    iou=0.7,
    max_det=300,
)