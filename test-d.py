num=int(input("Enter any positive integer"))

i = num + 1
numbers = list(range(i))
print("Number       Squares       cube       Square root")
for i in numbers:
    square = i**2
    cube = i**3
    square_root=i**(1/2)
    print(f"{i}           {square}             {cube}          {square_root:.3f}")