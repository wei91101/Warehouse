# 倉儲網頁管理系統
> 包含六大功能：及時定位、資產追蹤、入庫驗收、庫存貨量、揀貨作業、出貨製單
## 使用指南

### 檔案資料分類說明
#### app_redis.py：主程式、templates資料夾：網頁前端html、static資料夾

> static資料夾含：build、docs、production、src (bootstraps套件)、vendor(bootstraps套件)
>> vender 資料夾包含：urrent_stock (庫存盤點)、pickup(揀貨)、input_stock (入庫) outbound_tabulation (出庫)、Scatterchart (即時定位)、wms_trackingAssets (資產追蹤) 


### 執行環境建置 
>需安裝Python、MySQL、Redis等軟體

#### 1. Python
* [下載](https://www.python.org/downloads)並安裝Python
#### 2. MySQL資料庫
##### server建置
* 需先建置server，可至官方網站[下載](https://www.wampserver.com/en/)並安裝Wampserver
##### MySQL安裝
* 完成server的建置後至官方網站[下載](https://dev.mysql.com/downloads/mysql/)並安裝MySQL
##### phpMyAdmin
* 另可至官方網站[下載](https://www.phpmyadmin.net/)並安裝phpMyAdmin進行資料庫的管理



#### 3. Redis資料庫
* 至官方網站[下載](https://github.com/tporadowski/redis/releases)並安裝Redis


### 啟用

#### 1. 使用pip安裝requirements.txt中的Python類庫內容：
```
$ pip install -r requirements.txt
```

> requirements.txt 內容：
```
# Library dependencies for the python code.  You need to install these with
# `pip install -r requirements.txt` before you can run this.

bidict==0.21.2
click==7.1.2
dnspython==1.16.0
eventlet==0.30.2
Flask==1.1.2
Flask-SocketIO==5.0.1
greenlet==1.0.0
itsdangerous==1.1.0
Jinja2==2.11.3
MarkupSafe==1.1.1
numpy==1.20.1
PyMySQL==1.0.2
pypiwin32==223
python-engineio==4.0.1
python-socketio==5.1.0
pywin32==300
redis==3.5.3
six==1.15.0
Werkzeug==1.0.1
```
#### 2. 用cmd執行app_redis.py
* 步驟1：
``` 
$ cd+空格+app_redis.py所在目錄 
```
* 步驟2：
```
$ python+空格+redis.py
```
#### 3. 打開瀏覽器進入 http://127.0.0.1:7788
>執行完app_redis.py即可開啟瀏覽器進入倉儲網頁管理系統
 ![](https://i.imgur.com/Cdc6YQ8.png)


### 使用示例
> 倉儲網頁管理系統包含六大功能:及時定位、資產追蹤、入庫驗收、庫存貨量、揀貨作業、出貨製單
* #### 及時定位
* #### 資產追蹤
  ![](https://i.imgur.com/d5UEH8l.png)
* #### 入庫驗收
  * 入庫日期：選擇入庫日期
  * 操作人員編號：輸入操作人員編號
  * 入庫原因：設定入庫原因種類（一般退貨/退換貨/設備機具）
  * RFID編號：輸入產品的RFID編號
  * 入庫摘要資訊：輸入入庫摘要資訊
  

  ![](https://i.imgur.com/Ugws9lG.png)
* #### 庫存貨量
  ![](https://i.imgur.com/s4esJEX.png)
* #### 揀貨作業
  ![](https://i.imgur.com/SSjUI7S.png)
* #### 出貨製單
  * 操作人員編號：輸入操作人員編號
  * 製單類型：選擇製單類型（銷貨單/生產製令單/樣品製造單）
  * 揀貨員編號：輸入揀貨員編號
  * 增加出庫紀錄
  
  ![](https://i.imgur.com/jC3H07J.png)



## 疑難排解
### 無法連結至資料庫
#### 1. 修改app_redis.py連結MySQL功能函式為本地資料庫的帳號密碼
```
db = pymysql.connect("127.0.0.1", "root", "esfortest", "warehouse2")
```
> 更改為
```
db = pymysql.connect("localhost", "本地資料庫使用者名稱", "本地資料庫使用者密碼", "warehouse2")
```
#### 2. 若遇 “ __ init __ () takes 1 positional argument but 5 were given ” 報錯訊息
> 則更改函式表達式
```
dbhost = 'localhost'
dbuser = '本地資料庫使用者名稱'
dbpass = '本地資料庫使用者密碼'
dbname = 'warehouse2'
db = pymysql.connect(dbhost,dbuser,dbpass,dbname)
```

## 版本歷史

## 關於作者


## 授權協議

