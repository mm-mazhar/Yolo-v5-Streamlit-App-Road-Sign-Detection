# Yolo V5 | Streamlit App | Road Sign Detection

Step 1

- `git clone "https://github.com/mazqoty/Yolo-v5-Streamlit-App-Road-Sign-Detection.git"`
- Get/Setup Kaggle API credentials, download `kaggle.json` file
- `conda create -n envyolov5` or `python -m venv envyolov5`
- `conda activate envyolov5` or `.\envyolov5\Scripts\activate` for Windows `source envyolov5/bin/activate` for Linux
- Optional: `python -m ipykernel install --user --name=envyolov5`
- RUN `getDatanSetupYolov5.sh`

Step 2 (Skip if not interested in training the model)

- For Model Training upload `Yolov5_Colab_CustomModel_Training.ipynb` on Google Colab
- Upload `archive.tar.gz` file in yolov5/dataset/ in Google Colab
- Upload `custom_data.yaml` file in Google Colab
- Location where to upload these files is written in `Yolov5_Colab_CustomModel_Training.ipynb`
- Training results will be saved somewher in yolov5/runs/train/... e.g. yolov5/runs/train/exp3

Step 3
    
- Note: if Step 2 is executed then remember to change the file path of trained weights in app.py (line number: 90)
- RUN `streamlit run app.py`

Error handling: 
    - After running the above script,  if `no module error` is occured then just find the relevent `pip install <module name>` command and run it
- Other useful commands
- `conda env list`
- `conda env remove -n ENV_NAME`
- `conda list`
- `python.exe -m pip install -r requirements.txt --user`

#### Click Here To Watch The Video
[![asciicast](https://i.imgur.com/wv8sS6z.jpg)](https://youtu.be/l0yEcua5HEw)
