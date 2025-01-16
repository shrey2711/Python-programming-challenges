#Challenge: Find Two Numbers That Add Up to "n",
#In this problem, you have to implement the find_sum(lst, n) function which will take a list lst and number n as inputs and return two numbers from the list that add up to n.
def find_sum(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """
    num = 0
    for i in lst:
      left = 0
      right = len(lst)-1
      num = n-i
      while left<=right:
        mid = (left+right)//2
        
        if num==lst[mid]:
          return[i,lst[mid]]
        if num<lst[mid]:
          right = mid-1
        else:
          left = mid+1

