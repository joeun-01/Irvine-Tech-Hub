from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Columns
ranking = []
brand = []
product = []
price = []

# Get data from Musinsa
def getData(i, j):
    # Use XPATH to locate the data you want to get
    area = driver.find_element(By.XPATH,
                               '//*[@id="globalMain"]/main/div[2]/div[2]/div/div[1]/div/div/div[{}]/div[{}]'.format(
                                   i, j))

    # Save data to convert to csv file
    split = area.text.splitlines()

    ranking.append(split[0])
    brand.append(split[1])
    product.append(split[2])
    price.append(split[3])

    # print(area.text)

    # End with ranking 999
    if int(split[0]) == 999:
        toCSV()

# Convert to CSV file
def toCSV():
    df = pd.DataFrame()
    df["Ranking"] = ranking
    df["Brand"] = brand
    df["Product"] = product
    df['Price'] = price

    df.to_excel("musinsa.xlsx", index=False)
    df.to_csv('musinsa.csv', encoding='utf-8-sig')

    exit(0)

# Get the Musinsa ranking page from 1 to 100 (Ranking : 1 ~ 999)
for i in range(1, 101):
    # Musinsa ranking page link
    url = 'https://global.musinsa.com/us/trending/items?gad_source=1&gclid=CjwKCAiAkp6tBhB5EiwANTCx1F6-ntsnbMrAVlY1Nxnw83buXk1fT26Buh9sW4TJ0MdrMjN_rrvwABoCmL8QAvD_BwE&page={}&sex=F&toggleCountry=us&utm_content=musinsa__231201__-mdupus0167______'.format(i)

    # Web Scrapping using Selenium
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
        driver.get(url)

        # Waiting for page loading
        driver.implicitly_wait(10)

        # Get data
        for i in range(1, 8):
            for j in range(1, 5):
                getData(i, j)

        # Position the page for automatic scrolling
        for i in range(2):
            webdriver.ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(2)

        # Use automatic scrolling to get data, scroll by 471
        for i in range(17):
            current_scroll_position = driver.execute_script("return window.scrollY;") # 현재 스크롤 위치
            driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position + 471)) # 스크롤 다운
            time.sleep(2)

            # Get data
            for j in range(1, 5):
                getData(7, j)