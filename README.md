# Enhancing Small Object Detection in UAV Aerial Imagery with DCI-DETR: A Deep Learning Approach

> Ming Xin, Bo Wang, Xin Wang, Kaiting Gong, Caili Fang

## Introduction

![image](https://github.com/user-attachments/assets/29a50324-9083-45e4-b87e-5c3e338d5245)


With the widespread adoption of unmanned aerial vehicle (UAV) technology, the demand for accurate detection of small objects in aerial photography has surged. However, small objects in UAV imagery often face challenges such as small size, occlusion, and dim lighting, leading to issues like missed detections and false alarms. To address these challenges, this paper proposes DCI-DETR, an enhanced small object detection model. DCI-DETR introduces a variant residual network (V-Resnet) that integrates Deformable ConvNets v2 (DCNv2) and a parameter-free attention mechanism (SimAM) to extract features more effectively. Additionally, it optimizes the Attention-based Internal Feature Interaction (AIFI) module by replacing multi-head self-attention with Cascaded Group Attention (CGA), significantly improving computational efficiency. Furthermore, DCI-DETR utilizes a novel Shape-Inner Intersection over Union (IoU) loss function that focuses on the shape and scale of bounding boxes, enhancing detection precision. Experimental results on the VisDrone2019-DET dataset demonstrate that DCI-DETR achieves significant improvements in small object detection performance, with Precision, Recall, mAP50, mAP50-95, and FPS increasing by 1.2%, 2.5%, 2.4%, 3.2%, and 20%, respectively, compared to the original RT-DETR. This study presents an effective solution for small object detection in aerial imagery.

## Datasets

First, Users need to pre-process visdrone2019 dataset, Please get the yolo format json file.

## Results and models

|  Backbone  | mAP50 | mAP50-95 | FPS  |                          Baidu Yun                           |
| :--------: | :---: | :------: | :--: | :----------------------------------------------------------: |
| Resnet-r18 | 0.475 |  0.294   | 36.9 | [Model](https://pan.baidu.com/s/1xtyd-czXDKAN6rujVVVSrg?pwd=853p) |

## Get Started

```
pip install -r requirements.txt
unzip ultralytics.zip
python train.py
python val.py
```

