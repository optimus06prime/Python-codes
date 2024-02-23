def cylind(radius, height):
    volume = int((22/7)*radius*radius*height)
    print(str(volume) + "cm2")

r = int(input("What is your radius: "))
h = int(input("What is the height: "))
cylind(r, h)