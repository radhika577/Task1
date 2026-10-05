#if block
# if True:
#     print("If Block is Executed")
# print("If Ended")

#write a program to check whether a given number is equal to 10
# n=10
# if n==10:
#     print("True: Equals to 10")
# print("program ended")

# Find total price if the bill price is greater than 5000 and discount is 15%
# bp=6000
# if bp>5000:
#     discount=0.15*bp
#     total_bill=bp-discount
#     print("Bill =",bp)
#     print("Total Bill = ",total_bill)

#if-else
# if False:
#     print("True : if block is executed")
# else:
#     print("False : else block is executed")


#check whether the number is equal to 10
# n=int(input("Enter the Number"))
# if n==10:
#     print("n =",n,"equals to 10")

#check the given number is positive or negative
# n=int(input("Enter the number :"))
# if n<0:
#     print("n =",n,"given number is negative")
# else:
#     print("n =",n,"given number is positive")

#check the biggest number among two numbers
# n1=int(input("Enter the Number :"))
# n2=int(input("Enter the Number :"))
# print("n1 =",n1)
# print("n2 =",n2)
# if n1>n2:
#     print("n1 =",n1,"is greater than n2")
# else:
#     print("n1 =",n1,"is less than n2")


#check the given number is even or not
# n=int(input("Enter the number :"))
# if n%2!=0:
#     print("The given number is odd")
# else:
#     print("The given number is not odd number")


#check given value is vowel or not
# ch=input("Enter the letter :")
# if ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U" or  ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
#     print(ch,"is Vowel")
# else:
#     print(ch,"is not Vowel")



# ch=input("Enter a Alphabet :")
# if ch>="A" and ch<="Z" or ch>="a" and ch<="z":
#     print(ch,"is an Alphabet")
# else:
#     print(ch,"is not an Alphabet")


# n=input("Enter a Digit :")
# if (n>="0" and n<="9") :
#     print(n,"is a Digit")
# else:
#     print(n,"is not a Digit")


#name-"Hero" password-Hero@123
# name=input("Enter name")
# password="Hero@123"
# if name=="Hero" and password=="Hero@123":
#     print("Login Successful")
# else:
#     print("Login Invalid")
   
# if ():
#     print("True : If conditon is Executed")    
# else:
#     print("False : Else condition is Executed")
    


# if(False):
#     print("Condition is True : If Block Executed")
# elif(True):
#     print("Condition 1 is  False and Condition2 is True : 1st Elif Block Executed")
# elif(False):
#     print("Condition 1&2 are False and Condition3 is True : 2nd Elif Block Executed")
# else:
#     print("All the Above Conditions are False")




# n=int(input("Enter a number :"))
# if (n>0):
#     print("Positive Number")
# elif(n<0):
#     print("Negative Number")
# else:
#     print("Zero")


# ch=input("Enter a value :")
# if (ch>="A" and ch<="Z" or ch>="a" and ch<="z"):
#     print("The value is alphabet")
# elif (ch>="0" and ch<="9"):
#     print("The value is Digit")
# else:
#     print("The given value is symbol")

# n=int(input("enter a value :"))
# if (n>=90):
#     print("O")
# elif (n>=71 and n<=90):
#     print("A")
# elif(n>=50 and n<=70):
#     print("B")
# elif(n>=35 and n<=50):
#     print("C")
# elif(n<35):
#     print("Fail")
# else:
#     print("All the Conditions are false")


# if (False):
#     print("Outer If Block")
#     if(True):
#         print("Inner If Block")
#     else:
#         print("Inner Else Block")
# else:
#     print("Outer Else Block")



# n1=int(input("Enter a Number :"))
# n2=int(input("Enter a Number :"))
# if (n1!=n2):
#     if (n1>n2):
#         print(n2,"smallest number")
#     else:
#         print(n1,"is smallest number")
# else:
#     print("Both are Equal")

#multiple if's posibility
# if(True):
#     print("First If")
# if (False):
#     print("Second If")
# if (True):
#     print("third If")

#match case
# ch=3
# match ch:
#     case 1:
#         print("Case 1")
#     case 2:
#         print("Case 2")
#     case 3:
#         print("Case 3")
#     case 4:
#         print("Case 4")
#     case _:
#         print("Default Case")


# color="red"
# match color:
#     case "red":
#         print("All the vehicles should stop")
#     case "orange":
#         print("Start Bike and Get Ready to go")
#     case "green":
#         print("Go,Have a Safe Ride")
#     case _:
#         print("Traffic Light Error")

# sides=int(input("Enter a Number :"))
# match sides:
#     case 3:
#         print("Triangle")
#     case 4:
#         print("Square")
#     case 5:
#         print("Pentagon")
#     case 6:
#         print("Hexagon")
#     case _:
#         print("Enter a Valid No.of sides")
        


# day=int(input("Enter a Number :"))
# match day:
#     case 0:
#         print("Sunady")
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case _:
#         print("Enter a Valid number to evaluate day")

# n1=5
# n2=10
# opr="-"
# match opr:
#     case "+":
#         print("sum =",(n1+n2))
#     case "-":
#         print("sub =",(n1-n2))
#     case "*":
#         print("mul =",(n1*n2))
#     case "//":
#         print("div =",(n1//n2))
#     case "%":
#         print("remainder",(n1%n2))



# n1=int(input("Enter a Number"))
# n2=int(input("Enter a Number"))
# print("Select an option from the given choices:")
# print("1.Add")
# print("2.Sub")
# print("3.Mul")
# print("4.Division")
# print("5.Remainder")
# opt=int(input("Your Choices :"))
# match opt:
#     case 1:
#         print("Sum =",(n1+n2))
#     case 2:
#         print("Sub =",(n1-n2))
#     case 3:
#         print("Mul =",(n1*n2))
#     case 4:
#         print("Division =",(n1//n2))
#     case 5:
#         print("Remainder =",(n1%n2))
#     case _:
#         print("Default Operator")


# f_name="Innomatics"
# m_name="Research"
# l_name="Lab"
# full_name=f_name+" "+m_name+" "+l_name
# print("Institute Name is :"+full_name)

# name="Hero"
# age=25
# gender="m"
# salary=30000
# print("My Name is :"+name+"My age is :"+str(age)+"Gender :"+gender+"Salary :"+str(salary))

# print(f"My name is {name} My Age is {age} Gender {gender} Salary {salary}")


#if-else task
#check whether given number is a 3digit number or not
# n=int(input("Enter a Number :"))
# if (n<1000 and n>99):
#     print(n,"is a 3-digit Number")
# else:
#     print(n,"is not a 3-digit Number")


#check whether a given number is divisible by both 3 and 5 or not
# n=int(input("Enter a Number :"))
# if (n%3==0 and n%5==0):
#     print(n,"divisible by both 3 and 5")
# else:
#     print(n,"not divisible by both 3 and 5")


#check whether a given triangle is a valid or not
# a=int(input("Enter a Number :"))
# b=int(input("Enter a Number :"))
# c=int(input("Enter a Number :"))
# if (a+b>c and b+c>a and c+a>b):
#     print("The given Triangle is a valid Triangle")
# else:
#     print("The given Triangle is not a valid Triangle")


#check whether the given number is multiple of 10 or not
# n=int(input("Enter a Number :"))
# if (n%10==0):
#     print(n,"The given Number is Multiple of 10")
# else:
#     print(n,"The given Number is not Multiple of 10")


#if-elif-else
#check the type of triangle based on its sides Equilateral Isosceles or Scalene
# a=int(input("Enter a Number :"))
# b=int(input("Enter a Number :"))
# c=int(input("Enter a Number :"))
# if (a==b and b==c and a==c):
#     print("The given triangle is a Equilateral Triangle")
# elif (a==b and b!=c and a!=c):
#     print("The given triangle is a Isosceles Triangle")
# elif (a!=b and b!=c and a!=c):
#     print("The given triangle is a Scalene Triangle")
# else:
#     print("Check whether the input is valid for above condition.")


#calculate the electricity bill based on units consumed
# units=int(input("Enter a Number"))
# if (units<=100):
#     bill_amount=units*2
#     print("Total Bill Amount =",bill_amount)
# elif (units<=200):
#     bill_amount=units*3
#     print("Total Bill Amount =",bill_amount)
# elif (units<=300):
#     bill_amount=units*5
#     print("Total Bill Amount =",bill_amount)
# elif (units>300):
#     bill_amount=units*7
#     print("Total Bill Amount =",bill_amount)
# else:
#     print("Enter valid Units consumed.")


#Display the age category
# age=int(input("Enter the age :"))
# if (age<13):
#     print(age,"Belongs to child category")
# elif (age<=19):
#     print(age,"Belongs to Teenager category")
# elif (age<=59):
#     print(age,"Belongs to Adult category")
# elif (age>=60):
#     print(age,"Belongs to Senior Citizen category")


#calculate the discount based on shopping amount
# amount=int(input("Enter the Amount :"))
# if (amount<1000):
#     print("No Discount")
# elif (amount<=4999):
#     discount=(amount*10)/100
#     print("Discount is 10% for",amount)
#     print("Discount for shopping amount is",discount)
# elif (amount<=9999):
#     discount=(amount*20)/100
#     print("Dicount is 20% for",amount)
#     print("Discount for shopping amount is",discount)
# else:
#     discount=(amount*30)/100
#     print("Dicount is 30% for",amount)
#     print("Discount for shopping amount is",discount)

#display the season based on month number 
# month=int(input("Enter the  Month :"))
# if (month==3 or month==4 or month==5):
#     print("It is a Spring Season")
# elif (month==6 or month==7 or month==8):
#     print("It is Summer Season")
# elif (month==9 or month==10 or month==11):
#     print("It is Autumn Season")
# elif (month==12 or month==1 or month==2):
#     print("It is Winter Season")


#check the given year is leap year or not | condition1: year%400==0 and condition2 : year%4==0 and year%100!=0
# year=int(input("Enter the Year :"))
# if (year%400==0):
#     print(year,"given year is a Leap Year")
# elif (year%4==0 and year%100!=0):
#     print(year,"given year is a Leap Year")
# else:
#     print(year,"given year is not a Leap Year")



#Nested if 
#check whether the person is eligible to donate based on conditions:*age should be in between 18-60 *if the person eligible check weight and weight should be above 50.
# age=int(input("Enter the Age :"))
# if (age>=18 and age<=60):
#     print("Check Weight of the Person")
#     weight=int(input("Enter the Weight :"))
#     if (weight>50):
#         print("The Person is Eligible to Donate Blood ")
#     else:
#         print("The person is not Eligible by weight to Donate Blood")
# else:
#     print("The Persons are Eligible who are in between age 18-60")


#display the grade of student by avg of total marks and the student should pass all 4 subjects
# m1=int(input("Enter the Subject 1 marks :"))
# m2=int(input("Enter the Subject 2 Marks :"))
# m3=int(input("Enter the Subject 3 Marks :"))
# m4=int(input("Enter the Subject 4 Marks :"))
# if (m1>=40 and m2>=40 and m3>=40 and m4>=40):
#     print("The student passed all 4 subjects")
#     avg=(m1+m2+m3+m4)/4
#     if  (avg>=75):
#         print("Grade A")
#     elif (avg>=60):
#         print("Grade B")
#     elif (avg>=50):
#         print("Grade C")
#     else:
#         print("Grade D")
# else:
#     print("Student Failed in one or more Subjects")


#check whether the student is eligible for scholar ship by age and if eligible by age score should be above 86
# age=int(input("Enter the Student Age :"))
# if (age>=18):
#     score=int(input("Enter the Student Score :"))
#     if (score>86):
#         print("The Student Eligible For the Scholarship.")
#     else:
#         print("The Student doesnot Eligible For the Scholarship.")
# else:
#     print("The age should be above 18.")


