from franchise.modules import fm

def gs(driver, tab, time):
    driver.switch_to_window(tab)

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
            price = fm.price(price)
            try:
                img = item_images[index].get_attribute('src')
            except:
                img = "https://vignette.wikia.nocookie.net/asher-altens/images/3/3b/112815953-stock-vector-no-image-available-icon-flat-vector.jpg/revision/latest?cb=20200517192640"
            print([title, price, plus, img])
            result_item.append([title, price, plus, img])

        driver.execute_script("return goodsPageController.moveControl(1)")
        time.sleep(2)
            
    return result_item