import time
import random

correct=False
ran_num=random.randint(1,100)
i=1

while correct==False:
    n=int(input("Enter any number between 1 to 100: "))
    if n==ran_num:
        correct=True
    elif n>ran_num:
        print(f"Number is less than {n}. Try again...")
    elif n<ran_num:
        print(f"Number is greater than {n}. Try again...")
    i+=1

print(f"You have guessed the correct number in {i} attempts.")
time.sleep(5)  #shows the result for 5 seconds before exiting the program