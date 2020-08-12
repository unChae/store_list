from modules import Format
import time

class CU(object):
    def __init__(self, driver):
        self.driver = driver

    def get_plus_data(self):
        driver = self.driver

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
                price = Format.price(price)
                plus = item.find_element_by_tag_name("ul li").get_attribute('textContent')
                print("CU:", [title, price, plus, img])
                result_item.append([title, price, plus, img])
            except:
                continue
            
        return result_item  
