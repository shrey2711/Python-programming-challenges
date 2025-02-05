class Solution:
    def missingNumber(self, arr):
        # code here
        # I have used sets here, since I think it is easier to use, however it can be done using lists also
        sorted_arr = set(sorted(arr))
        arr_original = set()
        
        for i in range(1,len(sorted_arr)+2): # make contigous original array
            arr_original.add(i)
        sorted_arr.add(0) # to make the lengths equal to the original array
        
        return ((arr_original-sorted_arr).pop()) # just pop the difference
            
