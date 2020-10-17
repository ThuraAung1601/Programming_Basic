people = True
count = 0
while people:
    ans = input("Will u join us tonight: ")
    if ans == "Y":
        print("Welcome")
        count = count + 1 #count++ 
        nex = input("Next ? ")
        if nex == 'Y':
            people = True
        else:
            people = False
    else:
        nex = input("Next ? ")
        if nex == 'Y':
            people = True
        else:
            people = False
print(count,"people will come tonight")
