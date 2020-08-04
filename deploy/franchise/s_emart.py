from franchise.modules import fm

def emart(driver, tab, time):
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
            s_price = int(fm.price(price[1][4:]))
            price = int(fm.price(price[0]))
            rate = 100 - int(s_price/price*100)
            try:
                img = item.find_element_by_css_selector(".box .productImg").find_element_by_tag_name("img").get_attribute('src')
            except:
                img = "https://vignette.wikia.nocookie.net/asher-altens/images/3/3b/112815953-stock-vector-no-image-available-icon-flat-vector.jpg/revision/latest?cb=20200517192640"
            print([title, price, rate, s_price, img])
            result_item.append([title, price, rate, s_price, img])

        cw_next = driver.find_element_by_css_selector(".paging .next")
        cw_next.click()
            
    return result_item