def recursive(n):
    if n<=0:
        return n
    else:

       return recursive(n-1) + n

r=recursive(16)

print (r)