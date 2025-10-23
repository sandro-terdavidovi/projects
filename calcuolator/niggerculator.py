# warning:CHAOSDUAWE89 DONT KNOWS WHAT THWE HELL HES DOING HE JUST NEED TO DO SOMETHING INSTEAD OF CONTANTLY WATCHING YOUTUBE
try: 

    
    a = lambda a, b: a + b
    
    b = lambda a, b: a - b
    
    c = lambda a, b: a * b
    
    d = lambda a, b: a / b

    hi = int(input("type your number"))
    hi2 = int(input("type your number"))

    choice = input("type..")
    if choice == "+":
        retur = a(hi, hi2)
        print(f"result is: {retur}")
    elif choice == "-":
        retur1 = b(hi, hi2)
        print(f"result is: {retur1}")
    elif choice == "*":
        retur2 = c(hi, hi2)
        print(f"result is: {retur2}")
    elif choice == "/":
        retur3 = d(hi, hi2)
        print(f"result is: {retur3}")
    
        
    
    
    print("by choasduawe89")
except TypeError:
    print("no.")
except ZeroDivisionError:
    print("no.")