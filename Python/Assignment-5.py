# Name: Robi Gurung
# Date: 28 October 2016
# Points: 20

#Problem 1. Lottery Number Generator
#Design a program that generates a seven-digit lottery number. The program should generate seven random numbers, each in the range of 0 through 9, and assign each number to a list element. Then write
#another loop that displays the lottery numbe
def lottery(): #defining a function named lottery
    import random #importing random
    Lottery_number = [] #assigning a variable Lottery_number to an empty set
    for W in range(7): #starting a loop that runs 7 times
        a = random.randint(0,9) #assigning a random number from 0 to 9 to a
        Lottery_number.append(a) #adding the random number 'a' to the list Lottery_number      
    print('The lottery number is:') #printing a statement
    print (Lottery_number) #printing the list Lottery_number
    print() #printing a blank line
lottery() #calling the defined function

#Problem 2. Number Analysis Program
#Design a program that asks the user to enter a series of 20 numbers. The program should store the numbers in a list and then display the following data:
#   +The lowest number in the list
#   +The highest number in the list
#   +The total of the numbers in the list
#   +The average of the numbers in the list
#   +Print the number in the list in ascending order(10 points)
def Number_Analysis(): #defining a function called Number_Analysis
    print('\t*Enter a series of 20 numbers*') #printing a statement
    Empty=[] #assigning a variable Empty to an empty set
    Sum=0 #assigning 0 to a variable 'Sum'
    for E in range(20): #starting a loop that runs 20 times
        print("Enter a number:") #printing a statement 
        Number = input() #taking the input and assigning it into 'Number'
        Number = int(Number) #converting the type of the data inputed into number
        Sum = Sum + Number #adding the value inputed into the variable 'Number' to Sum
        Empty.append(Number) #adding the inputed number 'Number' to the list Empty
    Data_Of_Numbers = Empty #assigning the collective data of list 'Empty' to 'Data_Of_Numbers'
    Data_Of_Numbers.sort() #sorting the data inside the list of 'Data_Of_Numbers' into an ascending order
    Average_Of_Numbers = Sum/20 #finding the Average of the stored data numbers in the list by dividing the Sum by the total number of data inputed
    A = max (Data_Of_Numbers) #assigning variable 'A' to calculate the maximum number in the list 'Data_Of_Numbers'
    B = min (Data_Of_Numbers) #assigning variable 'A' to calculate the minimum number in the list 'Data_Of_Numbers'
    print ('The maximum number in the list is:', A) #printing the maximum number in the list
    print ('The minimum number in the list is:', B) #printing the minimum number in the list
    print ('The total of the numbers in the list is :', Sum) #printing the total of the numbers in the list
    print ('The average of the numbers in the list is:', Average_Of_Numbers) #printing the average of the numbers in the list
    print ('The number in the list in ascending order:', Data_Of_Numbers) #printing the numbers in the list in ascending order
    print () #printing a blank line
Number_Analysis() #calling the defined function

#Problem 3. Driver's License Exam
#The local driver's license office has asked you to create an application that grades the written portion of the driver's license exam. The exam has 10 multiple-choice questions. Here are the correct answers:
#   1.B     6.A
#   2.D     7.B
#   3.A     8.A
#   4.A     9.C
#   5.C     10.D
#Your program should store these correct answers in a list. The program should take the student's answer for the 10 questions from input and store the answers in another list. It should then display
#the total number of correctly answered questions, the total number of incorrectly answered questions, and a list showing the question of the incorrectly answered questions. (10pts)
def Drivers_License_Exam(): #defining a function named Drivers_License_Exam
    CorrectAnswerList=['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D'] #a list of correct answers data stored in a variable list 'CorrectAnswerList'
    StudentAnswerList=[] #assigning an empty set to 'StudentAnswerList'
    print('\t*Enter the Answers*') #printing a statement
    A=1 #assigning 1 to A
    for E in range(10): #starting a loop that runs 10 times
        print("Enter the answer of",A,"question") #asking the user to input the answers
        StudentAnswer=input()#taking the input from the user and assigning it to variable 'StudentAnswer'
        StudentAnswer=StudentAnswer.upper() #converting the inputed data into uppercase
        StudentAnswerList.append(StudentAnswer) #adding the inputed data into the list 'StudentAnswerList'
        A=A+1 #increment of the variable 'A' by 1
    n=0 #assignning 0 to variable 'n'
    Right=0 #assigning 0 value to variable 'Right'
    Wrong=0 #assigning 0 value to variable 'Wrong'
    for D in range(10): #a for loop that runs 10 times
        if StudentAnswerList[n]==CorrectAnswerList[n]: #checking a condition if the inputed data is exactly the same with the correct data from 'StudentAnswerList' and 'CorrectAnswerList' respectively
            Right=Right+1 #Adding 1 to the variable 'Right'
        else: #condition if the above condition doesn't result 'True'
            Wrong=Wrong+1 #Adding 1 to the variable 'Wrong'
        n=n+1 #increment of variable 'n' by 1
    print('The total number of correctly answered questions is:',Right) #printing the total number of correctly answered questions
    print('The total number of incorrectly answered questions is:', Wrong) #printing the total number of incorrectly answered questions
    print('The list of correct 10 questions is:', CorrectAnswerList) #printing the correct answer list
Drivers_License_Exam() #calling the defined function


















