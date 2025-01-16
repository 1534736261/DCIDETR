import warnings
warnings.filterwarnings('ignore')
from ultralytics import RTDETR

if __name__ == '__main__':
    model = RTDETR('ultralytics/cfg/models/DCI-DETR.yaml')
    # model.load('') # loading pretrain weights
    model.train(data='datasets/visdata.yaml',
                cache=False,
                imgsz=640,
                epochs=180,
                batch=4,
                workers=4,
                device='0',
                # resume='', # last.pt path
                project='runs/train',
                name='exp',
                )