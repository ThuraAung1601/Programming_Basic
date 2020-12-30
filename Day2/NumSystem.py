check = True
while check:
    bases = input("From what to what: ")
    bases = bases.split()
    ip = input("Enter num to be converted: ")

    if bases[1] == '10':
        if bases[0] == "2":
            result = int(ip,2)
        elif bases[0] == "8":
            result = int(ip,8)
        elif bases[0] == "16":
            result = int(ip,16)
        else:
            pass

    elif bases[1] == '2':
        if bases[0] == "8":
            result = int(ip,8)
            result = bin(result)
        elif bases[0] == "10":
            result = bin(result)
        elif bases[0] == "16":
            result = int(ip,16)
            result = bin(result)
        else:
            pass
    
    elif bases[1] == '8':
        if bases[0] == "2":
            result = int(ip,2)
            result = oct(result)
        elif bases[0] == "10":
            result = oct(result)
        elif bases[0] == "16":
            result = int(ip,16)
            result = oct(result)
        else:
            pass


    elif bases[1] == '16':
        if bases[0] == "2":
            result = int(ip,2)
            result = hex(result)
        elif bases[0] == "10":
            result = hex(result)
        elif bases[0] == "8":
            result = int(ip,8)
            result = hex(result)
        else:
            pass
    else:
        pass
    
    print(result)
    stop = input("Type 1 to quit, 0 to continue : ")
    if stop == '1':
        check = False
    else:
        continue

