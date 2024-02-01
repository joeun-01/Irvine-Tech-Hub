from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# //*[@id="globalMain"]/main/div[2]/div[2]/div/div[1]/div/div/div[8]
# //*[@id="globalMain"]/main/div[2]/div[2]/div/div[1]/div/div/div[9]
# //*[@id="globalMain"]/main/div[2]/div[2]/div/div[1]/div/div/div[9]

ranking = []
brand = []
product = []
price = []

def getData(i, j):
    area = driver.find_element(By.XPATH,
                               '//*[@id="globalMain"]/main/div[2]/div[2]/div/div[1]/div/div/div[{}]/div[{}]'.format(
                                   i, j))

    split = area.text.splitlines()

    ranking.append(split[0])
    brand.append(split[1])
    product.append(split[2])
    price.append(split[3])

    print(area.text)

    if int(split[0]) == 999:
        toCSV()

def toCSV():
    df = pd.DataFrame()
    df["Ranking"] = ranking
    df["Brand"] = brand
    df["Product"] = product
    df['Price'] = price

    df.to_excel("musinsa.xlsx", index=False)
    df.to_csv('musinsa.csv', encoding='utf-8-sig')

    exit(0)

for i in range(1, 101):
    url = 'https://global.musinsa.com/us/trending/items?gad_source=1&gclid=CjwKCAiAkp6tBhB5EiwANTCx1F6-ntsnbMrAVlY1Nxnw83buXk1fT26Buh9sW4TJ0MdrMjN_rrvwABoCmL8QAvD_BwE&page={}&sex=F&toggleCountry=us&utm_content=musinsa__231201__-mdupus0167______'.format(i)

    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
        driver.get(url)

        # time.sleep(10000)

        driver.implicitly_wait(10)

        for i in range(1, 8):
            for j in range(1, 5):
                # print(i, ' ', j)
                getData(i, j)

        # time.sleep(10000)

        for i in range (2):
            webdriver.ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(2)

        # 471만큼씩 스크롤을 한다

        for i in range(17):
            current_scroll_position = driver.execute_script("return window.scrollY;") # 현재 스크롤 위치
            driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position + 471)) # 스크롤 다운
            time.sleep(2)

            for j in range(1, 5):
                getData(7, j)