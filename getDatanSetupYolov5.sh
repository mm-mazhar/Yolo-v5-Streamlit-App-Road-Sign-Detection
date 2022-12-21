#!/bin/bash -e
echo "########## Setting up Kaggle API"
mkdir ~/.kaggle
cp kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
pip install -r requirements.txt
echo "#################### Downloading Dataset"
kaggle datasets download -d andrewmvd/road-sign-detection
unzip road-sign-detection.zip -d dataset
mv ./dataset/annotations ./dataset/labels

echo "#################### Converting Dataset into Yolo Format"
python3 - <<END
from preprocessing import convert_voc_to_yolo
convert_voc_to_yolo()
END

echo "#################### Processing Train Test Split"
for filename in ./dataset/labels/*.xml
do
  echo "Removing ${filename}"
  rm -rf $filename
done;

for filename in ./dataset/labels/*.txt
do
  echo "Moving ${filename}"
  mv $filename ./dataset/images
done;

rm -rf ./dataset/labels

python3 ./trainTestSplit.py

# cp ./data.yaml ./dataset

echo "#################### Downloading Yolo V5 Repo "
git clone https://github.com/ultralytics/yolov5

cd './yolov5'

echo "##### Installing Requirements.txt #####"
pip install -r requirements.txt
pip install streamlit

python3 - <<END
import torch
print("#################### Dependencies Check")
#from IPython.display import Image, clear_output  # to display images
#from utils.google_utils import gdrive_download  # to download models/datasets
#clear_output()
print('Setup complete. Using torch %s %s' % (torch.__version__, torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU'))
END

echo "#################### Copying custom_data.yaml and Moving dataset folder"
cd ..
cp ./custom_data.yaml ./yolov5/data
mv ./dataset ./yolov5

echo "Copying Trained Model to yolov5/models"
cp './best.pt' './yolov5/models'

echo "##### Installing Requirements.txt #####"
pip install -r requirements.txt

mkdir -p ./yolov5/data/videos

echo "__________________ Script END __________________"