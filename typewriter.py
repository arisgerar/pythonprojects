import time
import random

text = input("What do you want to type? ")

for letter in text:
    chance = random.randint(1, 10)

    if chance == 3:
        print(letter + letter, end="", flush=True)  

    elif chance == 2:
        print("*", end="", flush=True)  

    if chance == 1:
        print("JAM!")  

    else:
        print(letter, end="", flush=True)

    time.sleep(0.1)