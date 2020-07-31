import requests
from bs4 import BeautifulSoup
#pip install pillow
from io import BytesIO
from datetime import datetime
import calendar

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
            
    img = soup.findAll("img",{"class":"prod_img"})

    for inx, val in enumerate(img):
        img[inx] = val.get('src')

    for inx, val in enumerate(obj_result):
        obj_result[inx].append(img[inx])
        url = "http://52.79.94.232/admin/_ajax_board_update.php"
        image_url = img[inx]
        res = requests.get(image_url)
        multiple_files = [
            ('bf_file[0]', ('test.jpeg', BytesIO(res.content), 'image/png')),
        ]

        #formatting

        #first&second
        first, second = val[3].split("+")
        
        #get month
        month = val[6].split(".")[0]
        year = datetime.today().year
        last_day = calendar.monthrange(year, int(month))[1]
        if last_day < 10:
            last_day = "0" + str(last_day)
        else:
            last_day = str(last_day)

        wr_10 = 71
        #get wr_10
        if 'CU' in val[4]:
            wr_10 = 72
        elif 'GS' in val[4]:
            wr_10 = 71
        elif 'MINI' in val[4]:
            #현재 db에 미니스탑이 없기에 gs에 입력
            wr_10 = 71
        elif 'EMART' in val[4]:
            wr_10 = 74
        elif 'ELEVEN' in val[4]:
            #현재 db에 세븐일레븐이 없기에 gs에 입력
            wr_10 = 71
        
        data = {
            'w': '',
            'bo_table':'item',
            'ca_name':'프랜차이즈',
            'wr_10': wr_10,
            'wr_subject':val[0],
            'wr_2':val[1],
            'wr_3[chk]':'on',
            'wr_3[first]':first,
            'wr_3[last]':second,
            'wr_4[first]':'',
            'wr_4[last]':'',
            'wr_5':'2020-'+month+'-01',
            'wr_6':'2020-'+month+'-'+last_day
        }
        r = requests.post(url, data=data, files=multiple_files)

        print(val[0],":",r.text)

    #print(obj_result)



