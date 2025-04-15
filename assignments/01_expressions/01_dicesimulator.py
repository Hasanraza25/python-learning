# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random

def roll_dice():
    return random.randint(1,6)

def main():
    for i in range(1,4):
        die1 = roll_dice()
        die2 = roll_dice()
        total = die1 + die2
        print(f"Roll {i}: Die 1 = {die1}, Die 2 = {die2} -> Total = {total}")
        
    
if __name__ == '__main__':
   main()