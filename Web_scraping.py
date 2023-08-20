from bs4 import BeautifulSoup as bs
import requests

url = 'https://www.flipkart.com/search?q=bicycles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

page_data = requests.get(url)
print(page_data)

show_html = bs(page_data.content,'html.parser')
print(show_html.prettify())

bicycle_names = show_html.find_all('a',class_ = "s1Q9rs" )
print(bicycle_names)

print('\n\n\n')

names=[]
for i in range(0,len(bicycle_names)):
    names.append(bicycle_names[i].get_text())
print(names)

print('\n\n\n')
cost = show_html.find_all('div', class_="_30jeq3")
print(cost)

print('\n\n\n')

price=[]
for i in range(0,len(cost)):
    price.append(cost[i].get_text())
print(price)

price[:] = [p.lstrip('₹') for p in price]
print(price)

print('\n\n\n')

import pandas as pd
df = pd.DataFrame()

print('\n\n\n')

df['Bicycle_Name'] = names
df['Pricing(in Rs.)'] = price[:40]
print(df)


df.to_csv("Buying_bicycles.csv")



