try:
    a=int(input("Enter the number :"))
    b=int(input("Enter the number :"))
    print(a+b)
except:
    print("Error Occured Check!!!!")

#---------------------------------------------------------------------------------------------

#=======Some Operations Using Exception Handling========

# 1.Syntax Error Check
# Write a small code snippet that will produce a compile-time (syntax) error. Then fix it.
# Example: Missing colon in an if statement.

# if
# print("Hello")
#---------------------------------

# 2.ZeroDivisionError
# Take two numbers from the user and perform division. Handle the case when the denominator is 0.

try:
    a=6
    print(a/0)
except ZeroDivisionError:
    print("Divison by zero is not possible so give a number other than 0")
#------------------------------------

# 3.ValueError
# Ask the user for their age. Handle the case when the user enters a string instead of a number.

try:
    a=int(input("Enter your age: "))
    print(f"Your Age is {a} years")
except ValueError:
    print("Please give age as a Number Not String!!!")
#---------------------------------

# 4.TypeError
# Try adding an integer and a string together. Handle the error.

try:
    a=5
    b="hello"
    print(a+b)
except TypeError as e:
    print("We can't add integer and string together ",e)
#---------------------------------------

# 5.Finally Block
# Write a program that takes an integer input. No matter what error occurs, print "Program Completed" using finally.

try:
    a=5
    b="hello"
    print(a+b)
except:
    print("We can't add integer and string together ")

finally:
    print("Programm Completed!!")
#-----------------------------------

# 6.Multiple Exceptions
# Ask the user for two numbers and perform division. Handle both ZeroDivisionError and ValueError separately.

try:
    a=int(input("Enter the Number: "))
    b=int(input("Enter the Number: "))
    print(a/b)
except ZeroDivisionError:
    print("Divison by zero is not possible so give a number other than 0")
except ValueError:
    print("we can't perform division of a number with String")
finally:
    print("Programm Completed!!!")
#------------------------------------

# 7.File Handling Error
# Try to open a file named student_data.txt. If it doesn’t exist, show a proper error message.

try:
    with open("./students_data.txt",'r')as f:
        print(f.read())
except FileNotFoundError as e:
    print("There is no file with given Name",e)
#------------------------------------------------------

# 8.Catch All Exceptions
# Write a program that asks for a number and prints its square. Use Exception to handle any unexpected errors.

try:
    a=int(input("Enter a Number: "))
    print(a**2)
except ValueError as e:
    print("It must be a Number",e)
#-------------------------------------

# 9.Safe Calculator
# Create a simple calculator (add, subtract, multiply, divide) that takes input from the user. 
# Handle errors like invalid input, division by zero, etc.
try:
    a=int(input("Enter a Number: "))
    b=int(input("Enter a Number: "))
    choice=int(input("Enter your choice 1/2/3/4 : "))
    if choice==1:
        print(a+b)
    elif choice==2:
        print(a-b)
    elif choice==3:
        print(a*b)
    elif choice==4:
        print(a/b)
except ZeroDivisionError as e:
    print("we cant divide a number with zero",e)
except ValueError as e:
    print("Invalid Input")
finally:
    print("Code Completed!!!!")




