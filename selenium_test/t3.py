# cu

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
#실제 크롬창을 띄울려면 False
#options.headless = True
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)

browser.get("https://cu.bgfretail.com/event/plus.do")

time.sleep(3)

result_item = []

while True:
    try:
        cw_more = browser.find_element_by_css_selector(".prodListBtn .prodListBtn-w").find_element_by_tag_name("a")
        browser.execute_script("return nextPage(1)")
        time.sleep(3)
    except:
        break

items = browser.find_element_by_css_selector(".prodListWrap").find_elements_by_tag_name("ul > li")
for item in items:
    try:
        img = item.find_element_by_css_selector(".photo").find_element_by_tag_name("img").get_attribute('src')
        title = item.find_element_by_css_selector(".prodName").get_attribute('textContent')
        price = item.find_element_by_css_selector(".prodPrice").find_element_by_tag_name("span").get_attribute('textContent')
        plus = item.find_element_by_tag_name("ul li").get_attribute('textContent')
        result_item.append([title, price, plus, img])
    except:
        continue
    
print(result_item)    