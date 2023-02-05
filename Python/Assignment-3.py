# Name: Robi Gurung
# Date: 23 September 2016
# CRN: 21952
# Homework-3

# A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation, she asks membes for the number of fat grams and carbohydrate grams that they consumed in
# a day. Then, she calculates the number of calories that result from the fat, using the following formula:
#                                                                                                              Calories from fat= fat grams*9
# Next, she calculates the number of calories that result from the carbohydrates, using the formula:
#                                                                                                              Calories from carbs= carb grams*4
# The nutritionist asks you to write a function that will make these calculations and return the total calories.

def calories(): #creating a user-defined function named as calories()
    print('Enter the number of fat grams consumed in a day:') #asking the user for the number of fat grams that he/she consumes in a day
    fat_grams=input() #taking input of the number of fat grams from the user
    fat_grams=float(fat_grams) #conversion into float data type
    
    print('Enter the number of carbohydrate grams consumed in a day:') #asking the user for the number of carbohydrates grams that he/she consumes in a day
    carb_grams=input() #taking input of the number of carbohydrates gram from the user
    carb_grams=float(carb_grams) #conversion into float data type
    
    print('-----EVALUATING YOUR DIETS-----') #displaying a statement

    calories_from_fat= fat_grams*9 #calculation of total calories from the fats
    calories_from_carbs= carb_grams*4 #calculation of totalcalories from the carbohydrates
    total_calories= calories_from_fat + calories_from_carbs #calculation of the total calories by adding the total calories from fat and carbohydrates

    print('The number of calories that result from the fats is:', calories_from_fat) #diplaying the number of calories from the fat to the user
    print('The number of calories that result from the carbohydrates is:', calories_from_carbs) #displaying the number of calories from the carbohydrtes to the user
    print('Therefore, the total calories from fats and carbohydrates consumed in a day is:', total_calories) #displaying the total calories from fats and carbs consumed in a day
calories() #calling the defined function

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a function that lets the user play the game of Rock, paper, Scissors against the computer. The program should work as follows:
# 1. When the program begins, a random number in the range of 1 through 3 is generated.
#    If the number is 1, then the computer has chosen rock. If, the number is 2, then the computer has chosen paper. If the number is 3, then the computer has chosen scissors.
#    (Don't display the computer's choice yet).
# 2. The user enters his or her choice of "rock", "paper", or "scissors" at the keyboard.
# 3. The computer's choice is displayed.
# 4. A winner is selected according to the following rules:
#    + If one player chooses rock and the other player chooses scissors, then rock wins. (The rock smashes scissors)
#    + If one player chooses scissors and the other player chooses paper, then scissors wins. (Scissors cuts paper)
#    + If one player chooses paper and the other player chooses rock, then paper wins. (Paper wraps rock)
#    + If both players make the same choice, the game is tie.

def rock_paper_scissor(): #creating a user defined function named as rock_paper_scissor()
    import random #importing random
    for x in range(3): #use of for loop and the range function 
        computer= random.randint(1,3) #assigning a random number between 1 and 3 into computer
        if computer==1: #condition if the variable computer has 1
            hand1="Rock" #if the condition is true then Rock is assigned to hand1 variable
        elif computer==2: #condition if the computer has 2
            hand1="Paper" #if the condition is true then Paper is assigned to hand1 variable
        else: #default line that displays if the above conditions are not true
            hand1="Scissor" #if neither of the above condition are true then hand1 is assigned as Scissor 
            
        print("Let's play Rock, Paper or Scissor") #displaying a statement
        print('Enter one of the above:') #asking for the user to input to begin the game
        player=input() #taking the inputed value in player
        print('Player=',player) #displaying what was inputed by the user
        print('Computer=',hand1) #displaying what the computer came up with
        
        if player=="Rock": #first condition check
            if hand1=="Scissor": #inner condition check
                print("Rock smashes Scissor") #displaying if the condition is true
                print("You won") #displaying if the condition is true
            elif hand1=="Paper": #inner condition check if the above was false
                print("Paper wraps Rock") #displaying if the condition is true
                print("You lost") #displaying if the condition is true
        elif player=="Scissor": #second condition if the first is false
            if hand1=="Paper": #inner condition check
                print("Scissors cuts Paper") #displaying if the condition is true
                print("You won") #displaying if the condition is true
            elif hand1=="Rock": #inner condition check if the above was false
                print("Rock smashes Scissor") #displaying if the condition is true
                print("You lost") #displaying if the condition is true
        elif player=="Paper": #third condition if the first and the seconf is false
            if hand1=="Rock": #inner condition check
                print("Paper wraps Rock") #displaying if the condition is true
                print("You won") #displaying if the condition is true
            elif hand1=="Scissor": #inner condition check if the above was false
                print("Scissors cuts Paper") #displaying if the condition is true
                print("You lost") #displaying if the condition is true
        elif player==hand1: #fourth condition if all the above is false
            print("It's a tie.") #displaying if the condition is true
        else: #if the above condition doesn't meet at all 
            print("Please choose only from 'Rock','Paper' or'Scissor' and check the spellings") #a default statement to be displayed if the above conditions are not true

        print("Thanks for playing with me") #displaying a statement
            
rock_paper_scissor() #calling the defined function
































