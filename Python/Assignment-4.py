# Name: Robi Gurung
# Date: 3 October 2016
# CRN: 21952
# Homework-4

#Problem 1. Calories Burned:
#Running on a particular treadmill you burn 3.9 calories per minute. Write a program that uses a loop to display the number of calories burned after 10,15,20,25 and 30 minutes.

def calories_burned(): #defining a function named calories_burned
    Time=10 #setting a constant to a variable named Time
    
    while Time <= 30: #checking a condition if the variable Time is less or equal to 30
        CaloriesBurned= Time * 3.9 #conducting a mathematic operation to calculate the number of calories burned on different time intervals
        print('The number of caloried burned after',Time,'minutes is:',CaloriesBurned) #printing the number of calories burned after Time intervals
        Time= Time + 5 #increment of Time with 5
        
calories_burned() #calling the defined function
print() #for a free line
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Problem 2. Prime Numbers:
#A prime number is a number that is only evenly divisible by itself and 1. For example, the number 5 is prime because it can only be evenly divided by 1 and 5. The number 6, however, is not a prime
#because it can be divided evenly by 1,2,3 and 6. Write a function named is_prime which takes an integer as an arguement and returns TRUE if the arguement is a prime, or FALSE otherwise. Use the
#function in a program that prompts the user to enter a number and then displays a message indicating whether the number is prime.
#TIP: Recall that the % operator divides one number by another and returns the remainder of the division. In the expression num1 % num2, the % operator will return 0 if num1 is evenly divisible by num2.

def is_prime(): #defining a function named is_prime
    print('Enter a number:') #asking the user to input a number
    Number=input() #assigning the inputed number in a variable named Number
    Number=int(Number) #changing the datatype into Integer
    White=1 #assigning a constant with 1 as its data
    Iverson=0 #assigning a constant with 0 as its data
    
    while White <=  Number: #checking whether the given Number is greater or equal to the number assigned in the variable White
        Testing= Number % White #dividing Number value by the White value and assigning them into Testing variable
        if Testing == 0: #checking if the resulted Testing value is equals to 0 or not
            Iverson= Iverson + 1 #if the above condition came true then Iverson variable is termed to be increased by 1
        White= White + 1 #increment of the value assigned in White by 1
        
    if Iverson > 2: #checking if the value in Iverson variable is greater than 2 or not
        print("FALSE, it's not a prime number.") #if the above condition results true then this prints that the number inputed was not a prime number
    else: #if the condition is false then 
        print("TRUE. it's a prime number.") #this prints if the condition is false and shows that the inputed number is a prime number
is_prime() #calling the defined function
print() #for a free line
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Problem 3. Sum of Numbers:
#Write a program with a loop that asks the user to enter a series of positive numbers. The user should enter a negative number to signal the end of the series. After all the positive numbers have been
#entered, the program should display their sum.

def Ferrari_Number_Series(): #defining a function named Ferrari_Number_Series
    Space=0 #assigning 0 value into a variable termed as Space
    Engine=True #assignning True into the variable Engine
    
    while Engine : #checking while the Engine is still True to start the loop
        print("Enter a number:") #asking the user to input a number
        Driver=input() #assigning the inputed number into a variable termed as Driver
        Driver=int(Driver) #conversion of datatype into Integer because the inputed value by the user is a number

        if Driver >=0 : #checking if the condition about the inputed number is greater than 0 or equal to 0 or not
            Space= Driver + Space #Adding the value inputed into a variable termed as Space whose value is 0 at the first
        else: #if the condition results false then
            Engine=False #if the above condition results false then Engine is assigned to False to stop the loop
    print('The total sum of the inputed numbers is:',Space) #printing the total sum of the positive numbers inputed by the user
Ferrari_Number_Series() #calling the defined function
print() #for a free line
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Problem 4. Draw the pattern:
#Write a program that uses nested loop to draw the pattern below:
#
#   *******
#   ******
#   *****
#   ****
#   ***
#   **
#   *

def Star_Pattern(): #deifning a function named Star_Pattern
    for a in range(7): #constructing a loop with a rows of 7
        for b in range(7-a): #a nested loop that is of columns which is decreasing by the first value and so on till 7
            print('*', end='') #prints '*' in correspondence to the loop and ending with a free space after a work is done
        print() #for a free line   
            
Star_Pattern() #calling the defined function

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------








    
    

        
        
        
