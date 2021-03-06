# data insert

# module
import requests
from io import BytesIO
from datetime import datetime
import calendar
from modules import Format
import json

# url 정보 가져오기
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

url = config['URL']['TEST']
# url = config['URL']['SERVER']

# get franchise list from ./franchise_list.json
with open('franchise_list.json') as json_file:
    franchise_list = json.load(json_file)

def func(res, index):

    # franchise
    wr_10 = franchise_list[index]["id"]
    i = 0
    
    length = len(res)
    if length == 1:
        length = False

    for y in res:
        # y = plus or sale item list

        # plus == 0 or sale == 1
        idx = i

        for z in y:

            print("item", z)      

            #img
            image_url = z[3]
            res = requests.get(image_url)
            multiple_files = [
                ('bf_file[0]', ('product.jpeg', BytesIO(res.content), 'image/png')),
            ]
    
            # get month
            month = datetime.today().month
            year = datetime.today().year
            last_day = calendar.monthrange(year, month)[1]

            # day month formatting
            last_day = Format.check_zero(last_day)
            month = Format.check_zero(month)

            if length == False:
                # plus만 있는 경우

                # first&second
                first, second = z[2].split("+")

                data = {
                    'w': '',
                    'bo_table':'item',
                    'ca_name':'프랜차이즈',
                    'wr_10': wr_10,
                    'wr_subject':z[0],
                    'wr_2':z[1],
                    'wr_3[chk]':'on',
                    'wr_3[first]':first,
                    'wr_3[last]':second,
                    'wr_4[first]':'',
                    'wr_4[last]':'',
                    'wr_5':'2020-'+month+'-01',
                    'wr_6':'2020-'+month+'-'+last_day
                }
            else:
                if idx == 0:
                    # sale
                    data = {
                        'w': '',
                        'bo_table':'item',
                        'ca_name':'프랜차이즈',
                        'wr_10': wr_10,
                        'wr_subject':z[0],
                        'wr_2':z[1],
                        'wr_3[first]':'',
                        'wr_3[last]':'',
                        'wr_4[chk]':'on',
                        'wr_4[first]':z[2],
                        'wr_4[last]':z[4],
                        'wr_5':'2020-'+month+'-01',
                        'wr_6':'2020-'+month+'-'+last_day
                    }
                else:
                    # plus

                    # first&second
                    first, second = z[2].split("+")

                    data = {
                        'w': '',
                        'bo_table':'item',
                        'ca_name':'프랜차이즈',
                        'wr_10': wr_10,
                        'wr_subject':z[0],
                        'wr_2':z[1],
                        'wr_3[chk]':'on',
                        'wr_3[first]':first,
                        'wr_3[last]':second,
                        'wr_4[first]':'',
                        'wr_4[last]':'',
                        'wr_5':'2020-'+month+'-01',
                        'wr_6':'2020-'+month+'-'+last_day
                    }
            
            requests.post(url, data=data, files=multiple_files)
        i = i + 1
