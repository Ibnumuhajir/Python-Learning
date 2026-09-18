# Question 1
User=(input("Enter your name:"))
print("Welcome ",User)
# Question 2
User=int(input("Enter your Age:"))
print("You Are",User,"Years Old")
# Question 3
Name=(input("Enter your Name:"))
Age=(input("Enter your age:"))
City=(input("Enter your City:"))
print(f"My Name is {Name},Iam {Age} Years old,Iam Living in {City}.")
# Question 4
Num_1=float(input("Enter the First number"))
Num_2=float(input("Enter the second number"))
print(f"Sum is: {Num_1 + Num_2}")
print(f"Difference: is {Num_1 - Num_2}")
print(f"Product: {Num_1*Num_2}")
print(f"division is: {Num_1/Num_2}")
# Question 5
User_1=int(input("Enter the Length of rectangle:"))
User_2=int(input("Enter The Width of Rectangle:"))
print(f"Its Area is {User_1*User_2}")
# Question 6
User_1=int(input("Enter the Length of rectangle:"))
User_2=int(input("Enter The Width of Rectangle:"))
print(f"Its Perimeter is: {User_1+User_2*2}")
# Question 7
User=float(input("Enter The side of square:"))
print(f"Area is: {User**2},&,perimeter is: {4*User}")
# Question 8
User=float(input("Enter the Radius of circle: "))
print(f"Its Area {3.14*(User**2)}")
# Question 9
User=float(input("enter a temperature in Celsius:"))
print(f"convert into Fahrenheit is: {(User*9/5)+32}")
# Question 10
User=float(input("enter a temperature in Fahrenheit:"))
print(f"Convert into Celsius is: {(User-32)*5/9}")
# Question 11
User=int(input("Enter your birth year:"))
current_year = 2026
age = current_year - User
print(f"You are approximately {age} years old.")
# Question 12
User=float(input("Enter the number of days:"))
print(f"days are: {User//7},Remaining Days: {User%7}")
# Question 13
User=float(input("Enter the number of Second:"))
print(f"In minute: {User//60},Remaining Days: {User%60}")
# Question 14
User= int(input("Enter the amount in rupees:"))
User1=float(input("Enter the discount in percentage:"))
print(f"The discount amount is: {User*User1/100}")
print(f"The final amount: {User-User1}")
# Question 15
User= int(input("Enter the price of product:"))
User1=int(input("Enter the quantity:"))
print(f"The total bill is: {User*User1}")
# Question 16
User= int(input("Enter the total bill:"))
User1= int(input("Enter the number of people"))
print(f"Each person should take: {User//User1}")
# Question 17
User= int(input("Enter the basic salary:"))
HRA=20/100*User
DA=10/100*User
Gross_salary=User+HRA+DA
print("Basic salary:",User)
print("HRA is:",HRA)
print("DA is: ",DA)
print("Gross Salary is: ",Gross_salary)
# Question 18
a=int(input("Enter the Priciple amount: "))
b=float(input("Enter the Rate of Interest:"))
c=int(input("Enter the Time:"))
print(f"The simple Interest is: {(a*b*c)/100}")
# Question 19
a= float(input("Enter the 1 subject mark:"))
b= float(input("Enter the 2 subject mark:"))
c= float(input("Enter the 3 subject mark:"))
d= float(input("Enter the 4 subject mark:"))
e= float(input("Enter the 5 subject mark:"))
Total_Mark=a+b+c+d+e
Average=Total_Mark/5
print("Total Marks is: ",Total_Mark)
print("The average mark: ",Average)
# Question 20
User=float(input("Enter a number:"))
print(f"the square is: {User*User}")
print(f"the cube is: {User*User*User}")





