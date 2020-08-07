import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from franchise import plus_cu, plus_emart, plus_gs, plus_seven
from franchise import sale_emart

#chromedriver 경로 설정
CHROMEDRIVER_PATH = './chromedriver.exe'

chrome_options = Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("disable-gpu")

#브라우저 실행 및 탭 추가
driver = webdriver.Chrome( executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options )
driver.execute_script('window.open("about:blank", "_blank");')
driver.execute_script('window.open("about:blank", "_blank");')

tabs = driver.window_handles

# TAB_1
driver.switch_to_window(tabs[0])
driver.get('https://cu.bgfretail.com/event/plus.do')
 
# TAB_2
driver.switch_to_window(tabs[1])
driver.get('http://gs25.gsretail.com/gscvs/ko/products/event-goods')
 
# TAB_3
driver.switch_to_window(tabs[2])
driver.get('https://emart24.co.kr/product/eventProduct.asp')

time.sleep(1)
res = []
startTime = time.time()

# 1+1 2+1 3+1
res.append(plus_emart.getData(driver, tabs[2], time))
res.append(plus_cu.getData(driver, tabs[0], time))
res.append(plus_gs.getData(driver, tabs[1], time))

# sale
res.append(sale_emart.getData(driver, tabs[2], time))

from franchise.modules import insert_check
from franchise.modules import sort_items
from franchise.modules import insert_data

endTime = time.time() - startTime
print("runtime for get data:", endTime)

# check for database insert data
ans = insert_check.func(res)
# sorted_res = sort_items.func(res)

if ans == "Y" or ans == "y":
    insert_data.func(res)

endTime = time.time() - startTime
print("total runtime:", endTime)