import requests
from bs4 import BeautifulSoup
#pip install pillow
from io import BytesIO

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

        header = soup.findAll("div",{"class":"card-header"})[j].get_text().replace(" ", "").replace("\n", "|").split("|")
        _header = []
        for val in header:
            if(len(val) > 0):
                _header.append(val)

        _obj.extend(_header)

        obj_result.append(_obj)

        

    print(obj_result)



