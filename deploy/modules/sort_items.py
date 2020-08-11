# sort 
# 1+1 2+1 3+1 순서 대로 정렬

def func(items):
    res = []
    for v in items:
        res.append(sorted(v, key = lambda v: v[2]))
    return res         
