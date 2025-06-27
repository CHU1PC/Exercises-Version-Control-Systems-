import numpy as np


def roll_dice(name):
    print("Rolling dice...")
    a, b = np.random.randint(1, 7, 2)
    print("Die 1:", a)
    print("Die 2:", b)
    print("Total value:", a + b)
    if a + b >= 7:
        print(f"{name} won!")
    else:
        print(f"{name} lost.")


def greeting():
    name = input("What is your name?\n")
    print(f"Hello, {name}!")
    return name

if __name__ == "__main__":
    name = greeting()
    roll_dice(name)
