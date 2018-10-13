name = input ("Please, What is your name? ")
print ("Hi " + name + "! Welcome to my game!")
print ("I will pick a number between 1 and 100" + '\n' + "and you have 5 attempts to guess the number")
print ("Will you be able to guess?" + '\n' + "Good Luck!")
import random
sec_num = (random.randint(1,101))
user_num=()
count = 1

while user_num != sec_num and count <=(5):
    user_num=input("Pick your number: ")
    def check(user_num):
        try:
            int(user_num)
            return True
        except ValueError:
            return False
    if check(user_num) == False:
        user_num=input("Please insert a number: ")
        count += 1
    else:
        count += 1
    user_num = int(user_num)
    if int(user_num) < sec_num:
        if sec_num - user_num <= 5:
            print ("You are very close! GO GO GO!")
            print ("Secret number is higher!"+'\n')
        elif sec_num - user_num >= 40:
            print ("You are very far mate!")
            print ("Secret number is higher!"+'\n')
        else:
            print ("Secret number is higher!"+'\n')
            
    elif user_num > sec_num:
         if user_num - sec_num <= 5:
            print ("You are very close! GO GO GO!")
            print ("Secret number is lower!"+'\n')
         elif user_num - sec_num >= 40:
            print ("You are very far mate!")
            print ("Secret number is lower!"+'\n')
         else:
            print ("Secret number is lower!"+'\n')
      
if user_num == sec_num:
    print ("Congratulations!!! YOU WON!!!")
else:
    print ("Sorry! Out of Guess! YOU LOSE!")
    print ("Secret number is: " + str(sec_num))

print=input("")
