# Project_DIVA_Mega39s_auto
使用yolov5识别屏幕+按键时间估算实现自动玩Project_DIVA_Mega39s/use yolov5+eta to play Project_DIVA_Mega39s automatically

## 使用方法
```
python 114.py
```
使用114.py,启动后会自动检测屏幕内容,启动完成后打开游戏并打开一首歌曲即可,会自动检测屏幕上的按键图案并且估算按下去的时间.
```
python 115.py
```
使用115.py,启动后会自动检测屏幕内容,启动完成后打开游戏并打开一首突显模式的歌曲,会自动检测屏幕上的按键图案并且在固定时间(0.4s)后按下去.
注意,需要先安装依赖.需要安装pytorch,opencv,sounddevice,keyboard.最好使用cuda加速,不然会很慢.

## 
