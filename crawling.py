import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://pyony.com/search/")
soup = BeautifulSoup(webpage.content, "html.parser")

# 마지막 페이지 추출
page = soup.findAll("a", {"class":"page-link"})
last_page = page[len(page)-1].get('href')
_last_page = last_page.replace("?page=","")
    
print("last page", _last_page)

for x in range(1, int(_last_page)):
    webpage = requests.get("https://pyony.com/search/?page="+str(x))
    soup = BeautifulSoup(webpage.content, "html.parser") 

    obj_result = []
    for j in range(0,20):
        obj = soup.findAll("div",{"class":"card-body"})[j].get_text().replace(" ", "").replace("\n", "|").split("|")
        _obj = []
        i = 0
        for val in obj:
            if(val):
                if(i < 4):
                    _obj.append(val)
                    i = i+1
        obj_result.append(_obj)
            
    img = soup.findAll("img",{"class":"prod_img"})

    for inx, val in enumerate(img):
        img[inx] = val.get('src')

    for inx, val in enumerate(obj_result):
        obj_result[inx].append(img[inx])
    print(obj_result)




