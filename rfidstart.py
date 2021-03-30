#要將chromedriver.exe放進同一個資料夾
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os
d = os.popen('arp -a')
f = d.read()
#print(f)
f.replace(" ", "")
#print(f)
pos = f.find('0c-b2-b7-d1-f0-0e')
#print(pos)
#pos2 = f.find('192.168.0.31')
#print(pos2)
#pos3 = f.rfind('192.168.0.31')
#print(pos3)
fnew=f[0:pos]
pos2 = fnew.rfind('192')
ip=f[pos2:pos]
ip=ip.rstrip()

#print(ip)

options = webdriver.ChromeOptions()
# ip = '192.168.0.31'
# ------ 設定要前往的網址 ------
url = 'http://'+ip+':3161/index.html'

# ------ 登入的帳號與密碼 ------
username = 'admin'
password = 'admin'


# ------ 透過Browser Driver 開啟 Chrome ------
driver = webdriver.Chrome()

# ------ 前往該網址 ------
driver.get(url)

elem = driver.find_element_by_id("lg_login")
elem.send_keys(username)

elem = driver.find_element_by_id("lg_pass")
elem.send_keys(password)

elem.send_keys(Keys.RETURN)

button = driver.find_element_by_id("start")
button.click()


