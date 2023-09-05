# Project_DIVA_Mega39s_auto
[English README](readme_en.md) | [日本語のREADME](readme_jp.md)<br>
---

使用yolov5识别屏幕+按键时间估算实现自动玩Project_DIVA_Mega39s<br>
<img width="529" alt="yolo result" src="https://github.com/sszzz830/Project_DIVA_Mega39s_auto/assets/32834442/e4342a30-d40b-42fc-b2e6-669fd0515e89">

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

## 模型
使用yolov5的预训练模型yolov5s.pt,然后在199张图片的数据集训练了200epoch得到project_diva_mega39s_4obj.pt.该模型能检测XYAB,在绝大部分情况下表现良好,召回率和正确率都很高.数据集使用roboflow标注,地址<a href="https://universe.roboflow.com/zhao-qianli-tnqky/pmd39s">
    <img src="https://app.roboflow.com/images/download-dataset-badge.svg"></img>
</a>.<br>
按键时间估算使用了一个很烂且正确率很低的算法(会改进),大概是把yolo检测到的目标区域黑白化,然后遍历360度找出白色点占比最高的方向(只判断下半圆的指针,有一个-+7度的修正机制,虽然修正里还是很烂),然后按照指针一圈1.6s估算按下时间.<br>
检测到的事件会被存储在eventlist里,等待被一个线程执行按下按键操作.当一个事件被执行,它不会被立即销毁,而是进入cooldownlist,等待0.4s冷却后再结束其生命周期.<br>
每次检测到的目标首先会判断尺寸是否合格,然后和eventlist和cooldownlist内的事件对比,只有当其不重复时才会进入估算环节(114.py)或者进入eventlist(115.py)<br>


## 演示视频
[效果演示](https://github.com/sszzz830/Project_DIVA_Mega39s_auto/assets/32834442/43977a8b-f48c-463f-b942-6b713d64ab6d)
<br>
[yolo识别演示](https://github.com/sszzz830/Project_DIVA_Mega39s_auto/assets/32834442/5b742019-a64c-47c4-bf61-9147dde34990)
## TODO List
改善模型和算法的时间估算能力,多打点combo.<br>
使识别<-和->,和hold,和多个按键一起按的情况.<br>
存储识别数据以用于修改轴和分享.可以通过保存的文件微调和直接加载.

## License
本仓库使用AGPL v3.0授权,因为使用了yolov5.




