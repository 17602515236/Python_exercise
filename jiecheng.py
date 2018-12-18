def muilt(m):
    if m == 1:
        return 1
    else:
       m *= muilt(m - 1)
    return m

print(muilt(4))



