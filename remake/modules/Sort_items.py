# sort 
# 1+1 2+1 3+1 순서 대로 정렬

def func(items):
    for v in items:
        # make orderby rule 1+1 2+1 3+1 sale
        temp = []
        v[0] = sorted(v[0], key = lambda v: v[2])
        v[0].reverse()
        try:
            temp = v[1] 
            v[1] = v[0]
            v[0] = temp
        except:
            temp = []

    return items         
