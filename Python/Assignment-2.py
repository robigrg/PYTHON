# Name: Robi Gurung
# Date: 16 September 2016
# CRN: 21952
# Homework-2

# The area of a rectangle is the rectangle's length times its width.
# Write a program that asks for the length and width of two rectangles.
# The program should tell the user which rectangle has the greater area,
# or if the areas are the same.
def Area(): #creating a user-defined function named as Area()
    print('Enter the length of the first rectangle:') #asking the user for the length of first rectangle
    length1=input() #taking input of the length of the first rectangle
    length1=float(length1) #conversion into float type
    print('Enter the width of the first rectangle:') #asking the user for the width of first rectangle
    width1=input() #taking input of the width of the first rectangle
    width1=float(width1) #conversion into float type
    Area1=length1*width1 #calulating the area of the first rectangle


    print('Enter the length of the second rectangle:') #asking the user for the length of second rectangle
    length2=input() #taking input of the length of the second rectangle
    length2=float(length2) #conversion into float type
    print('Enter the width of the second rectangle:') #asking the user for the width of second rectangle
    width2=input() #taking input of the width of the second rectangle
    width2=float(width2) #conversion into float type
    Area2=length2*width2 #calculating the area of the second rectangle

    if Area1>Area2: #checking if the area of the first rectangle is greater than the second one
        print('The first rectangle has the greater area.') #displaying that the first rectangle has a greater area after the condition became true
    elif Area1<Area2: #checking if the area of the secong retangle is greater than the first one
        print('The second rectangle has the greater area.') #displaying that the second rectangle has a greater area after the condition became true
    else: #the last condition that sets a default value if the above mentioned condition does not work out
        print('Both of the rectangle has the same area.') #displaying that both of the rectangle has the same area 

Area() #calling the defined function

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Serendipity Booksellers has a book club that awards points to its customers
# based on the number of books purchased each month. The points are awarded
# as follows:
# -If a customer purchases 0 books, he or she earns 0 points.
# -If a customer purchases 1 book, he or she earns 5 points.
# -If a customer purchases 2 books, he or she earns 15 points.
# -If a customer purchases 3 books, he or she earns 30 points.
# -If a customer purchases 4 books, he or she earns 60 points.
# Write a program that asks the user to enter the number of books that he or
# she has purchased this month and displays the number of points awarded.

def Points(): #creating a user-defined function named as Points()
    print('Enter the number of books that you have purchased this month:') #asking the user for the number of books that he or she had purchased this month
    number=input() #taking input of the number of books bought by the user
    number=int(number) #conversion into integer data type

    if number==0: #checking if the number of books that the user had bought is 0 or not
        print('You have earned 0 points.') #output showing that the user had earned 0 points for not buying any book
    elif number==1: #checking if the number of books that the user had bought is 1 or not
        print('You have earned 5 points.') #output showing that the user had earned 5 points for buying 1 book
    elif number==2: #checking if the number of books that the user had bought is 2 or not
        print('You have earned 15 points.') #output showing that the user had earned 15 points for buying 2 books
    elif number==3: #checking if the number of books that the user had bought is 3 or not
        print('You have earned 30 points.') #output showing that the user had earned 30 points for buying 3 books
    elif number==4: #checking if the number of books that the user had bought is 4 or not
        print('You have earned 60 points.') #output showing that the user had earned 60 points for buying 4 books

    print('Thank-You for shopping with us.') #displaying a statement

Points() #calling the defined function

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# The Fast Freight Shipping Company charges the following rates:
#       Weight Of Package                          Rate per Pound
#         2 lbs or less                                 $1.10
#         Over 2 lbs but not more than 6 lbs            $2.20
#         Over 6 lbs but not more than 10 lbs           $3.70
#         Over 10 lbs                                   $3.80
# Write program that asks the user to enter the weight of a package and then
# displays the shipping charges.

def Shipping(): #creating a user-defined function named as Shipping()
    print('Enter the weight of the package:') #asking the user to input the weight of the package
    weight=input() #taking the input of the weight of the user's package
    weight=float(weight) #conversion into float data type

    if weight<=2: #condition checking whether the weight of the package is less and equal to 2lbs or not
        print('The Shipping Charges is $1.10 per pound.') #displaying the shipping charge rate per pound for the inputed weight
        charge=weight*1.10 #calculating the total amount of shipping charge for the weight inputed which falls true on the above condition
        print('The total shipping charge is:$',charge) #displaying the total amount of the shipping charge with the above conditions
    elif weight>2 and weight<=6: #condition checking whether the weight of the package is greater than 2 lbs and less than and equal to 6 lbs
        print('The Shipping Charges is $2.20 per pound.') #displaying the shipping charge rate per pound for the inputed weight
        charge=weight*2.20 #calculating the total amount of shipping charge for the weight inputed which falls true on the above condition 
        print('The total shipping charge is:$',charge) #displaying the total amount of the shipping charge with the above conditions
    elif weight>6 and weight<=10: #condition checking whether the weight of the package is greater than 6 lbs and less than and equal to 10 lbs
        print('The Shipping Charges is $3.70 per pound.') #displaying the shipping charge rate per pound for the inputed weight
        charge=weight*3.70 #calculating the total amount of shipping charge for the weight inputed which falls true on the above condition
        print('The total shipping charge is:$',charge) #displaying the total amount of the shipping charge with the above conditions
    elif weight>10: #condition checking whether the weight of the package is greater than 10 lbs or not
        print('The Shipping Charges is $3.80 per pound.') #displaying the shipping charge rate per pound for the inputed weight
        charge=weight*3.80 #calculating the total amount of shipping charge for the weight inputed that falls true ont the above condition
        print('The total shipping charge is:$',charge) #displaying the total amount of the shipping charge with the above conditions

    print('Thank-you!') #displaying a statement

Shipping() #calling the defined function

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    



























































