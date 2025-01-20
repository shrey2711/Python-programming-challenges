def find_closest(lst,target):
    
    min = float('inf')
    index = 0
    for i in range(0,len(lst)):
        if abs(lst[i]-target)<min:
            min = abs(lst[i]-target)
            index = i
    return lst[index]
