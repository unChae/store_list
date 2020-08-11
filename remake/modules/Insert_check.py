# insert check
# db에 입력할 것인지 안할 것인지 확인

# module
import sys
import json

def func(items):
    franchise_list = []
    # get franchise list from ./franchise_list.json
    with open('franchise_list.json') as json_file:
        franchise_list = json.load(json_file)

    ans = ""
    for i in items:
        idx = items.index(i)
        name = franchise_list[idx]["name"]
        print(name, "plus:", len(i[0]))
        try:
            print(name, "sale:", len(i[1]))
        except:
            continue

    print("Do you want to insert data?(y or n)")
    while (ans == "y" or ans == "n" or ans == "Y" or ans == "N") == False:
        ans = sys.stdin.readline()
        ans = ans.replace("\n", "")
    return ans