# module
import json
from modules.Chrome import Chrome

# get franchise list from ./franchise_list.json
with open('franchise_list.json') as json_file:
    franchise_list = json.load(json_file)

# print franchise list
# print(franchise_list)

driver_list = {}

def open_chrome(i):

    # data binding
    name = i["name"]
    url = i["url"]
    
    # create chrome object
    driver_list[name] = Chrome(name)

    # url setting
    driver_list[name].set_url(url)

    # get chrome driver for input parameter
    driver = driver_list[name].get_driver()

    # call function
    return create_franchise_object(name, driver)

def create_franchise_object(name, driver):

    # import franchise class
    path = 'franchise.' + name
    module = __import__(path, fromlist=[name])

    # create franchise object
    instance = getattr(module, name)(driver)

    # call function
    return get_data(instance, driver)

def get_data(instance, driver):

    _res = []
    # run get_data function
    _res.append(instance.get_plus_data())

    # exception => not exist sale data
    try:
        _res.append(instance.get_sale_data())
    except:
        driver.close()
        return _res
    driver.close()
    return _res

# module
import time
import multiprocessing

# start time
start_time = time.time()
res = []
# start to multiprocessing
if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    res.extend(pool.map(open_chrome, franchise_list))
    pool.close()
    pool.join()

    # end time
    end_time = time.time() - start_time

    # check time for getting data
    print(end_time)

    # return data ['franchise'['plus, sale'['items'['item']]]]
    # print(res)

    from modules import Insert_check
    from modules import Sort_items
    

    # sort data
    res = Sort_items.func(res)

    # check for insert data
    Insert_check.func(res)


