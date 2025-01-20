#Possibility of improvement, might be slow, can be optimized further for timing puprposes

def find_peak(lst):
    
    if len(lst)==1:
        return lst
    peak=[]
    left = 0
    right = len(lst)-1
    mid = cal_midpoint(left, right)
    
    # for left half
    while left<right:
        if lst[mid-1]<=lst[mid]>=lst[mid+1]:
            if lst[mid] not in peak:
                peak.append(lst[mid])
        right=mid
        mid = cal_midpoint(left, right)
        if mid==left:
            break
    left = (0+len(lst)-1)//2
    right = len(lst)-1
    mid = cal_midpoint(left, right)
    
    #right half
    while left<right:
        if lst[mid-1]<=lst[mid]>=lst[mid+1]:
            if lst[mid] not in peak:
                peak.append(lst[mid])
        left+=1
        mid = cal_midpoint(left, right)
        if mid==right:
            break
    return max(peak)

def cal_midpoint(left,right):
    return (left+right)//2

            
# Driver to test above code
if __name__ == '__main__':
    
    lst = [42, 69, 68, 52, 93, 11]

    # Function call
    result = find_peak(lst)

    if result != -1:
        print("Maximum peak is: ", result)
    else:
        print("Error!")
