#Challenge: Search in a Rotated List
#Problem statement#
#Given a sorted list of n integers that has been rotated an unknown number of times, write some code to find an element in the list. 
#You may assume that the list was originally sorted in an ascending order.
def pivoted_binary_search(lst, n, key):
    """
    Function to search key in a list
    :param lst: A list of integers
    :param n: The size of the list
    :param key: A key to be searched in the list
    """
    min_element = lst[0]
    
    for i in range(1,len(lst)):
        if lst[i]<min_element:
            min_index = i
            min_element = lst[i]
    if min_index == 0: # list already sorted
        key_index = binary_search(lst, 0, len(lst), key)
        return key_index
    if min_index>0 and key > min_element: # search to the right of the minimum index
        key_index = binary_search(lst, min_index, len(lst)-1, key)
        if key_index == -1: # if it is not on the right it is on the left side
            key_index = binary_search(lst, 0, min_index, key)
            return key_index
        else:
            return key_index
    return -1 # if the key is not at all in the list

def binary_search(lst, left, right, key):
  
    """
    Binary search function
    :param lst: lst of unsorted integers
    :param left: Left sided index of the list
    :param right: Right sided index of the list
    :param key: A key to be searched in the list
    """
    while left<=right:
        mid = (left+right)//2
    
        if key==lst[mid]:
            return mid
        if key<lst[mid]:
            right = mid-1
        else:
            left = mid + 1
    return -1
