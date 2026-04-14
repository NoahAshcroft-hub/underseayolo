# 海胆识别 YOLO 项目

本项目聚焦于基于 YOLO 的海胆识别与检测任务。  
项目的主要目标是支持多人协作开发，包括数据集整理、模型改进、训练实验和 mAP 优化。

## 项目目标
我们希望构建一个可复现、可扩展、便于协作的海胆识别项目。  
本仓库用于统一管理训练代码、数据配置、模型改动和实验流程，方便后续持续优化算法效果。

## 项目内容
- YOLO 训练脚本
- 预测与推理脚本
- 数据集配置文件
- 自定义模型配置与改动
- 团队协作所需的基础环境配置

## 项目结构
```text
.
├─ README.md
├─ requirements.txt
├─ train.py
├─ predict.py
├─ data/
│  └─ seaurchin.yaml
├─ models/
│  └─ yolov8_cbam.yaml
├─ ultralytics/
└─ examples/
