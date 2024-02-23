print("BMI calculator")
weight = int(input("Enter your weigth(in kg): "))
height = int(input("Enter your height(in ft): "))
BMI = weight/(height**2)
print("Your BMI is " , BMI)
if BMI < 18.5:
    print("You are underweight")
    print("Try dey chop!!")
if  18.5 <= BMI <= 24.9:
    print("You have a normal BMI")
    print("Maintain your regular healthy diet and exercise routine")
if 25 <= BMI <= 29.9:
    print("You are overweight")
    print("Reduce food intake, take more of healthy food and excercise more")
if BMI >= 30:
    print("You are obese")
    print("Reduce intake of high calorie food, take more healthy meals and workout more")       
    