# insert check
# db에 입력할 것인지 안할 것인지 확인
import sys

def func(items):
    ans = ""
    print("emart24:", len(items[0]))
    print("cu:", len(items[1]))
    print("gs:", len(items[2]))
    print("emart24 sale", len(items[3]))
    print("Do you want to insert data?(y or n)")
    while (ans == "y" or ans == "n" or ans == "Y" or ans == "N") == False:
        ans = sys.stdin.readline()
        ans = ans.replace("\n", "")
    return ans