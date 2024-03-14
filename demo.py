#qus-1 :Take values of length and breadth of a rectangle from user and check if it is
# square or not.

lengthValue = float(input("Enter the LEGTH value of the rectangle:"))
widthValue = float(input("Enter the WIDTH value of the rectangle:"))

if lengthValue == widthValue :
    print(f"rectangle is square : {lengthValue * widthValue}")
else:
    print(f"rectangle is not square : {lengthValue * widthValue}")

#qus-2 : A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
   #Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.

print("Will give discount of 10% if the cost of purchased quantity is more than 1000")

print("One unit will cost 100")

ans_unit = int(input("How many units you want to take :"))

if ans_unit > 10 :
    main_valeo = ((100 * ans_unit) *.1 )
    print(f"Your cost {((100 * ans_unit) - main_valeo )} tk")
    print(f"There will be a discount from the shopkeeper :{main_valeo} tk")
else:
    print(f"Your cost {(100 * ans_unit) } tk")


# qus - 3:A school has following rules for grading system:
    # a. Below 25 - F
    # b. 25 to 45 - E
    # c. 45 to 50 - D
    # d. 50 to 60 - C
    # e. 60 to 80 - B
    # f. Above 80 - A
    # Ask user to enter marks and print the corresponding grade.


valeo = float(input("Enter your number :"))

if valeo > 80 and valeo <= 100 :
    print("Your Grade is: A")
elif valeo > 60 and valeo <= 80:
    print("Your Grade is: B")
elif valeo > 50 and valeo <= 60:
    print("Your Grade is: C")
elif valeo > 45 and valeo <= 50:
    print("Your Grade is: D")
elif valeo > 25 and valeo <= 45:
    print("Your Grade is: E")
elif valeo >= 0 and valeo <= 25:
    print("Your Grade is: F")
else:
    print("There is a problem with your number")


# qus -4 :Write a program to print absolute value of a number entered by user. E.g.-
# INPUT: 1 OUTPUT: 1
# INPUT: -1 OUTPUT: 1


inp = int(input("Enter one Integer value :"))

if 0 <= inp:
    print(inp)
else:
    print(inp * -1 )


#qus -4 :ake input of age of 3 people by user and determine oldest and
# youngest among them.

youngest_1 = int(input("Enter your age :"))
youngest_2 = int(input("Enter your age :"))
youngest_3 = int(input("Enter your age :"))

alist = [f"1st youngest man : {youngest_1} ", f"2nd youngest man : {youngest_2} ", f"3rd youngest man : {youngest_3} "]

print(f"{max(alist)} year is Biggest")
print(f"{min(alist)} year is Smallest")

#qus -5:A student will not be allowed to sit in exam if
# his/her attendence is less than 75%.
# Take following input from user Number of classes held Number of
# classes attended. And print percentage of class attended Is student is
# allowed to sit in exam or not.

totalStudent = int(input("Enter total student :"))
presentStudent = int(input("Enter present student :"))

persent = ((100 * presentStudent) / totalStudent)

qus = input("Could you not come because of illness? : Answare Y ro N:")
if persent < 75 :
    print(f"Since the number of students present is: {(int(persent))}% ,So they cannot appear in the exam")
elif qus == "Y":
    print(f"Since the number of students present is: {(int(persent))}% ,So they can participate in the exam")
else:
    print(f"Since the number of students present is: {(int(persent))}% ,So they can participate in the exam")
