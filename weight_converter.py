#Converts lbs to kg or vice versa
weight = input("Weight: ")

weight = int(weight)

unit = input("(K)g or (L)lbs: ")

if (unit) == "l":
    print("Weight in Kg: " + str(weight / 2.205))
else:
    print("Weight in Lbs: " + str(weight * 2.205))