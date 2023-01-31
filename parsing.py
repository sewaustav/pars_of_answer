import requests
from bs4 import BeautifulSoup as BS 


page = int(input("Введите первый номер:"))
page_final = int(input("Введите последний номер:"))
step = int(input('Введите шаг'))
count = 0

while True:

    r = requests.get("https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId="+str(page))
    html = BS(r.content, "html.parser")
    selector = html.select(".answer")

    if (len(selector)):
        for el in selector:
            title = el.select(".hidedata")
            print( title[0].text , end = " ")
        if step > 0:
            if page <= page_final:
                print(page)
                page += step
            else: break
        elif step < 0:
            if page >= page_final:
                print(page)
                page += step
            else: break
            
    else: break