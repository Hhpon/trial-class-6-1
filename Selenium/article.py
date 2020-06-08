from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time
from openpyxl import Workbook


def get_news():
    global num
    time.sleep(1)
    news_list = driver.find_elements_by_xpath(
        "//li[contains(@id,'sogou_vr_11002601_box')]")
    for news in news_list:
        source = news.find_elements_by_xpath('div[2]/div/a')[0].text
        if key not in source:
            continue
        num += 1
        title = news.find_elements_by_xpath('div[2]/h3/a')[0].text
        date = news.find_elements_by_xpath('div[2]/div/span')[0].text
        url = news.find_elements_by_xpath(
            'div[2]/h3/a')[0].get_attribute('href')
        print(num, title, date)
        print('-' * 10)
        row = [title, date, url]
        sheet.append(row)


wb = Workbook()
sheet = wb.active
sheet.title = '公众号推文'
sheet.append(['标题', '时间', '链接'])

print('请先输入需要爬取的公众号名称')
key = input('')

driver = webdriver.Chrome()
driver.get('https://weixin.sogou.com/')
wait = WebDriverWait(driver, 10)
input = wait.until(EC.presence_of_element_located((By.NAME, 'query')))
print(input)
input.send_keys(key)
driver.find_element_by_xpath("//input[@class='swz']").click()

num = 0

for i in range(10):
    get_news()
    if i == 9:
        break
    driver.find_element_by_id('sogou_next').click()

driver.find_element_by_name('top_login').click()

while True:
    try:
        next_page = driver.find_element_by_id('sogou_next')
        break
    except:
        time.sleep(5)

next_page.click()

while True:
    get_news()
    try:
        driver.find_element_by_id('sogou_next').click()
    except:
        break

driver.quit()

wb.save('Selenium/%s.xlsx' % key)
