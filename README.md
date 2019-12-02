# iottalk_dashboard
### Using the data that crawl on the weather website, show it on the dashboard.
教學： [https://hackmd.io/5LqVk4MBSCinRXQderD_Jw]

安裝 Mysql : [https://andy6804tw.github.io/2019/01/29/ubuntu-mysql-setting/]

若mysql下載失敗, 解除安裝mysql [https://noob.tw/remove-mysql-completely/] 並再重新安裝一次

完成以上設定後至瀏覽器輸入 [http://127.0.0.1:7788/] 帳密 admin / 123456789 連接 dashboard.

並執行以下動作: [https://hackmd.io/PwhExG5NSkO4oC8M30pVZQ?view&fbclid=IwAR0Qo-3oIJZFdnOachw_U_2c2qLxDtYmnQNwO9yUCSeai7yp8J-UkhkedWw]

至 IoTtalk Device Feature Management 新增Input Device Features
勾選AtPressure、Humidity、Temperature、rain、windspeed
(若無法勾選請自行至Device Feature新增)
![Device Feature Management ](https://github.com/ChangWinnie/iottalk_dashboard/blob/master/Screenshot%20from%202019-12-02%2021-31-36.png "Device Feature Management ")

回到project，model點選dummy device，勾選AtPressure、Humidity、Temperature、rain、windspeed
![Dummy_device](https://github.com/ChangWinnie/iottalk_dashboard/blob/master/Screenshot%20from%202019-12-02%2021-39-20.png "Dummy device")

ODF model選擇DataServer 勾選如圖的features:
![DataServer](https://github.com/ChangWinnie/iottalk_dashboard/blob/master/Screenshot%20from%202019-12-02%2021-40-52.png "DataServer")

完成後至終端機將路徑切換到crawl_weather.py之資料夾 執行`python crawl_weather.py`

確認dashboard有無資料

有即完成~
