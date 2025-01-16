#Challenge: Search Position
#write a function to find the appropriate position to insert a new element in a sorted list.
#Given a sorted list and a target value, return the index of the target value if the value is present in the list. 
#If the value is not present, return the index at which the value should be inserted.

#You may assume that no duplicates are in the list.

def search_insert_position(lst,value):
  left = 0
  right = len(lst)-1
  found = 0
  while left<=right:
      mid = (left+right)//2
      
      if value == lst[mid]:
          found = 1
          return mid
      if value>lst[mid]:
          left = mid+1
      else:
          right=mid-1
  if found == 0:
      for i in range(0,len(lst)-1):
          if lst[i]<value<lst[i+1]:
              return i+1
      return len(lst)
