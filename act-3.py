w=(1,2,1,2,1,2,1)
x=1
y=2
for day in range(0,7):
    if w[day]==1:
        y=y+1
    else:
        x=x+1


if x<y:
    print("Great weather")

else:
    print("Bad weather")