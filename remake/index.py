# module
import json
from modules.Chrome import Chrome

# get franchise list from ./franchise_list.json
with open('franchise_list.json') as json_file:
    franchise_list = json.load(json_file)

# print franchise list
# print(franchise_list)

driver_list = {}

plus_data = []
sale_data = []

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
    create_franchise_object(name, driver)

def create_franchise_object(name, driver):

    # import franchise class
    path = 'franchise.' + name
    module = __import__(path, fromlist=[name])

    # create franchise object
    instance = getattr(module, name)(driver)

    # call function
    get_data(instance)

def get_data(instance):

    # run get_data function
    plus_data.append(instance.get_plus_data())

    # exception => not exist sale data
    try:
        sale_data.append(instance.get_sale_data())
    except:
        return

# module
import time
import multiprocessing

# start time
start_time = time.time()

# start to multiprocessing
if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    pool.map(open_chrome, franchise_list)
    pool.close()
    pool.join()

    # end time
    end_time = time.time() - start_time

    # check time for getting data
    print(end_time)

    res = []
    
    # combinate plus_data & sale_data in res array
    res.extend(plus_data)
    res.extend(sale_data)
    print(res)
    from modules import Insert_check
    from modules import Sort_items
    from modules import Insert_data

    # check for insert data
    ans = Insert_check.func(res)

    # sort data
    res = Sort_items.func(res)

    # insert data
    if ans == "Y" or ans == "y":
        Insert_data.func(res)






