from modules import Format
import time

class EMART24(object):
    def __init__(self, driver):
        self.driver = driver

    def get_plus_data(self):
        driver = self.driver

        check = True
        result_item = []
        
        while check:
            time.sleep(2)
            items = driver.find_element_by_css_selector(".categoryListNew").find_elements_by_tag_name("li")
            
            # 다음 페이지가 없으면 종료
            if check == driver.find_element_by_css_selector(".paging .on").get_attribute('textContent'):
                check = False
                continue
            check = driver.find_element_by_css_selector(".paging .on").get_attribute('textContent')

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
                price = Format.price(price)
                try:
                    img = item.find_element_by_css_selector(".box .productImg").find_element_by_tag_name("img").get_attribute('src')
                except:
                    img = ""
                print("EMART24:", [title, price, plus, img])
                result_item.append([title, price, plus, img])

            cw_next = driver.find_element_by_css_selector(".paging .next")
            cw_next.click()
                
        return result_item

    def get_sale_data(self):
        driver = self.driver 
        driver.execute_script("return goTab('SALE')")

        check = True
        result_item = []

        while check:
            time.sleep(2)
            items = driver.find_element_by_css_selector(".categoryListNew").find_elements_by_tag_name("li")

            # 다음 페이지가 없으면 종료
            if check == driver.find_element_by_css_selector(".paging .on").get_attribute('textContent'):
                check = False
                continue
            check = driver.find_element_by_css_selector(".paging .on").get_attribute('textContent')

            for item in items:
                title  = item.find_element_by_css_selector(".box .productDiv").get_attribute('textContent')
                price  = item.find_element_by_css_selector(".box .price").get_attribute('textContent').split('\xa0')
                s_price = int(Format.price(price[1][4:]))
                price = int(Format.price(price[0]))
                rate = 100 - int(s_price/price*100)
                try:
                    img = item.find_element_by_css_selector(".box .productImg").find_element_by_tag_name("img").get_attribute('src')
                except:
                    img = ""
                print("EMART24:", [title, price, rate, img, s_price])
                result_item.append([title, price, rate, img, s_price])

            cw_next = driver.find_element_by_css_selector(".paging .next")
            cw_next.click()
                
        return result_item