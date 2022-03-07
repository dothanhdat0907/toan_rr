def ternary_search(x, list=[]):
    l= 0
    r = len(list)-1
    while l<r:
        m1 = int(l + (r-l)/2)
        m2 = int(m1 + (r-l)/2)
        if list[m1] > x: r = m1
        elif list[m2] < x: l = m2 + 1
        else: 
            l = m1
            r = m2
    if x == list[r]: location = r
    else: location = 0
    return location

print(ternary_search(19,[1,2,3,4,5,6,7,8,10,12,13,15,16,18,19,20,22]))