import random

response = input("Click y to roll the dice")

while response == "y":
    no = random.randint(1,6)

    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")    
    elif no == 2:
        print("[-----]")
        print("[0    ]")
        print("[     ]")
        print("[    0]")
        print("[-----]")  
    elif no == 3:
        print("[-----]")
        print("[ 0   ]")
        print("[  0  ]")
        print("[   0 ]")
        print("[-----]") 
    elif no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")  
    elif no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")      
    elif no == 6:
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")   

    r1 = input("Enter y to continue, or n to stop the program")   

    if r1 == "n":
        print("Thank you for rolling the dice, come back later")
        exit()
