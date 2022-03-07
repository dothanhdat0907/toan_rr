def count_binary_insertion_sort(list=[]):
    count1 = 0
    for i in range(1,len(list)): 
        x = list[i]
        l = 0
        r = i-1
        while l<=r:
            count1+=1
            m = int((r+l)/2)
            if x>list[m]: 
                l = m+1
                count1+=1
            else: 
                r = m-1
                count1+=1   
        count1+=1
        for k in range(0,i-l):
            list[i-k] = list[i-k-1]
        list[l] = x
    return count1

def count_insertion_sort(list=[]):
    count2 = 0
    for i in range(1,len(list)):
        x = list[i]
        j = 0
        while (list[i]>list[j]):
            j+=1
            count2+=1
        count2+=1
        for k in range(0,i-j):
            list[i-k] = list[i-k-1]
        list[j] = x
    return count2

print(count_binary_insertion_sort([7, 4, 3, 8, 1, 5, 4, 2]))    
print(count_insertion_sort([7, 4, 3, 8, 1, 5, 4, 2]))    

