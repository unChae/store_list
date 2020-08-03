#gs25

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
#실제 크롬창을 띄울려면 False
#options.headless = True
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)

browser.get("http://gs25.gsretail.com/gscvs/ko/products/event-goods")

time.sleep(3)

cw_plus = browser.find_element_by_css_selector(".myptab").find_elements_by_tag_name("li")

cw_plus[1].click()
time.sleep(2)

# 내부 아이템 크롤링
check = True
result_item = []

while check:
    time.sleep(2)
    items = browser.find_element_by_css_selector(".prod_list").find_elements_by_tag_name("li")
    item_images = browser.find_element_by_css_selector(".prod_list").find_elements_by_tag_name("img")
    try:
        last_page = browser.find_element_by_css_selector(".paging .num .on").get_attribute('textContent')
    except:
        check = False
        continue
    print(last_page)
    for index, item in enumerate(items):

        plus  = item.find_element_by_css_selector(".prod_box .flag_box").get_attribute('textContent')
        if plus == "덤증정":
            continue

        title  = item.find_element_by_css_selector(".prod_box .tit").get_attribute('textContent')
        price  = item.find_element_by_css_selector(".prod_box .price").get_attribute('textContent')
        try:
            img = item_images[index].get_attribute('src')
        except:
            img = "no_image"
        a = []
        a.append(title)
        a.append(price)
        a.append(plus)
        a.append(img)
        result_item.append(a)

    browser.execute_script("return goodsPageController.moveControl(1)")
    time.sleep(2)
        
print(result_item)