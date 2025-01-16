#Challenge: Dutch National Flag Problem
#Let's solve the famous problem of Dutch National Flag.
def dutch_national_flag(lst):
    i=0
    j=len(lst)-1
    mid = 0
    
    # same like the implementation in educative, have to think more of my own mehtod
    while mid<=j:
        if lst[mid] == 0:
            lst[mid],lst[i] = lst[i], lst[mid]
            i+=1
            mid+=1
        elif lst[mid]==2:
            lst[mid],lst[j] = lst[j], lst[mid]
            j-=1
        elif lst[mid]==1:
            mid+=1
    return lst
