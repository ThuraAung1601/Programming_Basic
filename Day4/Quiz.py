'''
Haine Min Thu
Modified - Thura Aung
'''
people = True
count = 0
while people:
        ans = input("Will you join us tonight? Y for Yes N for No: ")
        if ans == "Y":
            count += 1
        else: 
            continue
        res = input("Next One ? ")
        if res == "Y":
            people = True
        else:
            people = False
print(count," people are interested in coming our party !! ")

for i in range(count):
    a =  eval(input("How old are you? : "))
    ask_age(a)
    
def ask_age(a):
    if a >= 18:
        print("Welcome to the party!")
    elif a >= 16:
        b = input("Do your parents know? Y for yes N for No")
        if b == "Y":
            print("Welcome to the party!")
        else: 
            print("Go for discussion!")
    else:
        print("Sorry,no kid allowed!")


