def m(s:str):
    if len(s) == 1:
        return int(s[0])
    else:
        return max(int(s[0]),m(s[1:]))

