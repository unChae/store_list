from modules import format

def getData(driver, tab, time):
    driver.switch_to_window(tab)

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
            s_price = int(format.price(price[1][4:]))
            price = int(format.price(price[0]))
            rate = 100 - int(s_price/price*100)
            try:
                img = item.find_element_by_css_selector(".box .productImg").find_element_by_tag_name("img").get_attribute('src')
            except:
                img = ""
            print([title, price, rate, img, s_price])
            result_item.append([title, price, rate, img, s_price])

        cw_next = driver.find_element_by_css_selector(".paging .next")
        cw_next.click()
            
    return result_item