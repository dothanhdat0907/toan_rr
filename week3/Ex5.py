def binary_insertion_sort(list=[]):
    for i in range(1,len(list)): 
        x = list[i]
        l = 0
        r = i-1
        while l<=r:
            m = int((r+l)/2)
            if x>list[m]: l = m+1
            else: r = m-1
        for k in range(0,i-l):
            list[i-k] = list[i-k-1]
        list[l] = x
    return list
    
print(binary_insertion_sort([3,2,4,5,1,6]))