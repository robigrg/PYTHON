# Name: Robi Gurung
# Date: 12 November 2016
# Total Points: 40
# CSCI 1340: Assignment 6: File

# Problem 1. Random Number File Writer
# WAP that writes a series of random numbers to a file namemd to a file named randNum.txt one number per line. Each random number should be in the range of 1 to 100.
# The application should let the user specify how many random numbers the file will hold.

def RandomNum_FileWriter(): #defining a function named RandomNum_FileWriter
    import random #importing random
    New_File = open ('randNum.txt','w') #opening a file 'randNum.txt' for writing purpose and assigning it to New_File
    UserSpecification = input('How many random numbers should the file hold?\n') #asking the user to input which is assigned to UserSpecification
    UserSpecification = int(UserSpecification) #converting the data into Integer
    for x in range(UserSpecification): #using for loop that runs UserSpecification times
        TheNumber = random.randint(1,100) #assigning a random number to variable TheNumber
        TheNumber = str(TheNumber) #converting the data into string
        New_File.write(TheNumber + '\n') #writing the number assigned as a string in TheNumber into the opened file       
    New_File.close() #closing the file
RandomNum_FileWriter() #calling the defined function

# Problem 2. Random Number File Reader
# This exercise asks you to read the random numbers from the file randNum.txt, display the numbers and then display the following data:
# i.The total of the numbers
# ii.The number of random numbers read from the file

def RandomNum_FileReader(): #defining a function named RandomNum_FileReader
    New_File = open('randNum.txt','r') #opening a file 'randNum.txt' for reading purpose and assigning it to New_File
    Sum = 0 #assigning 0 in the variable named Sum
    Count = 0 #assigning 0 in the variable named Count
    for A in New_File.readlines(): #starting a for loop that runs each line until it ends up with a blank line
        Sum = Sum + int(A) #adding the first number by converting it from string into integer
        Count = Count + 1 #the variable Count is being increment by 1 everytime the loop runs
    print('The total of the numbers:',str(Sum)) #statement that prints the total number stored in the file
    print('The number of random numbers read from the file:',str(Count)) #statement that prints the number of random numbers read from the file
    print() #printing a blank line
    New_File.close() #closing the file
RandomNum_FileReader() #calling the defined function

# Problem 3. Customer data management
# The manager of a store has asked you to write software that manages customer data with the following capabilities:
# i.A function that will read each customer's name and id as keyboard input, and then save these as records in a file named customer.txt. (Each record line will have a field for the customer's name and 
#   a field for his/her id.)
# ii.Another function that reads the records from the customer.txt file and displays them.
# iii.The software has a menu that allows a user to select one of the two functions in each run.

def main(): #defining a function named main
    play = True #assigning True to play
    while play: #starting a while loop only if the play is True
        select = menu() #getting value from the menu function and assigning it to select variable
        if select == 'I': #condition that checks if the value in select variable is equal to 'I' or not
            Part_1() #if the above condition results True then Part_1() function runs
        elif select == 'R':  #condition that checks if the value in select variable is equal to 'R' or not
            Part_2() #if the above condition results True then Part_2() function runs
        elif select == 'X': #condition that checks if the value in select variable is equal to 'X' or not
            play = False #if the above condition results True then play is assigned to be False
        
def menu(): #defining a function named menu
    print('\tPlease choose from the following:') #printing a statement
    print('-Type "I" to enter the name and ID number of the customer.') #printing a statement
    print('-Type "R" to read and see the records from the customer.txt file.') #printing a statement
    print('-Type "X" to exit.') #printing a statement
    User = input() #getting the value typed by the user and assigning it to variable named User
    User = User[0].upper() #converting the first letter inputed into Uppercase
    while User != 'I' and User != 'R' and User != 'X': #condition that checks if the value inputed in User is not equal to "I","R" or "X"
        print('**Invalid Input.**Please only choose from the following:\n') #printing a statement
        print('-Type "I" to enter the name and ID number of the customer.') #printing a statement
        print('-Type "R" to read and see the records from the customer.txt file.') #printing a statement
        print('-Type "X" to exit.') #printing a statement
        User = input() #getting the value typed by the user and assigning it to variable named User
        User = User[0].upper() #converting the first letter inputed into Uppercase
        
    return User #returning the value in User for further use
        
def Part_1(): #defining a function named Part_1
    Inputs_1 = open("customer.txt","w") #opening the file 'customer.txt' for writing purpose
    Name1 = input("Enter your name:") #asking the user to input the name of the customer
    ID1 = input("Enter your ID number:") #asking the user to input the id number of the customer
    Inputs_1.write(Name1 + '\n') #writing the name inputed by the user into the file
    Inputs_1.write(ID1 + '\n') #writing the id number inputed by the user into the file
    Inputs_1.close() #closing the file

def Part_2(): #defining a function named Part_2
    Display_2 = open("customer.txt", "r") #opening the file 'customer.txt' for reading purpose
    Name = Display_2.readline() #reads the first line from the file and is assigned to Name variable since the first value is the name of the customer
    while Name!= '': #while loop that checks if variable Name is a blank line or not
        ID = Display_2.readline() #reads the first line from the file and is assigned to ID variable since the second value is the ID number of the customer
        Name = Name.rstrip('\n') #stripping the \n from the string after reading
        ID = ID.rstrip('\n') #stripping the \n from the string after reading
        print("Customer Name:", Name) #prints the name of the customer
        print("Customer ID number:", ID) #prints the ID number of the customer
        print() #printing a blank line
        break #function that stops the while loop
    Display_2.close() #closing the file
main() #calling the defined function main















































































