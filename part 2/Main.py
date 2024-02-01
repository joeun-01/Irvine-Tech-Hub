import pandas as panda
import matplotlib.pyplot as plt

csv = panda.read_csv('/Users/joeun/PycharmProjects/WebScraping/part 1/musinsa.csv')
# print(csv)

data = panda.DataFrame(csv)
# print(data)

# 달러 표시를 제거
data['Price'] = data['Price'].str.replace("$", '').astype(int)

# 어떤 브랜드가 가장 인기가 많을까?
# 상위 10위 브랜드 구하기
# 브랜드별로 묶기
brand = data.groupby('Brand')['Ranking'].count().reset_index()
brand = brand.rename(columns={'Ranking': 'Count'})  # 'Ranking' 열의 이름을 'Brand_Count'로 변경
# print(brand)

tenth = brand.nlargest(10, 'Count', keep='all').reset_index()
# print(tenth)

tenth.plot(kind='bar', x='Brand', y='Count')
plt.title('Musinsa Brand Top 10')
plt.rc(group='font', family='Arial')
plt.xlabel('Brand')
plt.ylabel('Count')
plt.show()

# 가격이 주는 순위 영향
# # 가장 비율이 높은 가격 구하기
# # 가격별로 묶기
# # print(data)

# 가격 평균 중앙값 표준편차
print(data['Price'].median())  # 중앙값
print(data['Price'].std())  # 표준편차
print(data['Price'].sum() / 999)  # 평균
print(data['Price'].min())  # 최소
print(data['Price'].max())  # 최대

# 'Price' 열을 범위에 따라 나누고, 각 범위의 데이터 갯수를 세기
price = data.groupby(panda.cut(data['Price'], [0, 25, 50, 75, 100, 1000])).size().reset_index(name='Count')
print(price)

price.plot(kind='bar', x='Price', y='Count')
plt.title('Musinsa Price')
plt.rc(group='font', family='Arial')
plt.xlabel('Price')
plt.ylabel('Count')
plt.show()