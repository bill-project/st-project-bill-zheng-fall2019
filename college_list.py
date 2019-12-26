import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.payscale.com/college-salary-report/bachelors/page/1")

soup = BeautifulSoup(page.content, 'html.parser')

income_list = []
names = soup.find_all("div", class_="pxl-hidden-sm-down text-center")
for name in names:
    atag = name.find("span")
    print(atag.text)
    income_list.append(atag.text)


image_list = []
names = soup.find_all("div", class_="datatable-logo__img")
for name in names:
    atag = name.find("img")
    print(atag['src'])
    image_list.append(atag['src'])

name_list = []
names = soup.find_all("div", class_="datatable-logo__text")
for name in names:
    atag = name.find("a")
    print(atag.text)
    name_list.append(atag.text)

college_list = []
for i in range(len(name_list)):
    col = {
        "name" : name_list[i],
        "image" : image_list[i]
    }
    college_list.append(col)

print(college_list)