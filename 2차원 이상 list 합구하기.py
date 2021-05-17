lst = [[1,[1,1,1,1],1],[1,1,1]]

def sum_list(lst, res=0):
    for i in lst:
        if type(i) ==list:
            res +=sum_list(i)
        else:
            res += i
    return res

print(sum_list(lst))
