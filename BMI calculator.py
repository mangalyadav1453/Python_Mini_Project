weight=float(input("enter weight in kg : "))
height=float(input("Enter height in meter : "))
BMI = weight/height**2
print("your body mass index is",BMI)
if BMI < 18.5:
    print("you are underweight")
elif BMI < 25:
    print("awesome! you are healthy.")
elif BMI <=29.9:
        print("you are over weight.")
else:
    print("over weight")
             
       
