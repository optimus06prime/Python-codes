#create a factorial function
def factorial_recursion(n):
    if n == 1:
        answer =1
        return answer
    elif n==0:
    	answer=1
    	return answer
    else:
        answer= n * factorial_recursion(n-1)
        return answer
        print(answer)
#prompt the user for a value
print("enter The number to be factorialed")
number=int(input(" "))
#call function
factorial_recursion(number)


