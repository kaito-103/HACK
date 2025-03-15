import time
import random
import os
def clear():
 os.system("clear")

question = input("Enter your victim: ")
questionfb = input("Please enter a valid Facebook link: ")
answer = input("Are you sure this is your victim? (y/n):")
if answer == 'y':
    print("Ok Wait for it")
    for i in range(1, 2):
        print(i)
        time.sleep(1)

    print("Victim Found")
    print("Victim Name:" + question) 
    print("Victim FB:" + questionfb)
    print("Wait for the F2F CODE.....")
    
    f2f_code = ''.join(random.choice('0123456789') for i in range(6))
    print("F2F CODE: " + f2f_code)

code = input("Enter Your F2F CODE:")
print("SUCCESSFULLY HACK CHECK YOUR ACCOUNT.TXT ON FILE")