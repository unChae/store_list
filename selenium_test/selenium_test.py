import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
#실제 크롬창을 띄울려면 False
#options.headless = True
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)

#gs25
browser.get("http://gs25.gsretail.com/gscvs/ko/products/event-goods#;")

time.sleep(3)
# 1+1, 1+2 클릭 반복문
cw_plus = browser.find_element_by_css_selector(".myptab").find_elements_by_tag_name("li")
for plus in cw_plus:
    if "덤" in plus.text:
        break
    # 마지막 페이지 조회
    cw_last_page = browser.find_element_by_css_selector(".paging").find_element_by_css_selector(".next2")
    cw_last_page.click()

    time.sleep(3)

    _last_page = browser.find_element_by_css_selector(".paging").find_elements_by_tag_name("a")
    pages = []
    for page in _last_page:
        try:
            if int(page.text) > 0:
                pages.append(int(page.text))
        except:
            continue
    last_page = max(pages)
    
    # 내부 아이템 크롤링
    cw_prev_page = browser.find_element_by_css_selector(".paging").find_element_by_css_selector(".prev")
    for i in range(last_page - 1):

        tag_names = browser.find_element_by_css_selector(".prod_list").find_elements_by_tag_name("li")
        for tag in tag_names:
            print(tag.text.split("\n"))
        
        browser.execute_script("return goodsPageController.moveControl(-1)")
        time.sleep(1)

    plus.click()
    time.sleep(3)

# tag_names = browser.find_element_by_css_selector(".prod_list").find_elements_by_tag_name("li")
# for tag in tag_names:
#     print(tag.text.split("\n"))

# #cu
# browser.get("https://cu.bgfretail.com/event/plus.do")

# time.sleep(3)
# tag_names = browser.find_element_by_css_selector(".relCon").find_elements_by_tag_name("li")
# for tag in tag_names:
#     print(tag.text.split("\n"))

# #emart24
# browser.get("https://emart24.co.kr/product/eventProduct.asp")

# time.sleep(3)
# tag_names = browser.find_element_by_css_selector(".categoryListNew").find_elements_by_tag_name("li")
# for tag in tag_names:
#     print(tag.text.split("\n"))