seque=[10,20,35,15,62,60]

for i in seque:
    
    if i>seque[seque[i]+1]:
        print(i)
    else:
        i=seque[seque[i]+1]    