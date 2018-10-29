#Introduction: Prompt user name and explanation of the game
name = input ("Please, What is your name? ")
print ("Hi " + name + "! Welcome to my game!")
print ("I will pick a number between 1 and 100" + '\n' + "and you have 5 attempts to guess the number")
print ("Will you be able to guess?" + '\n' + "Good Luck!")

#with import i can recall the module random
import random
#In this way is possible to generate a random number givin a range
#IMPORTANT!!! The range will stop before the second number inside the parenthesis)
sec_num = (random.randint(1,101))
user_num=()
count = 1

#This loop will continue until the user did 5 attemp or guess the number
while user_num != sec_num and count <=(5):
    
    user_num=input("Pick your number: ")
    #This function add an exception in case the user do not insert a number
    #if it is a number give me a True value, otherwhise instead of giving error message return an True value
    def check(user_num):
        try:
            int(user_num)
            return True
        except ValueError:
            return False
    #If the value of the function check is false we ask again to insert a number    
    while check(user_num) == False: #i change from a IF statement to a WHILE statement to repeat until a number is put.
        user_num=input("Please insert a number: ")
        #i had to add this increment because i noticed that if the user did not put the number the first time requested
        #but only the second time, actually could have infinite attempts
       
    count += 1 #increase the attempt counter
    #i had to transform the string to a number to able to do math operation    
    user_num = int(user_num)
    #here i check if the user number is lower that the secret number
    if user_num < sec_num:
       
        #here i check if the difference between the secret number and the user number is lower or equal than 5 and give a hint
        if sec_num - user_num <= 5:
            print ("You are very close! GO GO GO!")
            print ("Secret number is higher!"+'\n')
        
        #here i check if the difference between the secret number and the user number is higher or equal than 40 and give a hint
        elif sec_num - user_num >= 40:
            print ("You are very far mate!")
            print ("Secret number is higher!"+'\n')
        else:
            print ("Secret number is higher!"+'\n')
   
   #here i am doing the same did above but in case the user number is higher than the secret number.        
    elif user_num > sec_num:
         
         if user_num - sec_num <= 5:
            print ("You are very close! GO GO GO!")
            print ("Secret number is lower!"+'\n')
         
         elif user_num - sec_num >= 40:
            print ("You are very far mate!")
            print ("Secret number is lower!"+'\n')
         
         else:
            print ("Secret number is lower!"+'\n')
            
#after the loop finish i check if the user won or not      
if user_num == sec_num:
    print ("Congratulations!!! YOU WON!!!")
else:
    print ("Sorry! Out of Guess! YOU LOSE!")
    print ("Secret number is: " + str(sec_num))
#this is to stop the screen and wait until the user press any key
print=input("")
