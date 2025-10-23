# warning:CHAOSDUAWE89 DONT KNOWS WHAT THWE HELL HES DOING HE JUST NEED TO DO SOMETHING INSTEAD OF CONTANTLY WATCHING YOUTUBE
while True:
    try: 
        def a(a, b):
            return a + b

        def b(a, b):
            return a - b
    
        def c(a, b):
            return a * b
    
        def d(a, b):
            return a / b

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
        else:
            print("invalid choice")
        
            
        
        
        print("by choasduawe89")
    except TypeError:
        print("no.")
    except ZeroDivisionError:
        print("no.")