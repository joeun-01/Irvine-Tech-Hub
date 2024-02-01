import pandas as panda
import matplotlib.pyplot as plt

# Read CSV file
csv = panda.read_csv('/Users/joeun/PycharmProjects/WebScraping/part 1/musinsa.csv')
# print(csv)

# Make datafram from CSV file
data = panda.DataFrame(csv)
# print(data)

# 1. Which brands are the most popular? - TOP 10

# Group by brand
brand = data.groupby('Brand')['Ranking'].count().reset_index()
brand = brand.rename(columns={'Ranking': 'Count'})  # Renamed 'Ranking' column to 'Brand_Count'

# Pick the top 10 brands and count the number of times they appear in the ranking
tenth = brand.nlargest(10, 'Count', keep='all').reset_index()
# print(tenth)

# Visualize the data with the bar graph
tenth.plot(kind='bar', x='Brand', y='Count')
plt.title('Musinsa Brand Top 10')
plt.rc(group='font', family='Arial')
plt.xlabel('Brand')
plt.ylabel('Count')
plt.show()

# 2. How much will the price affect the ranking?

# 2-1. Find the price that most appeared in the ranking

# Remove the dollar mark and change it to int type
data['Price'] = data['Price'].str.replace("$", '').astype(int)

# Count the number of appearances in the ranking by price range
price = data.groupby(panda.cut(data['Price'], [0, 20, 40, 60, 80, 100, 1000])).size().reset_index(name='Count')
# print(price)

# Visualize the data with the line graph
price.plot(kind='line', x='Price', y='Count')
plt.title('Musinsa Price')
plt.rc(group='font', family='Arial')
plt.xlabel('Price')
plt.ylabel('Count')
plt.show()

# 2-2. Find the median price, standard deviation, and average for each ranking range
price_range = panda.cut(data['Ranking'], [0, 200, 400, 600, 800, 1000])
group_range = data.groupby(price_range)

group_median = []
group_std = []
group_average = []

# Find the median, standard deviation, and mean of each range
for group_name, group_data in group_range:
    group_median.append(group_data['Price'].median())  # 중앙값
    group_std.append(group_data['Price'].std())  # 표준편차
    group_average.append(group_data['Price'].sum() / len(group_data))  # 평균

price_data = panda.DataFrame()
price_data["Median"] = group_median
price_data["Standard Deviation"] = group_std
price_data["Average"] = group_average

# Create DataFrame
price_data.index = ['0-200', '200-400', '400-600', '600-800', '800-1000']
# print(price_data)

# Visualize the data with the bar graph
price_data.plot(kind='bar')
plt.title('Price data by ranking')
plt.rc(group='font', family='Arial')
plt.xlabel('Range')
plt.ylabel('Price Data')
plt.show()