# DCI-DETR

> Ming Xin, Bo Wang, Xin Wang, Kaiting Gong, Caili Fang

## Overview of DCI-DETR

![image](https://github.com/user-attachments/assets/29a50324-9083-45e4-b87e-5c3e338d5245)




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

