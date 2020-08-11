# sort 
# 1+1 2+1 3+1 순서 대로 정렬

def func(items):
    for v in items:
        v[0] = sorted(v[0], key = lambda v: v[2])
    return items         
