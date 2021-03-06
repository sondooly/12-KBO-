# -*- coding: utf-8 -*-
"""12주차 크롤링 이정언 최종.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yGCVGQkgBP63rm1eXhA-HDD-sR55j64v
"""

!pip install selenium
!apt-get update
!apt install chromium-chromedriver

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
f = open("./2조_이정언_출력결과.txt", 'w')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('chromedriver', options=options)

url = 'https://www.koreabaseball.com/TeamRank/TeamRank.aspx'
browser.get(url)

select = Select(browser.find_element(By.XPATH, f'//*[@id="cphContents_cphContents_cphContents_ddlYear"]'))
select.select_by_value('2020') #('연도') 형식으로 연도 입력하기
time.sleep(1) #for문 돌아가기 전에 연도 선택한 것까지 코드 돌리기

for i in range(1, 11):
    grade = browser.find_element(By.XPATH, f'//*[@id="cphContents_cphContents_cphContents_udpRecord"]/table/tbody/tr[{i}]/td[1]').text
    team = browser.find_element(By.XPATH, f'//*[@id="cphContents_cphContents_cphContents_udpRecord"]/table/tbody/tr[{i}]/td[2]').text
    win = browser.find_element(By.XPATH, f'//*[@id="cphContents_cphContents_cphContents_udpRecord"]/table/tbody/tr[{i}]/td[4]').text
    lose = browser.find_element(By.XPATH, f'//*[@id="cphContents_cphContents_cphContents_udpRecord"]/table/tbody/tr[{i}]/td[5]').text
    draw = browser.find_element(By.XPATH, f'//*[@id="cphContents_cphContents_cphContents_udpRecord"]/table/tbody/tr[{i}]/td[6]').text
    winning_rate = browser.find_element(By.XPATH, f'//*[@id="cphContents_cphContents_cphContents_udpRecord"]/table/tbody/tr[{i}]/td[7]').text

    print(grade,'위 팀명:', team, '/', '승:',win, '/', '패:',lose, '/', '무:',draw, '/', '승률:',winning_rate)

    f.write(f'{grade}위 팀명: {team} / 승: {win} / 패: {lose} / 무: {draw} / 승률: {winning_rate} \n' )
f.close()

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('chromedriver', options=options)


url = 'https://www.koreabaseball.com/Player/RegisterAll.aspx'
browser.get(url)

table = browser.find_element_by_class_name('tData.tDays')
tbody = table.find_element_by_tag_name("tbody")
row = tbody.find_elements_by_tag_name("tr")
for index, value in enumerate(row):
  for i in range(2, 6):
    body=value.find_elements_by_tag_name("td")[i]
    print(body.text) #KBO 현역 선수들 이름(번호) 뽑기