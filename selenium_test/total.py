import time
from multiprocessing import Pool

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

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

def cu():
    driver.switch_to_window(tabs[0])

    result_item = []
    while True:
        try:
            driver.find_element_by_css_selector(".prodListBtn .prodListBtn-w").find_element_by_tag_name("a")
            driver.execute_script("return nextPage(1)")
            time.sleep(3)
        except:
            break

    items = driver.find_element_by_css_selector(".prodListWrap").find_elements_by_tag_name("ul > li")
    for item in items:
        try:
            img = item.find_element_by_css_selector(".photo").find_element_by_tag_name("img").get_attribute('src')
            title = item.find_element_by_css_selector(".prodName").get_attribute('textContent')
            price = item.find_element_by_css_selector(".prodPrice").find_element_by_tag_name("span").get_attribute('textContent')
            plus = item.find_element_by_tag_name("ul li").get_attribute('textContent')
            print([title, price, plus, img])
            result_item.append([title, price, plus, img])
        except:
            continue
        
    return result_item  

def gs():
    driver.switch_to_window(tabs[1])

    cw_plus = driver.find_element_by_css_selector(".myptab").find_elements_by_tag_name("li")

    cw_plus[3].click()
    time.sleep(2)

    # 내부 아이템 크롤링
    check = True
    result_item = []

    while check:
        time.sleep(2)
        items = driver.find_element_by_css_selector(".prod_list").find_elements_by_tag_name("li")
        item_images = driver.find_element_by_css_selector(".prod_list").find_elements_by_tag_name("img")
        try:
            driver.find_element_by_css_selector(".paging .num .on").get_attribute('textContent')
        except:
            check = False
            continue

        for index, item in enumerate(items):

            plus  = item.find_element_by_css_selector(".prod_box .flag_box").get_attribute('textContent')
            if plus == "덤증정":
                continue

            title  = item.find_element_by_css_selector(".prod_box .tit").get_attribute('textContent')
            price  = item.find_element_by_css_selector(".prod_box .price").get_attribute('textContent')
            price = price.split("원")[0]
            try:
                img = item_images[index].get_attribute('src')
            except:
                img = "no_image"
            print([title, price, plus, img])
            result_item.append([title, price, plus, img])

        driver.execute_script("return goodsPageController.moveControl(1)")
        time.sleep(2)
            
    return result_item

def emart():
    driver.switch_to_window(tabs[2])

    check = True
    result_item = []

    while check:
        time.sleep(2)
        items = driver.find_element_by_css_selector(".categoryListNew").find_elements_by_tag_name("li")

        # 다음 페이지가 없으면 종료
        try:
            driver.find_element_by_css_selector(".paging .on").get_attribute('textContent')
        except:
            check = False
            continue

        for item in items:

            try:
                plus  = item.find_element_by_css_selector(".box .txt").find_element_by_tag_name("img").get_attribute('alt')
            except:
                plus  = item.find_element_by_css_selector(".box .txtNo").find_element_by_tag_name("img").get_attribute('alt')          
            try:
                first = int(plus.split("+")[0])
                second = 1
                plus = str(first) + "+" + str(second)
            except:
                continue

            title  = item.find_element_by_css_selector(".box .productDiv").get_attribute('textContent')
            price  = item.find_element_by_css_selector(".box .price").get_attribute('textContent').split('\xa0')[0]
            try:
                img = item.find_element_by_css_selector(".box .productImg").find_element_by_tag_name("img").get_attribute('src')
            except:
                img = "no_image"
            print([title, price, plus, img])
            result_item.append([title, price, plus, img])

        cw_next = driver.find_element_by_css_selector(".paging .next")
        cw_next.click()
        time.sleep(2)
            
    return result_item

result = [0, 0, 0]
result[0] = cu()
result[1] = gs()
result[2] = emart()

driver.close()