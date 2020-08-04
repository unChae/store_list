import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from franchise import p_cu, p_emart, p_gs
from franchise import s_emart

#chromedriver 경로 설정
CHROMEDRIVER_PATH = './chromedriver.exe'

chrome_options = Options()
chrome_options.add_argument('--start-maximized')

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
res = {}

# 1+1 2+1 3+1
res["p_emart"] = p_emart.emart(driver, tabs[2], time)
res["p_cu"] = p_cu.cu(driver, tabs[0], time)
res["p_gs"] = p_gs.gs(driver, tabs[1], time)

# sale
res["s_emart"] = s_emart.emart(driver, tabs[2], time)

print(res)

driver.close()