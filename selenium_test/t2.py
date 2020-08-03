# emart24

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
#실제 크롬창을 띄울려면 False
#options.headless = True
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)

#gs25
browser.get("https://emart24.co.kr/product/eventProduct.asp")

time.sleep(3)

# 내부 아이템 크롤링
check = True
result_item = []

while check:
    time.sleep(2)
    items = browser.find_element_by_css_selector(".categoryListNew").find_elements_by_tag_name("li")
    try:
        last_page = browser.find_element_by_css_selector(".paging .on").get_attribute('textContent')
    except:
        check = False
        continue
    print(last_page)
    for index, item in enumerate(items):

        try:
            plus  = item.find_element_by_css_selector(".box .txt").find_element_by_tag_name("img").get_attribute('alt')
        except:
            plus  = item.find_element_by_css_selector(".box .txtNo").find_element_by_tag_name("img").get_attribute('src')          
        # if plus == "덤증정":
        #     continue

        title  = item.find_element_by_css_selector(".box .productDiv").get_attribute('textContent')
        price  = item.find_element_by_css_selector(".box .price").get_attribute('textContent').split('\xa0')[0]
        try:
            img = item.find_element_by_css_selector(".box .productImg").find_element_by_tag_name("img").get_attribute('src')
        except:
            img = "no_image"
        a = []
        a.append(title)
        a.append(price)
        a.append(plus)
        a.append(img)
        print(a)
        result_item.append(a)

    cw_next = browser.find_element_by_css_selector(".paging .next")
    cw_next.click()
    time.sleep(2)
        
print(result_item)