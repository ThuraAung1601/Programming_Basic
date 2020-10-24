"Bug Fixed"
people = True
count = 0
party_people = []
party_contact = []
ages = []

while people:
        ans = input("Will you join us tonight? Y for Yes N for No: ")
        if ans == "Y" or ans == "y":
            count += 1
        else: 
            pass
        res = input("Next One ? ")
        if res == "Y" or res == "y":
            people = True
        else:
            people = False
print(count," people are interested in coming our party !! ")

def ask_age(a):
    if a >= 18:
        ages.append(a)
        name = input("Your name please: ")
        party_people.append(name)
        ph = input("Your Ph no please: ")
        party_contact.append(ph)
        return True
    elif a >= 16:
        check = input("Do your parents know? Y for yes N for No")
        if check == "Y" or check == "y":
            ages.append(a)
            name = input("Your name please: ")
            party_people.append(name)
            ph = input("Your Ph no please: ")
            party_contact.append(ph)
            return True
        else: 
            return False
    else:
        return False

for i in range(count):
    print("Hello")
    a = eval(input("How old are you ?:"))
    if ask_age(a) == True:
        print("Welcome to the party {}".format(party_people[i]))
    else:
        print("Sorry not allowed")
    
party_info1 = zip(party_contact,ages)
party_full_info = dict(zip(party_people,party_info1))
print(party_full_info)

