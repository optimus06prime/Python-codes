#Ilugbaro Olaoluwa 236335
#program to print grade ans unit of a course
user_score=int(input("Enter your score in the course "))
if user_score<= 40:
	print("FAIL")
	print("0 units")
elif 41<= user_score <= 45:
	print("PASS") 
	print("1 unit")
elif 46<= user_score <= 59:
	print("AVERAGE")
	print("2 units")
elif 60<= user_score <=79:
	print("GOOD")
	print("3 units")
elif user_score>79:
	print("EXCELLENT")
	print("4 units")