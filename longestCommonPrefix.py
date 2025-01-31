def longestCommonPrefix(strs):
        #calculating the length of the strings
        length = []
        count = 0
        comm_prefix = 0
        for i in strs:
            length.append(len(i))
        # iterate till minimum lengths of string
        minimum_length = min(length)
        #go for till minimum length
        for i in range(minimum_length):
            ref_char = strs[0][i]
            for j in range(1,len(strs)):
                if ref_char == strs[j][i]:
                    count+=1
            if count==(len(strs)-1):
                comm_prefix+=1
                count=0
            else: # as soon as there is a mismatch which means we have founf longest prefix
                break
        if comm_prefix: # returning the common prefix from the first string
            return strs[0][:comm_prefix]
        else:
            return ""
