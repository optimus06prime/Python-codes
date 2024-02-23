print("UI NETWORKS")
print("Enter your desired duration")
print("Daytime duration")
while True:
    daytime = int(input(": "))

    if daytime < 20:
        print("Your daytime duration cannot be less than 20minutes, please select somethimg higher than 20minutes")
    else:
            
        print("Evening duration")   
        evening = int(input(": "))
        print("Weekend duration")
        weekend = int(input(": "))
        break
    
cost = ((daytime-20)*30) + (evening*20) + (weekend * 10)
print(cost, "Naira")