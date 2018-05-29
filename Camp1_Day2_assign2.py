from random import randint
number= randint(1,10)

while True:
    num_input = input("Guess the number: ")
    if str(number) != num_input:
        print ("Wrong, try again!")
    else:
        print("Correct!")
        break
