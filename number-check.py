#inputing number
print("Enter the nunber to be checked")
num=int(input(" "))
#checking if number is even or odd
if num == 0:
	print("The number is neutral")
elif num%2 == 0:
	print("This is an even number")
elif num%2 != 0:
	print("This number is odd")