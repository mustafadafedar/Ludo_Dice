import random

def PLAYER_1():
    print("1st Player Turn")
    user = input("Press Enter To Roll!")
    num = [1,2,3,4,5,6]
    ran = random.choice(num)
    print(ran)

def PLAYER_2():
    print("2nd Player Turn")

    user = input("Press Enter To Roll!")
    num = [1, 2, 3, 4, 5, 6]
    ran = random.choice(num)
    print(ran)

def PLAYER_3():
    print("3rd Player Turn")

    user = input("Press Enter To Roll!")
    num = [1, 2, 3, 4, 5, 6]
    ran = random.choice(num)
    print(ran)

def PLAYER_4():
    print("4th Player Turn")

    user = input("Press Enter To Roll!")
    num = [1, 2, 3, 4, 5, 6]
    ran = random.choice(num)
    print(ran)

def main():
    PLAYER_1()
    PLAYER_2()
    PLAYER_3()
    PLAYER_4()
print(main())