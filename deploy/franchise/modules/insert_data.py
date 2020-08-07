# data insert
import requests
from io import BytesIO
from datetime import datetime
import calendar
from franchise.modules import format

# url 정보 가져오기
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

def func(res):
    for i, x in enumerate(res):
        for y in x:
            print("item", y)
            
            url = config['URL']['TEST']
            # url = config['URL']['SERVER']

            #img
            image_url = y[3]
            res = requests.get(image_url)
            multiple_files = [
                ('bf_file[0]', ('product.jpeg', BytesIO(res.content), 'image/png')),
            ]
    
            # get month
            month = datetime.today().month
            year = datetime.today().year
            last_day = calendar.monthrange(year, month)[1]

            # day month formatting
            last_day = fm.check_zero(last_day)
            month = fm.check_zero(month)

            # franchise
            if i == 0:
                wr_10 = 74
            elif i == 1:
                wr_10 = 72
            elif i == 2:
                wr_10 = 71
            else:
                wr_10 = 74

            if i < 3:
                # first&second
                first, second = y[2].split("+")

                data = {
                    'w': '',
                    'bo_table':'item',
                    'ca_name':'프랜차이즈',
                    'wr_10': wr_10,
                    'wr_subject':y[0],
                    'wr_2':y[1],
                    'wr_3[chk]':'on',
                    'wr_3[first]':first,
                    'wr_3[last]':second,
                    'wr_4[first]':'',
                    'wr_4[last]':'',
                    'wr_5':'2020-'+month+'-01',
                    'wr_6':'2020-'+month+'-'+last_day
                }
            else:
                data = {
                    'w': '',
                    'bo_table':'item',
                    'ca_name':'프랜차이즈',
                    'wr_10': wr_10,
                    'wr_subject':y[0],
                    'wr_2':y[1],
                    'wr_3[first]':'',
                    'wr_3[last]':'',
                    'wr_4[chk]':'on',
                    'wr_4[first]':y[2],
                    'wr_4[last]':y[4],
                    'wr_5':'2020-'+month+'-01',
                    'wr_6':'2020-'+month+'-'+last_day
                }
            requests.post(url, data=data, files=multiple_files)