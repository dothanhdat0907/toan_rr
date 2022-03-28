def ones(s:str):
    if len(s) == 0:
        return 0
    else:
        return ones(s[1:]) + int(s[0])

print(ones('110000'))
