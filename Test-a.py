print("UI NETWORKS")
print("Enter your desired duration")
print("Daytime duration")
daytime = int(input(": ")) 
if daytime < 20:
    Daytime=0
else:
    Daytime=(daytime-20)*30    

print("Evening duration")
evening = int(input(": "))
Evening = evening*20
print("Weekend duration")
weekend = int(input(": "))
Weekend=weekend*10

cost = (Daytime + Weekend + Evening)
print(cost, "Naira")