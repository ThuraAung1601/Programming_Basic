age = eval(input("Enter your age:"))
print(age)
if age >= 18:
    print("Welcome to the party!!!")
elif age >= 16:
    print("Do ur parents know ???")
    response = input("Y for Yes/N for No:")
    if response == "Y":
        print("Welcome to the party !!!")
    else:
        print("Then go for discussion.")
else:
    print("Not for kids")