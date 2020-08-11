from modules import Format
import time
import re

class SEVEN(object):
    def __init__(self, driver):
        self.driver = driver
        self.result_item = []

    def get_data(self):
        time.sleep(1)
        items = self.items

        plus = items[0].get_attribute('textContent')
        for i in items:
            try:
                if i.get_attribute('class') != "btn_more":
                    title = i.find_element_by_css_selector(".pic_product .infowrap .name").get_attribute('textContent')
                    price = i.find_element_by_css_selector(".pic_product .infowrap .price").get_attribute('textContent').replace("\n", "").replace("\t","")
                    price = Format.price(price)
                    try:
                        img = i.find_element_by_css_selector(".pic_product").find_element_by_tag_name("img").get_attribute('src')
                    except:
                        img = ""
                    print("SEVEN:", [title, price, plus, img])
                    self.result_item.append([title, price, plus, img])
            except:
                continue

    def open_last_list(self):
        driver = self.driver
        items = self.items
        page = True

        def change_page():
            driver.execute_script("return fncMore('" + str(self.num) + "')")
            time.sleep(1)
            return driver.find_element_by_css_selector("#listUl").find_elements_by_tag_name("li")

        while page:
            # last + component display check for find last page
            if self.num == 1:
                if ("display" in items[-1].get_attribute('style')) == True:
                    items = change_page()
                else:
                    page = False
            elif self.num == 4:
                try:
                    "float" in items[-1].find_element_by_tag_name("a").get_attribute('style')
                    items = change_page()
                except:
                    page = False
            else:
                page = False
                try:
                    "float" in items[-1].find_element_by_tag_name("a").get_attribute('style')
                    items = change_page()
                except:
                    page = False

        self.items = items

    def get_plus_data(self):
        driver = self.driver
        
        time.sleep(3)

        # setting
        self.items = driver.find_element_by_css_selector("#listUl").find_elements_by_tag_name("li")
        self.num = 1
        
        # 1+1 open last list
        self.open_last_list()

        # get data
        self.get_data()

        # change tab 2+2
        driver.execute_script("return fncTab('2')")
        time.sleep(2)

        # setting
        self.items = driver.find_element_by_css_selector("#listUl").find_elements_by_tag_name("li")
        self.num = 2

        # 2+2 open last list
        self.open_last_list()

        # get data
        self.get_data()

        return self.result_item


    def get_sale_data(self):
        driver = self.driver

        # change tab 2+2
        driver.execute_script("return fncTab('4')")
        time.sleep(2)

        # setting
        self.num = 4
        self.items = driver.find_element_by_css_selector("#listUl").find_elements_by_tag_name("li")
        
        # sale open last list
        self.open_last_list()

        # product_id list
        product_id_list = []
        for i in self.items:
            try:
                href = i.find_element_by_tag_name("a").get_attribute('href')
                product_id = re.findall("\d+", href)
                product_id_list.extend(product_id)
            except:
                continue

        for i in product_id_list:
            # move to detail page
            driver.execute_script("return fncGoView('"+ i +"')")
            time.sleep(2)

            try:
                title = driver.find_element_by_css_selector(".tit_product_view").get_attribute('textContent')
                # s_price
                # price
                # img
            except:
                continue

        
        return self.result_item
        

