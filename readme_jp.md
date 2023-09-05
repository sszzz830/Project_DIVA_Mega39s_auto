# Project_DIVA_Mega39s_auto

YOLOv5を使用して、Project DIVA Mega39sの画面認識とキープレスタイミング推定を自動化します.<br>
<img width="529" alt="yolo result" src="https://github.com/sszzz830/Project_DIVA_Mega39s_auto/assets/32834442/e4342a30-d40b-42fc-b2e6-669fd0515e89">

## 使い方
```
python 114.py
```
114.pyを実行します。起動後、自動的に画面内容を検出します。初期化が完了したら、ゲームを開いて曲を選びます。スクリプトは画面上のキーパターンを識別し、キーを押すタイミングを推定します。

```
python 115.py
```
115.pyを実行します。起動後、同様に自動的に画面内容を検出します。初期化が完了したら、ゲームを開いて「チャレンジモード」の曲を選びます。スクリプトはキーパターンを識別し、固定時間（0.4秒）後にそれらを押します。

注意: 事前に依存関係をインストールする必要があります。必要なライブラリはPyTorch、OpenCV、sounddevice、およびkeyboardです。より良いパフォーマンスのために、CUDAの加速が推奨されます。

## モデル
事前学習済みのYOLOv5モデルyolov5s.ptを使用し、199枚の画像データセットで200エポックさらに訓練してproject_diva_mega39s_4obj.ptを取得しました。このモデルはXYABキーを正確に検出でき、ほとんどのケースで高い再現率と精度があります。データセットはRoboflowでアノテーションされています。以下のリンクからダウンロードできます。<a href="https://universe.roboflow.com/zhao-qianli-tnqky/pmd39s">
    <img src="https://app.roboflow.com/images/download-dataset-badge.svg"></img>
</a><br>
タイミング推定には、簡単なアルゴリズム（改善予定）を使用します。検出された領域をグレースケールに変換し、360度をスキャンして白いピクセルが最も集中している方向を見つけます。タイミングは、1.6秒のサークル回転時間に基づいて推定されます。

検出されたイベントはeventlistに格納され、別のスレッドがキープレスアクションを実行するのを待ちます。イベントが実行されると、cooldownlistに入り、0.4秒待機してから終了します。

各検出オブジェクトはまずサイズの検証を受けます。その後、eventlistおよびcooldownlist内の既存のイベントと比較されます。一意のイベントのみがタイミング推定フェーズ（114.pyで）に進むか、直接eventlistに入ります（115.pyで）。


## デモビデオ
[パフォーマンスデモ](https://github.com/sszzz830/Project_DIVA_Mega39s_auto/assets/32834442/43977a8b-f48c-463f-b942-6b713d64ab6d)
<br>
[YOLO検出デモ](https://github.com/sszzz830/Project_DIVA_Mega39s_auto/assets/32834442/5b742019-a64c-47c4-bf61-9147dde34990)
## TODO List
タイミング推定のアルゴリズムを改善し、より多くのコンボを達成します。<br>
<-と->の矢印、ホールド、および同時キープレスの認識を可能にします。<br>
認識データを保存して、軸の調整と共有ができるようにします。保存されたファイルを通じて微調整と直接ロードが可能です。

## License
このリポジトリは、YOLOv5を使用しているため、AGPL v3.0でライセンスされています。




