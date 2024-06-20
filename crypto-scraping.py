from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import URLError
from time import sleep
import numpy as np

try:
    urlinput = input("please enter a link : ")
    html = urlopen("https://"+urlinput)
    bs = BeautifulSoup(html.read(), 'lxml')
    
    # استخراج تمام ردیف‌های جدول
    table_rows = bs.find_all('div', {'class': 'valuta'})
    
    prices = []
    
    # استخراج و تبدیل قیمت‌ها به اعداد شناور
    for i in range(len(table_rows)):
        price_string = table_rows[i].get_text().replace('$', '').replace(' ', '').replace('\n', '').replace(',', '')
        try:
            price = float(price_string)
            prices.append(price)
        except ValueError:
            continue  # در صورتی که تبدیل به عدد امکان‌پذیر نباشد، ادامه دهید
    
    # تقسیم قیمت‌ها به دسته‌های پنج تایی و محاسبه میانگین هر دسته
    for i in range(0, len(prices), 5):
        batch = prices[i:i + 5]
        if batch:
            average_price = np.mean(batch)
            print(f"Batch {i // 5 + 1}: {batch}")
            print(f"Average price: {average_price}")
            print("******************************************")

except URLError as e:
    print("you should connect to the internet")
    sleep(1)

print("*-----------------------------------------------------------------*")
