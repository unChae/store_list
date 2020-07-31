import requests

url = "http://52.79.94.232/admin/_ajax_board_update.php"

data = {
    'w': '',
    'bo_table':'item',
    'ca_name':'프랜차이즈',
    'wr_10':78,
    'wr_subject':'이니스프리 테스트 상품',
    'wr_2':1000,
    'bf_file[0]': '',
    'wr_3[chk]':'on',
    'wr_3[first]':1,
    'wr_3[last]':2,
    'wr_4[first]':'',
    'wr_4[last]':'',
    'wr_5':'2020-07-13',
    'wr_6':'2020-08-16'
}
r = requests.post(url, data=data)

print(r.text)