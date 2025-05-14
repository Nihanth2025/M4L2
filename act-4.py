def avg(n):
    l1=list(n)
    s=0
    for x in l1:
        s=s+x
    return s

n=(50,20,30,60)
print("Tuple",n)
print("Average:",avg(n)/len(n))