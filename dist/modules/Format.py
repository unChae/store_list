def price(n):
    return n.replace(",","")

def check_zero(n):
    if n < 10:
        n = "0" + str(n)
    else:
        n = str(n)
    return n