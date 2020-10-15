var_1 = int(input("Enter an integer: "))
var_2 = int(input("Enter an integer: "))
if var_1 != var_2:
    print(var_1,"is not equal with ",var_2)
    if var_1 < var_2:
        print(var_1,"is less than ",var_2)
    else:
        print(var_1,"is greater than ",var_2)
else:
    print(var_1,"is equal with ",var_2)