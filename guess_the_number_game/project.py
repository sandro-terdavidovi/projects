import random

def niggaballs():
    try:
        randomnum1 = list(range(1, 50))
        randomnum2 = random.choice(randomnum1)

        attempts = 0
        maxattempts = 5

        user = int(input("Type your number or i will rape all your shit out"))

        while user != randomnum2:
            print("uncorrect try again")
            user = int(input("Type your number or i will rape all your shit out"))
            attempts = attempts + 1
        print("you did it!")
        niggaballs()

    except ValueError:
        print("try again its number game nigga")
        input("press enter to countinue NIGGAH")
        niggaballs()


niggaballs()



            

    
