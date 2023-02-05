# Name:Robi Gurung
# Date:7 September 2016
# CRN 21952
# Homework-1

# Sales Tax: Write a program that will ask the user to enter the amount of a
# purchase. The program should then compute the state and county sales tax. Assume the
# state sales tax is 4 percent and the county sales tax is 2 percent. The program should
# display the amount of the purchase, the state sales tax, the county sales tax, the total
# sales tax, and the total of the sale (which is the sum of the amount of purchase plus the
# total sales tax).

print ('Enter the amount of a purchase:')
Amount=float(input())
StateSalesTax=Amount*0.04
CountySalesTax=Amount*0.02
TotalSalesTax=round(StateSalesTax+CountySalesTax,2)
TotalSales=round(Amount+TotalSalesTax,2)

print('The amount of purchase is:$',Amount)
print('The states sales tax on the purchase is:$',StateSalesTax)
print('The county sales tax on the purchase is:$',CountySalesTax)
print('The total sales tax on the purchase is:$',TotalSalesTax)
print('The total of the sale is:$',TotalSales)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Celsius Fahrenheit Temperature Converter: Write a program that converts Celsius
# temperatures to Fahrenheit temperatures. The formula is as follows: F = 9/5*C + 32. The
# program should ask the user to enter a temperature in Celsius, and then display the
# temperature converted to Fahrenheit.

print('Enter the Celsius temperature:')
CT=float(input())
FT=9/5*CT+32

print('The temperature in Fahrenheit is:',FT)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Stock Transaction Program: Last month Joe purchased some stock in Acme Software,
# Inc. Here are the details of the purchase:
# 1.The number of shares that Joe purchased was 1,000.
# 2.When Joe purchased the stock, he paid $32.87 per share.
# 3.Joe paid his stockbroker a commission that amounted to 2 percent of the amount he paid for the stock.
# Two weeks later Joe sold the stock. Here are the details of the sale:
# 1.The number of shares that Joe sold was 1,000.
# 2.He sold the stock for $33.92 per share.
# 3.He paid his stockbroker another commission that amounted to 2 percent of the amount he received for the stock.
# Write a program that displays the following information:
# The amount of money Joe paid for the stock.
# The amount of commission Joe paid his broker when he bought the stock.
# The amount that Joe sold the stock for.
# The amount of commission Joe paid his broker when he sold the stock.
# Display the amount of money that Joe had left when he sold the stock and paid his broker (both times). If this amount is positive, then Joe made a profit. If the amount is negative, then Joe lost money.

Shares1= 1000
Costpershare1= 32.87
TotalStock1= Shares1*Costpershare1
Commission1= TotalStock1*0.02
print('The amount of money that Joe paid for the stock is:$',TotalStock1)
print('The amount of commission that Joe paid to his broker when he bought the stock is:$',Commission1)
Shares2=1000
Costpershare2=33.92
TotalStock2=Shares2*Costpershare2
Commission2=TotalStock2*0.02
print('The amount of money that Joe sold the stock for is:$',TotalStock2)
print('The amount of commission that Joe paid to his broker when he sold the stock is:$',Commission2)
A=TotalStock1-Commission1
B=TotalStock2-Commission2
C=A-B
D=B-A
if C>D:
    print("Joe made a loss of $",C)
else:
    print("Joe made a profit of $",D)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


