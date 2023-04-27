def greatestnum(a, b,c):


    if(a>b):
      if(a>c):
        return a
      else:
        return c
    else:

        if(b>c):
            return b
        else:
            return c

m= greatestnum(2,8,15)

print("Thr greatest num is "+ str(m))

