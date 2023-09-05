#!/usr/bin/env python3
import torch
from time import time, sleep
import keyboard
from threading import Thread
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageGrab
import sounddevice as sd

#fs = 44100  # 采样率
#t = np.linspace(0, 0.04, int(0.04 * fs), endpoint=False)
#x = 0.5 * np.sin(2 * np.pi * 440 * t)
# sd.play(x, fs)

custom_names = ['a', 'b', 'x', 'y']
kilist = ['s', 'd', 'a', 'w']
eventlist = []  # [(timestamp, coordinate, key), ...]
cooldownlist = []  # [(timestamp, coordinate, key), ...]


def capture_screen():
    screenshot = ImageGrab.grab()
    frame = np.array(screenshot)
    return frame


class VideoFrame:
    def __init__(self, video_path):
        self.cap = cv2.VideoCapture(video_path)

    def get_next_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame


vSource = 'cap'  # cap for screencapture/video for local video
video_path = ""
if (vSource == 'video'):
    video_frame = VideoFrame(video_path)


def getFrame():
    if vSource == 'video':
        frame = video_frame.get_next_frame()
    else:
        frame = capture_screen()
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    return frame_bgr


def process_events():
    global eventlist, cooldownlist
    while True:
        current_time = time()
        for event in eventlist:
            timestamp, coordinate, key = event
            if timestamp <= current_time:
                # sd.play(x, fs)
                keyboard.press(key)
                sleep(0.003)
                keyboard.release(key)
                cooldownlist.append(event)
                eventlist.remove(event)
        sleep(0.001)


def process_cooldowns():
    global cooldownlist
    while True:
        current_time = time()
        for event in cooldownlist:
            timestamp, _, _ = event
            if timestamp <= current_time - 0.42:
                cooldownlist.remove(event)
        sleep(0.005)


event_thread = Thread(target=process_events)
cooldown_thread = Thread(target=process_cooldowns)
event_thread.start()
cooldown_thread.start()


def is_valid_bbox(x1, y1, x2, y2, threshold_min=84, threshold_max=184):
    width = x2 - x1
    height = y2 - y1
    return threshold_min <= width <= threshold_max and threshold_min <= height <= threshold_max


def is_new_event(coordinate, threshold=60.0):
    global eventlist, cooldownlist
    for _, cd_coordinate, _ in cooldownlist:
        distance = ((coordinate[0] - cd_coordinate[0]) ** 2 + (coordinate[1] - cd_coordinate[1]) ** 2) ** 0.5
        if distance < threshold:
            return False
    for _, ev_coordinate, _ in eventlist:
        distance = ((coordinate[0] - ev_coordinate[0]) ** 2 + (coordinate[1] - ev_coordinate[1]) ** 2) ** 0.5
        if distance < threshold:
            return False
    return True



model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
cpkt = torch.load("project_diva_mega39s_4obj.pt", map_location=torch.device("cuda"))
yolov5_load = model
yolov5_load.model = cpkt["model"]
yolov5_load.names = custom_names

while True:
    imgnp = getFrame()
    t0 = time()
    results = yolov5_load(imgnp)
    results_xyxy = results.xyxy[0]
    results_xyxy = results_xyxy.cpu().int()
    for i, bbox in enumerate(results_xyxy):
        x1, y1, x2, y2, _, ki = bbox
        if is_valid_bbox(x1, y1, x2, y2):
            coordinate = (int((x1 + x2) // 2), int((y1 + y2) // 2))
            if is_new_event(coordinate):
                timestamp = time()
                eventlist.append((t0 + 0.4, coordinate, kilist[ki]))
# print(time() - t0)