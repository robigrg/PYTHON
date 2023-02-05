# Name: Robi Gurung
# Date: 19 November 2016
# Points: 30

# Problem 1. Sum of Digits in a String (10 points)
# WAP that asks the user to enter a series of single-digit numbers with nothing separating them. The problem should display the sum of all the single digit-numbers in the string.
# For example, if the user enter 2514, the method should return 12, which is the sum of 2,5,1,and 4.
def SDS(): #defining a function named SDS()
    print('Enter a series of single-digit numbers with nothing separating them:') #printing a statement to ask the user for an input of single-digit number with nothing separating them
    usersdigit = input() #taking the input and assigning it to variable usersdigit
    total = 0 #assigning 0 to variable total to count the sum of the numbers in particular
    while not usersdigit.isdigit(): #while loop that checks whether the number inputed is only digits or not
        print('Invalid Input. Please only type numbers.') #prints the statement about invalid input if the above condition is True
        print('Enter a series of single-digit numbers with nothing separating them:') #asks the user to input again another single-digit number with same requirement
        usersdigit = input() #taking the input and assigning it to variable usersdigit
    for x in usersdigit: #for loop that runs till the length of the string
        total = total + int(x) #adding the first number by converting it into interger to variable total
    print('The total number of the inputed number is:',total) #printing the total number of the inputed number
    print() #printing a blank line
SDS() #calling the defined function SDS()


# Problem 2. Date Printer (10 points)
# WAP that reads a string from the user containing a date in the form mm/dd/yyyy. It should print the date in the form November 2, 2016.

def date_printer(): #defining a function called date_printer()
    print("Write the date in the form of mm/dd/yyyy.") #printing a statement that tells the user how to type date for the further proccedure
    date = input("Input the date:") #taking the input and assigning it to variable date
    A = date.replace('/',' ') #replacing '/' with a blank space and assigning the dates into a variable A
    B = A.split() #splitting the data in the variable A and turning them into a list called B
    day = B[1] #assigning the second indexed data to variable day
    year = B[2] #assigning the third indexed data to variable year
    if B[0] == '01': #if condition that checks whether the first indexed data in the list B is equal to 01 or not
        month = 'January' #if the above statement is true then the month becomes January
    elif B[0] == '02': #if condition that checks whether the first indexed data in the list B is equal to 02 or not
        month = 'February' #if the above statement is true then the month becomes February
    elif B[0] == '03': #if condition that checks whether the first indexed data in the list B is equal to 03 or not
        month = 'March' #if the above statement is true then the month becomes March
    elif B[0] == '04': #if condition that checks whether the first indexed data in the list B is equal to 04 or not
        month = 'April' #if the above statement is true then the month becomes April
    elif B[0] == '05': #if condition that checks whether the first indexed data in the list B is equal to 05 or not
        month = 'May' #if the above statement is true then the month becomes May
    elif B[0] == '06': #if condition that checks whether the first indexed data in the list B is equal to 06 or not
        month = 'June' #if the above statement is true then the month becomes June
    elif B[0] == '07': #if condition that checks whether the first indexed data in the list B is equal to 07 or not
        month = 'July' #if the above statement is true then the month becomes July
    elif B[0] == '08': #if condition that checks whether the first indexed data in the list B is equal to 08 or not
        month = 'August' #if the above statement is true then the month becomes August
    elif B[0] == '09': #if condition that checks whether the first indexed data in the list B is equal to 09 or not
        month = 'September' #if the above statement is true then the month becomes September
    elif B[0] == '10': #if condition that checks whether the first indexed data in the list B is equal to 10 or not
        month = 'October' #if the above statement is true then the month becomes October
    elif B[0] == '11': #if condition that checks whether the first indexed data in the list B is equal to 11 or not
        month = 'November' #if the above statement is true then the month becomes November
    elif B[0] == '12': #if condition that checks whether the first indexed data in the list B is equal to 12 or not
        month = 'December' #if the above statement is true then the month becomes December
    print ('The Date is :',month,day,',',year) #printing the date in a different format
    print () #printing a blank line
date_printer() #calling the defined function date_printer()
    
# Problem 3. Pig Latin (10 points)
# WAP that accepts a sentence as input and converts each word to "Pig Latin". In one version, to convert a word to Pig Latin you remove the first letter and place that letter at the end of the word.
# Then you append the string "ay" to the word. Here is an example:
# English: I SLEPT MOST OF THE NIGHT
# Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY

def pig_latin(): #defining a function named pig_latin()
    print('Converting a sentence into Pig Latin') #printing a statement that tells the user that this function converts the sentence into Pig Latin
    sentence = input('Enter a sentence:') #asking the user to type a sentence, taking the input and assigning it to variable sentence
    sentence = sentence.upper() #converting the inputed sentence into Uppercase
    List = sentence.split() #splitting the words of the inputed sentence into a list in list variable called List
    for x in List: #for loop that runs till the length of the List
        if len(x) == 1: #if condition that checks if the word in the sentence has only one letter or not
            print(x + 'AY', end=' ') #if the above condition is True then it prints the letter with additional AY code word and a space at the end
        else: #if the above condition is False then this is what it prints
            print(x[1:]+x[0]+'AY',end=' ') #printing the second letter of the word and adding the first letter at the back of the word. Then it adds AY at last and a space at the end
    print() #printing a blank line
pig_latin() #calling the defined function


