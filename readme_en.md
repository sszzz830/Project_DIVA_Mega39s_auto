# Project_DIVA_Mega39s_auto

Automate gameplay in Project DIVA Mega39s using YOLOv5 for screen recognition and keypress timing estimation.<br>
<img width="529" alt="yolo result" src="https://github.com/sszzz830/Project_DIVA_Mega39s_auto/assets/32834442/e4342a30-d40b-42fc-b2e6-669fd0515e89">

## How to Use
```
python 114.py
```
Run 114.py. After launching, it will automatically detect screen content. Once initialized, open the game and select a song. The script will identify key patterns on the screen and estimate the timing for pressing the keys.

```
python 115.py
```
Run 115.py. After launching, it will also automatically detect screen content. Once initialized, open the game and select a song in "Challenge Mode." The script will identify key patterns and press them after a fixed time (0.4s).

Note: You need to install dependencies first. Required libraries include PyTorch, OpenCV, sounddevice, and keyboard. CUDA acceleration is recommended for better performance.

## models
We use the pre-trained YOLOv5 model yolov5s.pt and further trained it on a dataset of 199 images for 200 epochs to obtain project_diva_mega39s_4obj.pt. This model can accurately detect XYAB keys and performs well in most cases with high recall and precision rates. The dataset is annotated using Roboflow. You can download it from the link below.<a href="https://universe.roboflow.com/zhao-qianli-tnqky/pmd39s">
    <img src="https://app.roboflow.com/images/download-dataset-badge.svg"></img>
</a>.<br>
For timing estimation, we use a rudimentary algorithm (to be improved). It converts the detected region to grayscale, then scans 360 degrees to find the direction where the white pixels are most concentrated. The timing is then estimated based on a 1.6s circle rotation time.

Events detected are stored in an eventlist, waiting to be executed by a separate thread for keypress actions. When an event is executed, it enters a cooldownlist and waits for 0.4s before being terminated.

Each detected object first undergoes size validation. It is then compared with existing events in eventlist and cooldownlist. Only unique events will proceed to the timing estimation phase (in 114.py) or directly enter eventlist (in 115.py).


## DEMO videos
[DEMO](https://github.com/sszzz830/Project_DIVA_Mega39s_auto/assets/32834442/43977a8b-f48c-463f-b942-6b713d64ab6d)
<br>
[YOLO Detection Demo](https://github.com/sszzz830/Project_DIVA_Mega39s_auto/assets/32834442/5b742019-a64c-47c4-bf61-9147dde34990)
## TODO List
Improve timing estimation algorithms and hit more combos.<br>
Enable the recognition of <- and -> arrows, holds, and simultaneous key presses.<br>
Store recognition data for axis modification and sharing. Allow fine-tuning and direct loading through saved files.

## License
This repository is licensed under AGPL v3.0, as it utilizes YOLOv5.




