def pascal_triangle(line_number):
    
    pascal_triangle = []
    
    for i in range(0,line_number):
        if i==0:
            pascal_triangle.append(1)
        if i==1:
            pascal_triangle.append([1,1])
        elif i>1:
            temp_list = [0]*(i+1) # creating a list of desired size for that particular loop
            temp_list[0] = 1 # starting element is always fixed to be 1
            temp_list[len(temp_list)-1] = 1 # last element is always fixed to be 1
            for j in range(1,len(temp_list)-1):
                temp_list[j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j] # adding elements from the previosu pascal triangle iteratively
            pascal_triangle.append(temp_list)
    return pascal_triangle
          
# Driver to test above code
if __name__ == '__main__':

    # Function call
    line_number = 10
    result = pascal_triangle(line_number)

    if result != -1:
        print("Pascal triangle is: ", result)
    else:
        print("Element is not present in the list")
