def p(t):
    e=len(t)-1
    s=0
    while (s<e):
        if t[s]!=t[e]:
            return False
        s=s+1
        e=e-1
    return True
t=(1,2,3,3,2,1)
if p(t):
    print("Palendrome")
else:
    print("Not Palendrome")